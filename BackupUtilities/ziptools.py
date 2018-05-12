# config.py by Ramesh Balaji
# Part of ImageBak, Image Backup System for all Operating Systems, controlled in software, not by preboot
#
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import bz2

import shutil
import zipfile
from Configuration import config


def compress_dir(dirname, target):
    """Compress a directory to a bzip2 image"""
    shutil.make_archive('tmp', 'zip', dirname)
    with open('tmp.zip', 'rb') as data:
        bz2_compress = bz2.compress(data.read(), int(config.get_value('compression_level')))
        with open(target, 'wb') as writedata:
            writedata.write(bz2_compress)

    os.remove('tmp.zip')

def decompress_dir(archivename, target_parent_dir, dirname):
    """Copies the zip_bz2 file to the specified target parent directory under folder dirname, returns false if directory exists"""

    try:
        if dirname[-1] == "/":
            os.mkdir(target_parent_dir + dirname)
        else:
            os.mkdir(target_parent_dir + "/" + dirname)
    except FileExistsError:
        return False
    with open(archivename, 'rb') as data:
        bz2_decompress = bz2.decompress(data.read())

    with open(dirname + ".zip", 'wb') as bz2data:
        bz2data.write(bz2_decompress)

    zipobj = zipfile.ZipFile(dirname+'.zip', 'r')
    if dirname[-1] == "/":
            zipobj.extractall(target_parent_dir + archivename)
    else:
            zipobj.extractall(target_parent_dir + "/" + dirname)
    zipobj.close()

    os.remove(dirname + '.zip')

        