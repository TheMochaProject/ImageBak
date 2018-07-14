import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from time import gmtime, strftime,localtime

from Configuration import config
import shutil
import BackupUtilities.ziptools as ziptools
import traceback

class Backup:
    def __init__(self):
        self.backup_dir = config.get_value("backuploc")
        self.folders_to_backup = config.get_value('folderstobak').strip().split(';')
        self.backup_time = strftime('%Y_%m_%d_%H_%M_%S', localtime())
        self.back_path = self.backup_dir.strip() + "/backup_" + self.backup_time
        #print(self.back_path)
        if os.path.exists(self.back_path):
            sys.stderr.write('FATAL: The directory to back up to exists.\n')
        else:
            print("DEBUG: creating directory " + self.back_path)
            os.makedirs(self.back_path)
    def backup(self):
        success = True
        for folder in self.folders_to_backup:
            if os.path.exists(folder):
                try:
                    print("DEBUG: backing dir: " + folder + " to back_path: " + self.back_path)
                    ziptools.compress_dir(folder, self.back_path + "/"+ os.path.basename(folder) + ".zip")
                except:
                    success = False
                    sys.stderr.write("FATAL: An error occured and the backup could not be completed")
                    traceback.print_exc()
        if success:
            print("DEBUG: backup of dirs: " + str(self.folders_to_backup) + " has been completed" )