# config.py by Ramesh Balaji
# Part of ImageBak, Image Backup System for all Operating Systems, controlled in software, not by preboot
#
#

import bz2
import os
import tarfile

def compress_dir(dirname, target):
    """Compress a directory to a bzip2 image"""
    tarobject = tarfile.open(target, "w")
    tarobject.add(dirname, arcname=target)
    tarobject.close()

def make_tarfile(source_dir, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
