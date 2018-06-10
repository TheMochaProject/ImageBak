import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from Configuration import config
global builder
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
            if config.get_value('folderstobak').strip() == "":
                config.set_value('folderstobak', filename.strip())
       	    else:
                config.set_value('folderstobak', config.get_value("folderstobak").strip() + ";" + filename.strip())

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

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
        elif response == Gtk.ResponseType.NONE:
     	    print("No response recorded!")
        builder.get_object("entry1").set_text(config.get_value("backuploc"))
        dialog.destroy()
def run():
    script_running_in_full = os.path.dirname(os.path.realpath(__file__))
    print("DEBUG: os.getcwd basename is: " + script_running_in_full)
    builder.add_from_file(script_running_in_full + "/Preferences.glade")

    builder.connect_signals(Handlers())
    builder.get_object("prefswin").connect('destroy', Gtk.main_quit)
    folderstobak_list = config.get_value('folderstobak').strip().split(';')
    label_dict = {}
    for folder in folderstobak_list:
        label_to_insert = Gtk.Label(folder)
        label_dict[folder] = label_to_insert
        temp_gtklistboxrow = Gtk.ListBoxRow()
        temp_gtklistboxrow.add(label_to_insert)
        builder.get_object('folders_listbox').add(temp_gtklistboxrow)
    #builder.get_object("entry").set_text(config.get_value("folderstobak").strip())
    builder.get_object("entry1").set_text(config.get_value("backuploc").strip())
    window = builder.get_object("prefswin")
    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    run()
