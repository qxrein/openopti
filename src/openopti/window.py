import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from .menubar import create_menubar
from .component_library import ComponentLibrary
from .canvas import DesignCanvas

class MainWindow(Gtk.ApplicationWindow):
    """The main application window."""
    def __init__(self, app):
        super().__init__(application=app, title="OpenOpti")
        self.set_default_size(1280, 720)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(main_box)

        menubar = create_menubar(self)
        main_box.append(menubar)

        main_pane = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        main_pane.set_vexpand(True)
        main_pane.set_resize_start_child(False)
        main_pane.set_position(250)
        main_box.append(main_pane)

        comp_library = ComponentLibrary()
        main_pane.set_start_child(comp_library)

        canvas = DesignCanvas()
        main_pane.set_end_child(canvas)
