#!/usr/bin/env python
# minimal manage placeholder
from django.core.management import execute_from_command_line
import os, sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","ezlabs_translation.settings")
    execute_from_command_line(sys.argv)
