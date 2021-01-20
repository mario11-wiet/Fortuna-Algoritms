#!C:\Users\Mariusz\PycharmProjects\untitled1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'lines==0.1.0a0','console_scripts','lines'
__requires__ = 'lines==0.1.0a0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('lines==0.1.0a0', 'console_scripts', 'lines')()
    )
