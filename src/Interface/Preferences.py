# config.py by Ramesh Balaji
# Part of ImageBak, Image Backup System for all Operating Systems, controlled in software, not by preboot
#
#

import gi
gi.require_version('Gtk', '3.0')
import sys
#sys.path.append("../src/Configuration")


from gi.repository import Gtk

class PreferencesWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Preferences")

        self.set_border_width(10)
        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Preferences"
        self.set_titlebar(hb)


        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(100)


        self.entryvalidatebtn= Gtk.Button("Say Data")
        self.entryvalidatebtn.connect('clicked', self.button2_handler)
        hb.pack_start(self.entryvalidatebtn)

        self.box = Gtk.VBox(spacing=6)



        self.button = Gtk.Button("Bio")

        self.entrybox = Gtk.Box(spacing=5)

        self.entrylabel = Gtk.Label("Type Things: ")

        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("type things")
        self.entrybox.pack_start(self.entrylabel, True, True, 0)
        self.entrybox.pack_start(self.entry, True, True, 0)

        self.box.pack_start(self.entrybox, True, True, 0)

        self.add(stack)
        stack.add_titled(self.button, "btn", "Pane 2")
        stack.add_titled(self.box, "box", "Pane 1")


        #self.button2 = Gtk.Button("say data")
        #self.button2.connect("clicked", self.button2_handler)
        #self.box.pack_start(self.button2, True, True, 0)
    def button2_handler(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Text Entry Notifier")
        dialog.format_secondary_text(self.entry.get_text())
        dialog.run()
        print("Dialog Closed")
        dialog.destroy()

prefwin = PreferencesWindow()
prefwin.connect('destroy', Gtk.main_quit)
prefwin.show_all()
Gtk.main()
        