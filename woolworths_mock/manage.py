##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(levelname)s]  %(filename)s[%(lineno)d]  %(message)s')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woolworths_mock.settings')
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
