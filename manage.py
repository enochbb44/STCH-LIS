#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcs_project.settings')

    # pythonw.exe (used by the scheduled tasks) gives the process no console,
    # so sys.stdout/sys.stderr are None. That crashes every management command
    # the first time it writes output (e.g. daily_summary, send_pending_alerts),
    # which is why the scheduled email jobs were failing with exit code 1.
    # Route console output to a log file so the tasks run and remain diagnosable.
    if sys.stdout is None or sys.stderr is None:
        _log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
        os.makedirs(_log_dir, exist_ok=True)
        _log = open(os.path.join(_log_dir, 'commands.log'), 'a', encoding='utf-8')
        if sys.stdout is None:
            sys.stdout = _log
        if sys.stderr is None:
            sys.stderr = _log

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
