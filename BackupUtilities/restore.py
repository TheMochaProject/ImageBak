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
        