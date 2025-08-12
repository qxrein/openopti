import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="OpenOpti")

        self.set_default_size(400, 300)

        self.label = Gtk.Label(label="Hello, Wrld!")
        self.set_child(self.label)

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.OpenOptiApp",
                         flags=0)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(self)
        
        self.window.present()

if __name__ == "__main__":
    app = MyApp()
    app.run(None)
