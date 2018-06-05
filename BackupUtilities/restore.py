import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from time import gmtime, strftime

from Configuration import config
import shutil
import BackupUtilities.ziptools as ziptools
import traceback
import glob

class Restore:
    """Restore an ImageBak backup"""
    def __init__(self):
        self.restore_dir = config.get_value('folderstobak')
        self.backups_dir = config.get_value('backuploc')
        self.restore_dirmapper = {}
        for dir in self.restore_dir.split(';'):
            dir = dir.strip()
            print(dir)
            self.restore_dirmapper[os.path.basename(dir)] = dir
        print(self.restore_dirmapper)
    def restore(self, month, day, year, hours, minutes, seconds):
        """Restore a set backup"""
        print("DEBUG: Restoring from "+ self.backups_dir.strip() + "/" + self.__getBackupLocation(month, day, year, hours, minutes, seconds)  + "/*.zip")
        for filename in glob.glob(self.backups_dir.strip() + "/" + self.__getBackupLocation(month, day, year, hours, minutes, seconds)  + "/*.zip"):
            print("DEBUG: restoring " + filename + " to " + self.restore_dirmapper.get(os.path.basename(filename).split('.')[0]))
            shutil.rmtree(self.restore_dirmapper.get(os.path.basename(filename).split('.')[0]))
            ziptools.decompress_dir(filename, self.restore_dirmapper.get(os.path.basename(filename).split('.')[0]))



    def __getBackupLocation(self, month, day, year, hours, minutes, seconds):
        backup_name = "backup_" + year + "_" + month + "_" + day + "_" + hours + "_" + minutes + "_" + seconds
        #print("backupname: " + backup_name)
        return backup_name


if __name__=='__main__':
    c = Restore()
    c.restore('05','28','2018','01','13','59')
