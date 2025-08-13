import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gio
import os
import json

class ThemeManager:
    """Managing Application Themes"""
    
    def __init__(self):
        self.current_theme = "optisystem-light"
        self.themes = {
            "optisystem-light": {
                "name": "OptiSystem Light",
                "description": "Professional light theme similar to OptiSystem",
                "css_file": "optisystem-light.css",
                "icon_theme": "Adwaita",
                "color_scheme": "light"
            },
            "optisystem-dark": {
                "name": "OptiSystem Dark", 
                "description": "Professional dark theme similar to OptiSystem",
                "css_file": "optisystem-dark.css",
                "icon_theme": "Adwaita",
                "color_scheme": "dark"
            },
            "cappuccino": {
                "name": "Cappuccino",
                "description": "Warm, cozy theme with brown tones",
                "css_file": "cappuccino.css",
                "icon_theme": "Adwaita",
                "color_scheme": "light"
            },
            "gruvbox-dark": {
                "name": "Gruvbox Dark",
                "description": "Retro groove color scheme with dark background",
                "css_file": "gruvbox-dark.css",
                "icon_theme": "Adwaita",
                "color_scheme": "dark"
            },
            "nord": {
                "name": "Nord",
                "description": "Arctic-inspired color palette",
                "css_file": "nord.css",
                "icon_theme": "Adwaita",
                "color_scheme": "dark"
            },
            "gruvbox-light": {
                "name": "Gruvbox Light",
                "description": "Retro groove color scheme with light background",
                "css_file": "gruvbox-light.css",
                "icon_theme": "Adwaita",
                "color_scheme": "light"
            }
        }
        
        self.load_theme_preference()
        
    def get_theme_path(self, css_file):
        """Get the full path to a CSS theme file."""
        theme_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "themes")
        return os.path.join(theme_dir, css_file)
    
    def apply_theme(self, theme_name):
        """Apply a specific theme to the application."""
        if theme_name not in self.themes:
            print(f"Theme '{theme_name}' not found")
            return False
            
        theme = self.themes[theme_name]
        self.current_theme = theme_name
        
        css_file = self.get_theme_path(theme["css_file"])
        if os.path.exists(css_file):
            try:
                display = Gdk.Display.get_default()
                if display:
                    if hasattr(self, '_current_provider'):
                        try:
                            Gtk.StyleContext.remove_provider_for_display(display, self._current_provider)
                        except:
                            pass
                    
                    css_provider = Gtk.CssProvider()
                    css_provider.load_from_file(Gio.File.new_for_path(css_file))
                    
                    self._current_provider = css_provider
                    
                    Gtk.StyleContext.add_provider_for_display(
                        display,
                        css_provider,
                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                    )
                    
                    print(f"Applied theme: {theme['name']} from {css_file}")
                    return True
            except Exception as e:
                print(f"Error applying CSS theme: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"CSS theme file not found: {css_file}")
        
        print(f"Could not load theme file: {css_file}")
        return False
    
    def get_available_themes(self):
        """Get list of available themes."""
        return list(self.themes.keys())
    
    def get_theme_info(self, theme_name):
        """Get information about a specific theme."""
        return self.themes.get(theme_name, {})
    
    def get_current_theme(self):
        """Get the currently active theme name."""
        return self.current_theme
    
    def save_theme_preference(self):
        """Save the current theme preference to user config."""
        config_dir = os.path.expanduser("~/.config/openopti")
        os.makedirs(config_dir, exist_ok=True)
        
        config_file = os.path.join(config_dir, "theme.json")
        config = {"theme": self.current_theme}
        
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f)
        except Exception as e:
            print(f"Error saving theme preference: {e}")
    
    def load_theme_preference(self):
        """Load the saved theme preference from user config."""
        config_file = os.path.expanduser("~/.config/openopti/theme.json")
        
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    saved_theme = config.get("theme")
                    if saved_theme in self.themes:
                        self.current_theme = saved_theme
                        self.apply_theme(saved_theme)
            except Exception as e:
                print(f"Error loading theme preference: {e}")
    
    def create_preview_theme(self, theme_name):
        """Create a preview of a theme for the preferences dialog."""
        theme = self.themes.get(theme_name, {})
        if not theme:
            return None
            
        preview_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        preview_box.set_margin_start(12)
        preview_box.set_margin_end(12)
        preview_box.set_margin_top(8)
        preview_box.set_margin_bottom(8)
        
        name_label = Gtk.Label(label=theme["name"])
        name_label.add_css_class("title-4")
        preview_box.append(name_label)
        
        desc_label = Gtk.Label(label=theme["description"])
        desc_label.add_css_class("caption")
        desc_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        desc_box.append(desc_label)
        preview_box.append(desc_box)
        
        color_preview = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        color_preview.set_margin_top(8)
        
        if "dark" in theme["color_scheme"]:
            colors = ["#2d3748", "#4a5568", "#718096", "#a0aec0"]
        else:
            colors = ["#f7fafc", "#edf2f7", "#e2e8f0", "#cbd5e0"]
            
        for color in colors:
            swatch = Gtk.Box()
            swatch.set_size_request(20, 20)
            swatch.add_css_class("color-swatch")
            color_preview.append(swatch)
        
        preview_box.append(color_preview)
        
        return preview_box 