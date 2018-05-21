import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from Configuration import config

builder = Gtk.Builder()

class Handlers:
    def entry1validate(self, widget):
        print(builder.get_object("entry").get_text())

    def entry2validate(self, widget):
        print(builder.get_object("entry1").get_text())

    def onBackupDirsBtnClicked(self, widget):
        dialog = Gtk.FileChooserDialog("Choose Another Folder: ", None, Gtk.FileChooserAction.SELECT_FOLDER,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 600)

        response = dialog.run()
        filename = ""
        if response == Gtk.ResponseType.OK:
            print(dialog.get_filename())
            filename = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        if config.get_value('folderstobak').strip() == "":
            config.set_value('folderstobak', filename.strip())
        else:
            config.set_value('folderstobak', config.get_value("folderstobak").strip() + ";" + filename.strip())

        builder.get_object("entry").set_text(config.get_value("folderstobak"))
        dialog.destroy()

    def onSelectBackupLocationBtnClicked(self, widget):
        dialog = Gtk.FileChooserDialog("Choose a Folder: ", None, Gtk.FileChooserAction.SELECT_FOLDER,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 600)

        response = dialog.run()
        filename = ""
        if response == Gtk.ResponseType.OK:
            print(dialog.get_filename())
            filename = dialog.get_filename()
            config.set_value('backuploc', filename)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        builder.get_object("entry1").set_text(config.get_value("backuploc"))
        dialog.destroy()
def run():

    builder.add_from_file("Preferences.glade")

    builder.connect_signals(Handlers())
    builder.get_object("prefswin").connect('destroy', Gtk.main_quit)
    builder.get_object("entry").set_text(config.get_value("folderstobak").strip())
    builder.get_object("entry1").set_text(config.get_value("backuploc").strip())
    window = builder.get_object("prefswin")
    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    run()