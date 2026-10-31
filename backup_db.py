"""Daily SQLite online backup for the LIS.

Uses the sqlite3 .backup API (safe to run while the server is live),
writing to <project>\\backups\\db-YYYYMMDD-HHMMSS.sqlite3 and pruning
to the newest BACKUP_KEEP files.

Schedule (Windows Task Scheduler), adjusting the paths to this deployment:
    schtasks /create /tn "LIS DB Backup" /tr "python backup_db.py" /sc daily /st 01:30

Run manually:
    python backup_db.py
"""
import glob
import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'db.sqlite3')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')
BACKUP_KEEP = 14


def main():
    if not os.path.exists(DB_PATH):
        print('DB not found:', DB_PATH)
        return 1

    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    dest = os.path.join(BACKUP_DIR, f'db-{stamp}.sqlite3')

    src = sqlite3.connect(DB_PATH)
    dst = sqlite3.connect(dest)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()

    backups = sorted(glob.glob(os.path.join(BACKUP_DIR, 'db-*.sqlite3')))
    for old in backups[:-BACKUP_KEEP]:
        os.remove(old)

    size = os.path.getsize(dest)
    print(f'Backup written: {dest} ({size:,} bytes)')
    print(f'Keeping {min(len(backups), BACKUP_KEEP)} backups of {len(backups)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
