import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from BackupUtilities import backup

backup = backup.Backup()
backup.backup()