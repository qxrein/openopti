import gi
import sys

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="OpenOpti")

        self.set_default_size(400, 300)
        label = Gtk.Label(label="Hello, Wrld!")
        self.set_child(label)

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.OpenOptiApp")

    def do_activate(self):
        window = AppWindow(self)
        window.present()

if __name__ == "__main__":
    app = MyApp()
    sys.exit(app.run(sys.argv))
