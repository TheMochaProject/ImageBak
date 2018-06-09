import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from Configuration import config
import glob

class RestoreDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Select Backup to Restore", parent, 0)
        self.set_default_size(600,100)

        self.response_vbox = Gtk.VBox(spacing=5)
        self.selected_backup = ""
        self.response_boxes = {}
        self.button_mapper = {}

        print(config.get_value('backuploc'))
        for folder in glob.glob(config.get_value('backuploc') + "/*"):
            folder_name_array = folder.split("_")
            readable_name = "Backup on " + folder_name_array[2] + "/" + folder_name_array[3] + "/" + folder_name_array[1] + " at " + folder_name_array[4] + ":" + folder_name_array[5]
            backup_box = Gtk.Box(spacing = 10)
            backup_label = Gtk.Label(readable_name)
            select_button = Gtk.Button("Select")
            select_button.connect('clicked', self.log_selected_backup)
            backup_box.pack_start(backup_label, True, True, 0)
            backup_box.pack_start(select_button, True, True, 1)
            self.response_boxes[backup_box] = folder
            self.button_mapper[select_button] = folder
        box_index = 0
        for box,folder in self.response_boxes.items():
            self.vbox.pack_start(box, True, True, box_index)
            box_index += 1
        put = self.get_content_area()
        put.add(self.response_vbox)
        self.show_all()
    def log_selected_backup(self, widget):
        self.selected_backup = self.button_mapper.get(widget)
        self.destroy()
    def get_selected_backup(self):
            return self.selected_backup
class TestWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="testwin")
        dialog = RestoreDialog(self)
        response = dialog.run()
        print(dialog.get_selected_backup())
        dialog.destroy()

if __name__ == '__main__':
    win = TestWin()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()