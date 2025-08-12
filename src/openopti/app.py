import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
from .window import MainWindow

class OpenOptiApplication(Gtk.Application):
    """The main GTK application class."""
    def __init__(self):
        super().__init__(application_id="dev.openopti.OpenOptiApp",
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        """Called when the application is activated."""
        window = MainWindow(self)
        window.present()
