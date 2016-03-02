#!/usr/bin/env python
import os
import sys
sys.path.append('/home/timothy/fiveonetwo/venv/lib/python3.4/site-packages/')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newspaper.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
