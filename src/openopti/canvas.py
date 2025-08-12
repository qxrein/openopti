import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class DesignCanvas(Gtk.Box):
    """The main area for drawing the optical circuit diagram."""
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        label = Gtk.Label(label="Design Canvas")
        label.set_vexpand(True)
        label.set_hexpand(True)
        label.add_css_class("title-1")
        
        self.append(label)
