import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
from .theme_manager import ThemeManager

class PreferencesDialog(Gtk.Dialog):
    """Preferences dialog for OpenOpti application."""
    
    def __init__(self, parent=None):
        super().__init__(
            title="Preferences",
            transient_for=parent,
            modal=True,
            destroy_with_parent=True
        )
        
        self.set_modal(True)
        self.set_resizable(True)
        
        if not parent:
            self.set_position(Gtk.WindowPosition.CENTER)
        
        self.theme_manager = ThemeManager()
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the preferences dialog UI."""
        self.set_default_size(600, 500)
        self.set_resizable(True)
        
        content_area = self.get_content_area()
        content_area.set_margin_start(20)
        content_area.set_margin_end(20)
        content_area.set_margin_top(20)
        content_area.set_margin_bottom(20)
        
        notebook = Gtk.Notebook()
        content_area.append(notebook)
        
        theme_page = self.create_theme_page()
        notebook.append_page(theme_page, Gtk.Label(label="Theme"))
        
        ui_page = self.create_ui_page()
        notebook.append_page(ui_page, Gtk.Label(label="Interface"))
        
        sim_page = self.create_simulation_page()
        notebook.append_page(sim_page, Gtk.Label(label="Simulation"))
        
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        button_box.set_halign(Gtk.Align.END)
        button_box.set_margin_top(20)
        
        apply_button = Gtk.Button(label="Apply")
        apply_button.add_css_class("suggested-action")
        apply_button.connect("clicked", self.on_apply_clicked)
        button_box.append(apply_button)
        cancel_button = Gtk.Button(label="Cancel")
        cancel_button.connect("clicked", self.on_cancel_clicked)
        button_box.append(cancel_button)
        
        ok_button = Gtk.Button(label="OK")
        ok_button.add_css_class("suggested-action")
        ok_button.connect("clicked", self.on_ok_clicked)
        button_box.append(ok_button)
        
        content_area.append(button_box)
        
    def create_theme_page(self):
        """Create the theme preferences page."""
        page_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        page_box.set_margin_start(20)
        page_box.set_margin_end(20)
        page_box.set_margin_top(20)
        page_box.set_margin_bottom(20)
        
        theme_section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        title_label = Gtk.Label(label="Theme Selection")
        title_label.add_css_class("title-3")
        theme_section.append(title_label)
        
        desc_label = Gtk.Label(label="Choose your preferred visual theme for the application.")
        desc_label.add_css_class("caption")
        desc_label.set_wrap(True)
        theme_section.append(desc_label)
        
        self.theme_list_box = Gtk.ListBox()
        self.theme_list_box.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.theme_list_box.connect("row-selected", self.on_theme_selected)
        
        for theme_key in self.theme_manager.get_available_themes():
            theme_info = self.theme_manager.get_theme_info(theme_key)
            row = self.create_theme_row(theme_key, theme_info)
            self.theme_list_box.append(row)
            
            if theme_key == self.theme_manager.get_current_theme():
                self.theme_list_box.select_row(row)
        
        theme_section.append(self.theme_list_box)
        page_box.append(theme_section)
        
        preview_section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        preview_title = Gtk.Label(label="Theme Preview")
        preview_title.add_css_class("title-3")
        preview_section.append(preview_title)
        
        preview_frame = Gtk.Frame()
        preview_frame.set_size_request(300, 150)
        preview_frame.set_margin_top(8)
        
        self.preview_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        preview_frame.set_child(self.preview_box)
        
        current_theme = self.theme_manager.get_current_theme()
        preview_widget = self.theme_manager.create_preview_theme(current_theme)
        if preview_widget:
            self.preview_box.append(preview_widget)
        
        preview_section.append(preview_frame)
        page_box.append(preview_section)
        
        return page_box
    
    def create_theme_row(self, theme_key, theme_info):
        """Create a row for the theme list."""
        row = Gtk.ListBoxRow()
        
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.set_margin_start(12)
        box.set_margin_end(12)
        box.set_margin_top(8)
        box.set_margin_bottom(8)
        
        icon = Gtk.Image.new_from_icon_name("applications-graphics")
        icon.set_pixel_size(24)
        box.append(icon)
        
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        
        name_label = Gtk.Label(label=theme_info["name"])
        name_label.add_css_class("title-4")
        info_box.append(name_label)
        
        desc_label = Gtk.Label(label=theme_info["description"])
        desc_label.add_css_class("caption")
        info_box.append(desc_label)
        
        box.append(info_box)
        box.set_hexpand(True)
        
        scheme_label = Gtk.Label(label=theme_info["color_scheme"].title())
        scheme_label.add_css_class("caption")
        scheme_label.add_css_class("dim-label")
        box.append(scheme_label)
        
        row.set_child(box)
        return row
    
    def create_ui_page(self):
        """Create the UI preferences page."""
        page_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        page_box.set_margin_start(20)
        page_box.set_margin_end(20)
        page_box.set_margin_top(20)
        page_box.set_margin_bottom(20)
        
        general_section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        title_label = Gtk.Label(label="General Interface")
        title_label.add_css_class("title-3")
        general_section.append(title_label)
        
        grid_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        grid_label = Gtk.Label(label="Show grid by default")
        grid_label.set_hexpand(True)
        grid_switch = Gtk.Switch()
        grid_switch.set_active(True)
        grid_box.append(grid_label)
        grid_box.append(grid_switch)
        general_section.append(grid_box)
        
        rulers_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        rulers_label = Gtk.Label(label="Show rulers by default")
        rulers_label.set_hexpand(True)
        rulers_switch = Gtk.Switch()
        rulers_switch.set_active(False)
        rulers_box.append(rulers_label)
        rulers_box.append(rulers_switch)
        general_section.append(rulers_box)
        
        autosave_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        autosave_label = Gtk.Label(label="Auto-save projects")
        autosave_label.set_hexpand(True)
        autosave_switch = Gtk.Switch()
        autosave_switch.set_active(True)
        autosave_box.append(autosave_label)
        autosave_box.append(autosave_switch)
        general_section.append(autosave_box)
        
        page_box.append(general_section)
        
        canvas_section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        canvas_title = Gtk.Label(label="Canvas Settings")
        canvas_title.add_css_class("title-3")
        canvas_section.append(canvas_title)
        
        spacing_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        spacing_label = Gtk.Label(label="Grid spacing (pixels)")
        spacing_label.set_hexpand(True)
        spacing_spin = Gtk.SpinButton()
        spacing_spin.set_range(5, 100)
        spacing_spin.set_value(20)
        spacing_spin.set_increments(5, 10)
        spacing_box.append(spacing_label)
        spacing_box.append(spacing_spin)
        canvas_section.append(spacing_box)
        
        snap_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        snap_label = Gtk.Label(label="Snap to grid")
        snap_label.set_hexpand(True)
        snap_switch = Gtk.Switch()
        snap_switch.set_active(True)
        snap_box.append(snap_label)
        snap_box.append(snap_switch)
        canvas_section.append(snap_box)
        
        page_box.append(canvas_section)
        
        return page_box
    
    def create_simulation_page(self):
        """Create the simulation preferences page."""
        page_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        page_box.set_margin_start(20)
        page_box.set_margin_end(20)
        page_box.set_margin_top(20)
        page_box.set_margin_bottom(20)
        
        sim_section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        title_label = Gtk.Label(label="Simulation Settings")
        title_label.add_css_class("title-3")
        sim_section.append(title_label)
        
        solver_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        solver_label = Gtk.Label(label="Default FDTD solver")
        solver_label.set_hexpand(True)
        solver_combo = Gtk.ComboBoxText()
        solver_combo.append("meep", "MEEP")
        solver_combo.append("empy", "EMpy")
        solver_combo.append("simphony", "Simphony")
        solver_combo.set_active_id("meep")
        solver_box.append(solver_label)
        solver_box.append(solver_combo)
        sim_section.append(solver_box)
        
        threads_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        threads_label = Gtk.Label(label="Number of threads")
        threads_label.set_hexpand(True)
        threads_spin = Gtk.SpinButton()
        threads_spin.set_range(1, 32)
        threads_spin.set_value(4)
        threads_spin.set_increments(1, 2)
        threads_box.append(threads_label)
        threads_box.append(threads_spin)
        sim_section.append(threads_box)
        
        results_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        results_label = Gtk.Label(label="Auto-save simulation results")
        results_label.set_hexpand(True)
        results_switch = Gtk.Switch()
        results_switch.set_active(True)
        results_box.append(results_label)
        results_box.append(results_switch)
        sim_section.append(results_box)
        
        page_box.append(sim_section)
        
        return page_box
    
    def on_theme_selected(self, listbox, row):
        """Handle theme selection."""
        if row is None:
            return
        index = row.get_index()
        theme_keys = self.theme_manager.get_available_themes()
        if 0 <= index < len(theme_keys):
            selected_theme = theme_keys[index]
            
            self.update_preview(selected_theme)
            
            # TODO: Apply theme immediately for preview.
            # self.theme_manager.apply_theme(selected_theme)
    
    def update_preview(self, theme_name):
        """Update the theme preview."""
        if hasattr(self, 'preview_box'):
            for child in self.preview_box:
                self.preview_box.remove(child)
            preview_widget = self.theme_manager.create_preview_theme(theme_name)
            if preview_widget:
                self.preview_box.append(preview_widget)
    
    def on_apply_clicked(self, button):
        """Handle Apply button click."""
        listbox = self.get_theme_listbox()
        if listbox:
            row = listbox.get_selected_row()
            if row:
                index = row.get_index()
                theme_keys = self.theme_manager.get_available_themes()
                if 0 <= index < len(theme_keys):
                    selected_theme = theme_keys[index]
                    print(f"Applying theme: {selected_theme}")
                    success = self.theme_manager.apply_theme(selected_theme)
                    if success:
                        self.theme_manager.save_theme_preference()
                        print(f"Theme '{selected_theme}' applied successfully!")
                    else:
                        print(f"Failed to apply theme '{selected_theme}'")
                else:
                    print(f"Invalid theme index: {index}")
            else:
                print("No theme row selected")
        else:
            print("Could not find theme listbox")
    
    def on_cancel_clicked(self, button):
        """Handle Cancel button click."""
        self.close()
    
    def on_ok_clicked(self, button):
        """Handle OK button click."""
        self.on_apply_clicked(button)
        self.close()
    
    def get_theme_listbox(self):
        """Get the theme listbox widget."""
        return getattr(self, 'theme_list_box', None) 