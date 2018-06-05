import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from BackupUtilities import backup, restore
import Preferences
from RestoreDialog import RestoreDialog

class Handlers:
    def preferences_open(self, widget):
        Preferences.run()

    def backup_now(self, widget):
        builder.get_object('info').set_label("Backing up..")
        backup_obj = backup.Backup()
        backup_obj.backup()
        builder.get_object('info').set_label("Backup complete!\nPress Restore to select and restore from a backup!")

    def restore_now(self, widget):
        dialog = RestoreDialog(builder.get_object("mainwin"))
        response = dialog.run()
        selected_backup = dialog.get_selected_backup().split("_")
        dialog.destroy()
        print("DEBUG: Selected backup dir is: " + str(selected_backup))
        year = selected_backup[1]
        month = selected_backup[2]
        day = selected_backup[3]
        hour = selected_backup[4]
        minute = selected_backup[5]
        second = selected_backup[6]
        restore_obj = restore.Restore()
        restore_obj.restore(month, day, year, hour, minute, second)

builder = Gtk.Builder()
builder.add_from_file("MainView.glade")
builder.connect_signals(Handlers())

window = builder.get_object("mainwin")
builder.get_object('mainwin').connect('destroy', Gtk.main_quit)
window.show_all()
Gtk.main()