import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

import Preferences
class Handlers:
    def preferences_open(self, widget):
        Preferences.run()

builder = Gtk.Builder()
builder.add_from_file("MainView.glade")
builder.connect_signals(Handlers())

window = builder.get_object("mainwin")
builder.get_object('mainwin').connect('destroy', Gtk.main_quit)
window.show_all()
Gtk.main()