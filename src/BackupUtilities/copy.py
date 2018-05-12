import shutil
import os

def copy(source_file, target_dir):
    shutil.copyfile(source_file, target_dir)

def rename(source_file, target_file):
    os.rename(source_file, target_file)
