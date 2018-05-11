import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class Handlers:
    def entry1validate(self, widget):
        print(builder.get_object("entry").get_text())

    def entry2validate(self, widget):
        print(builder.get_object("entry1").get_text())



builder = Gtk.Builder()
builder.add_from_file("Preferences.glade")

builder.connect_signals(Handlers())
builder.get_object("btn3").connect('clicked', Gtk.main_quit)
builder.get_object("prefswin").connect('destroy', Gtk.main_quit)
window = builder.get_object("prefswin")
window.show_all()

Gtk.main()

