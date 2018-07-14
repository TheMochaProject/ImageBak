import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from Configuration import config
global builder
builder = Gtk.Builder()
global label_dict
label_dict = {}
global lbr_dict
lbr_dict = {}
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
            if filename in config.get_value('folderstobak').split(';'):
                print("DEBUG: Already added, skipping...")
            else:
                if config.get_value('folderstobak').strip() == "":
                    config.set_value('folderstobak', filename.strip())
                #foldertobak previously set
       	        else:
                    config.set_value('folderstobak', config.get_value("folderstobak").strip() + ";" + filename.strip())

                filename_label = Gtk.Label(filename)
                label_dict[filename] = filename_label
                filler_listboxrow = Gtk.ListBoxRow()
                filler_listboxrow.add(filename_label)
                print("DEBUG: adding filler listboxrow to folders listbox")
                builder.get_object("folders_listbox").add(filler_listboxrow)
                builder.get_object("folders_listbox").show_all()

                #update dicts
                lbr_dict[filler_listboxrow] = filename_label
                label_dict[filename] = filename_label
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")


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

    def onRemoveBackupDirsBtnClicked(self, widget):
        corresponding_label = lbr_dict.get(builder.get_object('folders_listbox').get_selected_row())
        corresponding_folder = corresponding_label.get_text()

        selected_row = builder.get_object('folders_listbox').get_selected_row()
        print("DEBUG: Removing selected row")

        builder.get_object('folders_listbox').remove(selected_row)
        del lbr_dict[selected_row]
        del label_dict[corresponding_folder]

        #build folderstobak_str
        folderstobak_str = ""
        len_folders = len(label_dict)
        current_folder = 0
        for key, value in label_dict.items():
            folderstobak_str += key
            if len_folders - 1 != current_folder:
                folderstobak_str += ";"
            current_folder += 1
        print("DEBUG: new folders to bak str is: " + folderstobak_str)
        #write to config.cfg
        config.set_value('folderstobak', folderstobak_str)
    def onEnableDaemonSwitchEnabled(self, switch, gparam):
        if switch.get_active():
            print("DEBUG: switch enabled")
        else:
            print("DEBUG: switch disabled")
def run():
    script_running_in_full = os.path.dirname(os.path.realpath(__file__))
    print("DEBUG: os.getcwd basename is: " + script_running_in_full)
    builder.add_from_file(script_running_in_full + "/Preferences.glade")

    builder.connect_signals(Handlers())
    builder.get_object("prefswin").connect('destroy', Gtk.main_quit)
    folderstobak_list = config.get_value('folderstobak').strip().split(';')
    for folder in folderstobak_list:
        label_to_insert = Gtk.Label(folder)
        label_dict[folder] = label_to_insert
        temp_gtklistboxrow = Gtk.ListBoxRow()
        lbr_dict[temp_gtklistboxrow] = label_to_insert
        temp_gtklistboxrow.add(label_to_insert)
        builder.get_object('folders_listbox').add(temp_gtklistboxrow)
    #builder.get_object("entry").set_text(config.get_value("folderstobak").strip())
    builder.get_object("entry1").set_text(config.get_value("backuploc").strip())
    window = builder.get_object("prefswin")
    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    run()
