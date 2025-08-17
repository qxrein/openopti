import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk
from .window import MainWindow
import os

class OpenOptiApplication(Gtk.Application):
    """The main GTK application class."""
    def __init__(self):
        super().__init__(application_id="dev.openopti.OpenOptiApp",
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        
        self.load_css_styles()
    
    def load_css_styles(self):
        """Load CSS styles for the application."""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            css_file = os.path.join(current_dir, "styles.css")
            
            if os.path.exists(css_file):
                css_provider = Gtk.CssProvider()
                css_provider.load_from_path(css_file)
                
                display = Gdk.Display.get_default()
                if display:
                    Gtk.StyleContext.add_provider_for_display(
                        display,
                        css_provider,
                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                    )
                    print(f"CSS styles loaded from: {css_file}")
                else:
                    print("Warning: Could not get default display for CSS")
            else:
                print(f"Warning: CSS file not found: {css_file}")
                
        except Exception as e:
            print(f"Error loading CSS styles: {e}")

    def do_activate(self):
        """Called when the application is activated."""
        print("Creating main window...")
        window = MainWindow(self)
        print("Main window created, presenting...")
        window.present()
        print("Main window presented successfully")
        
        self.setup_global_shortcuts(window)
        print("Application activation complete")
    
    def setup_global_shortcuts(self, main_window):
        """Setup application-wide keyboard shortcuts."""
        pass
    
    def do_startup(self):
        """Called when the application starts up."""
        Gtk.Application.do_startup(self)
        
        self.set_property("application-id", "dev.openopti.OpenOptiApp")
        
        self.initialize_resources()
    
    def initialize_resources(self):
        """Initialize application-wide resources."""
        pass
    
    def do_shutdown(self):
        """Called when the application shuts down."""
        self.cleanup_resources()
        
        Gtk.Application.do_shutdown(self)
    
    def cleanup_resources(self):
        """Clean up application resources."""
        pass
