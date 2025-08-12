import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class ComponentLibrary(Gtk.Box):
    """A widget to display available optical components."""
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_margin_top(10)
        self.set_margin_bottom(10)
        self.set_margin_start(10)
        self.set_margin_end(10)

        title = Gtk.Label(label="Component Library")
        title.add_css_class("title-4")
        
        placeholder = Gtk.Label(label="Lasers\nModulators\nFibers\nDetectors...")
        placeholder.set_xalign(0)

        self.append(title)
        self.append(Gtk.Separator())
        self.append(placeholder)
