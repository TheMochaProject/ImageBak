import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from BackupUtilities import backup

import Preferences

class Handlers:
    def preferences_open(self, widget):
        Preferences.run()
    def backup_now(self, widget):
        builder.get_object('info').set_label("Backing up..")
        backup_obj = backup.Backup()
        backup_obj.backup()
        builder.get_object('info').set_label("Backup complete!\nPress Restore to select and restore from a backup!")
    def restore_now(self, widget):
        pass

builder = Gtk.Builder()
builder.add_from_file("MainView.glade")
builder.connect_signals(Handlers())

window = builder.get_object("mainwin")
builder.get_object('mainwin').connect('destroy', Gtk.main_quit)
window.show_all()
Gtk.main()