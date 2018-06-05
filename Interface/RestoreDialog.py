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
        Gtk.Dialog.__init__(self, "My Dialog", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(600,300)

        self.response_vbox = Gtk.VBox(spacing=10)

        self.response_boxes = []
        print(config.get_value('backuploc'))
        for folder in glob.glob(config.get_value('backuploc') + "/*"):
            folder_name_array = folder.split("_")
            readable_name = "Backup on " + folder_name_array[2] + "/" + folder_name_array[3] + "/" + folder_name_array[1] + " at " + folder_name_array[4] + ":" + folder_name_array[5]
            backup_box = Gtk.Box(spacing = 10)
            backup_label = Gtk.Label(readable_name)
            select_button = Gtk.Button("Select")
            backup_box.pack_start(backup_label, True, True, 0)
            backup_box.pack_start(select_button, True, True, 1)
            self.response_boxes.append(backup_box)
        box_index = 0
        for box in self.response_boxes:
            self.vbox.pack_start(box, True, True, box_index)
            box_index += 1
        put = self.get_content_area()
        put.add(self.response_vbox)
        self.show_all()

class TestWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="testwin")
        dialog = RestoreDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()


win = TestWin()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()