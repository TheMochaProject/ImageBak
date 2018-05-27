import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from time import gmtime, strftime

from Configuration import config
import shutil
import ziptools
import traceback
import glob

class Restore:
    """Restore an ImageBak backup"""
    def __init__(self):
        self.restore_dir = config.get_value('folderstobak')
        self.backups_dir = config.get_value('backuploc')
        self.restore_dirmapper = {}
        for dir in self.restore_dir:
            self.restore_dirmapper[os.path.basename(dir)] = dir
    def restore(self, month, day, year, hours, minutes, seconds):
        """Restore a set backup"""
        for filename in glob.glob(self.backups_dir + "/" + __getBackupLocation(month, day, year, hours, minutes, seconds + "*.zip"):
            zipfile.decompress_dir(filename, self.restore_dirmapper.get(os.path.basename(filename).split('.')[0]))



    def __getBackupLocation(month, day, year, hours, minutes, seconds):
        backup_name = "backup_" + year + "_" + month + "_" + day + "_" + hour + "_" + minutes + "_" + seconds
        