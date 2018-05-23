import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from time import gmtime, strftime

from Configuration import config
import shutil
import ziptools
import traceback


class Restore:
    """Restore an ImageBak backup"""
    def __init__(self):
        self.restore_dir = config.get_value('folderstobak')
        self.backups_dir = config.get_value('backuploc')

    def restore(self, month, day, year, hours, minutes, seconds):
        """Restore a set backup"""



    def __getBackupLocation(month, day, year, hours, minutes, seconds):
        backup_name = "backup_" + year + "_" + month + "_" + day + "_" + hour + "_" + minutes + "_" + seconds
        