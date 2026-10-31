"""Rotate LIS server logs.

Moves the current server_out.log / server_err.log (and server.log if present)
to a timestamped copy, then truncates the live file so it never grows without
bound. Keeps the newest ROTATE_KEEP rotated files.

Schedule with Windows Task Scheduler (daily), adjusting the path to this
deployment:
    schtasks /create /tn "LIS Log Rotation" /tr "python rotate_logs.py" /sc daily /st 02:30
"""
import glob
import os
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILES = ['server_out.log', 'server_err.log', 'server.log']
ROTATED_DIR = os.path.join(BASE_DIR, 'logs')
ROTATE_KEEP = 14


def main():
    os.makedirs(ROTATED_DIR, exist_ok=True)
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    rotated = 0
    for name in LOG_FILES:
        path = os.path.join(BASE_DIR, name)
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            continue
        dest = os.path.join(ROTATED_DIR, f'{name}.{stamp}.log')
        try:
            shutil.copy2(path, dest)
            open(path, 'w').close()
            rotated += 1
            print(f'Rotated {name} -> {dest}')
        except OSError as e:
            print(f'Failed to rotate {name}: {e}')

    for name in LOG_FILES:
        backups = sorted(glob.glob(os.path.join(ROTATED_DIR, f'{name}.*.log')))
        for old in backups[:-ROTATE_KEEP]:
            try:
                os.remove(old)
            except OSError:
                pass
    print(f'Rotated {rotated} log file(s); keeping {ROTATE_KEEP} per file.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
