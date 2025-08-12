# src/openopti/menubar.py
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject

def create_menubar(window):
    """Creates the Gtk.PopoverMenuBar for the main window that looks like OptiSystem."""
    
    action_new = Gio.SimpleAction.new("new", None)
    action_new.connect("activate", lambda a, p: print("New Project"))
    window.add_action(action_new)
    
    action_open = Gio.SimpleAction.new("open", None)
    action_open.connect("activate", lambda a, p: print("Open Project"))
    window.add_action(action_open)
    
    action_save = Gio.SimpleAction.new("save", None)
    action_save.connect("activate", lambda a, p: print("Save Project"))
    window.add_action(action_save)
    
    action_save_as = Gio.SimpleAction.new("save_as", None)
    action_save_as.connect("activate", lambda a, p: print("Save Project As"))
    window.add_action(action_save_as)
    
    action_export = Gio.SimpleAction.new("export", None)
    action_export.connect("activate", lambda a, p: print("Export"))
    window.add_action(action_export)
    
    action_quit = Gio.SimpleAction.new("quit", None)
    action_quit.connect("activate", lambda a, p: window.close())
    window.add_action(action_quit)
    
    # Edit actions
    action_undo = Gio.SimpleAction.new("undo", None)
    action_undo.connect("activate", lambda a, p: print("Undo"))
    window.add_action(action_undo)
    
    action_redo = Gio.SimpleAction.new("redo", None)
    action_redo.connect("activate", lambda a, p: print("Redo"))
    window.add_action(action_redo)
    
    action_cut = Gio.SimpleAction.new("cut", None)
    action_cut.connect("activate", lambda a, p: print("Cut"))
    window.add_action(action_cut)
    
    action_copy = Gio.SimpleAction.new("copy", None)
    action_copy.connect("activate", lambda a, p: print("Copy"))
    window.add_action(action_copy)
    
    action_paste = Gio.SimpleAction.new("paste", None)
    action_paste.connect("activate", lambda a, p: print("Paste"))
    window.add_action(action_paste)
    
    action_delete = Gio.SimpleAction.new("delete", None)
    action_delete.connect("activate", lambda a, p: print("Delete"))
    window.add_action(action_delete)
    
    action_select_all = Gio.SimpleAction.new("select_all", None)
    action_select_all.connect("activate", lambda a, p: print("Select All"))
    window.add_action(action_select_all)
    
    action_zoom_in = Gio.SimpleAction.new("zoom_in", None)
    action_zoom_in.connect("activate", lambda a, p: print("Zoom In"))
    window.add_action(action_zoom_in)
    
    action_zoom_out = Gio.SimpleAction.new("zoom_out", None)
    action_zoom_out.connect("activate", lambda a, p: print("Zoom Out"))
    window.add_action(action_zoom_out)
    
    action_fit_to_window = Gio.SimpleAction.new("fit_to_window", None)
    action_fit_to_window.connect("activate", lambda a, p: print("Fit to Window"))
    window.add_action(action_fit_to_window)
    
    action_grid = Gio.SimpleAction.new("grid", None)
    action_grid.connect("activate", lambda a, p: print("Show Grid"))
    window.add_action(action_grid)
    
    action_rulers = Gio.SimpleAction.new("rulers", None)
    action_rulers.connect("activate", lambda a, p: print("Show Rulers"))
    window.add_action(action_rulers)
    
    action_insert_laser = Gio.SimpleAction.new("insert_laser", None)
    action_insert_laser.connect("activate", lambda a, p: print("Insert Laser"))
    window.add_action(action_insert_laser)
    
    action_insert_modulator = Gio.SimpleAction.new("insert_modulator", None)
    action_insert_modulator.connect("activate", lambda a, p: print("Insert Modulator"))
    window.add_action(action_insert_modulator)
    
    action_insert_fiber = Gio.SimpleAction.new("insert_fiber", None)
    action_insert_fiber.connect("activate", lambda a, p: print("Insert Fiber"))
    window.add_action(action_insert_fiber)
    
    action_insert_detector = Gio.SimpleAction.new("insert_detector", None)
    action_insert_detector.connect("activate", lambda a, p: print("Insert Detector"))
    window.add_action(action_insert_detector)
    
    action_insert_amplifier = Gio.SimpleAction.new("insert_amplifier", None)
    action_insert_amplifier.connect("activate", lambda a, p: print("Insert Amplifier"))
    window.add_action(action_insert_amplifier)
    
    action_insert_filter = Gio.SimpleAction.new("insert_filter", None)
    action_insert_filter.connect("activate", lambda a, p: print("Insert Filter"))
    window.add_action(action_insert_filter)
    
    action_properties = Gio.SimpleAction.new("properties", None)
    action_properties.connect("activate", lambda a, p: print("Properties"))
    window.add_action(action_properties)
    
    action_script_editor = Gio.SimpleAction.new("script_editor", None)
    action_script_editor.connect("activate", lambda a, p: print("Script Editor"))
    window.add_action(action_script_editor)
    
    action_component_library = Gio.SimpleAction.new("component_library", None)
    action_component_library.connect("activate", lambda a, p: print("Component Library"))
    window.add_action(action_component_library)
    
    action_preferences = Gio.SimpleAction.new("preferences", None)
    action_preferences.connect("activate", lambda a, p: print("Preferences"))
    window.add_action(action_preferences)
    
    action_run_simulation = Gio.SimpleAction.new("run_simulation", None)
    action_run_simulation.connect("activate", lambda a, p: print("Run Simulation"))
    window.add_action(action_run_simulation)
    
    action_stop_simulation = Gio.SimpleAction.new("stop_simulation", None)
    action_stop_simulation.connect("activate", lambda a, p: print("Stop Simulation"))
    window.add_action(action_stop_simulation)
    
    action_simulation_parameters = Gio.SimpleAction.new("simulation_parameters", None)
    action_simulation_parameters.connect("activate", lambda a, p: print("Simulation Parameters"))
    window.add_action(action_simulation_parameters)
    
    action_monitor_simulation = Gio.SimpleAction.new("monitor_simulation", None)
    action_monitor_simulation.connect("activate", lambda a, p: print("Monitor Simulation"))
    window.add_action(action_monitor_simulation)
    
    action_view_results = Gio.SimpleAction.new("view_results", None)
    action_view_results.connect("activate", lambda a, p: print("View Results"))
    window.add_action(action_view_results)
    
    action_export_results = Gio.SimpleAction.new("export_results", None)
    action_export_results.connect("activate", lambda a, p: print("Export Results"))
    window.add_action(action_export_results)
    
    action_plot_eye_diagram = Gio.SimpleAction.new("plot_eye_diagram", None)
    action_plot_eye_diagram.connect("activate", lambda a, p: print("Plot Eye Diagram"))
    window.add_action(action_plot_eye_diagram)
    
    action_plot_spectrum = Gio.SimpleAction.new("plot_spectrum", None)
    action_plot_spectrum.connect("activate", lambda a, p: print("Plot Spectrum"))
    window.add_action(action_plot_spectrum)
    
    action_plot_ber = Gio.SimpleAction.new("plot_ber", None)
    action_plot_ber.connect("activate", lambda a, p: print("Plot BER"))
    window.add_action(action_plot_ber)
    
    action_about = Gio.SimpleAction.new("about", None)
    action_about.connect("activate", show_about_dialog)
    window.add_action(action_about)
    
    action_help = Gio.SimpleAction.new("help", None)
    action_help.connect("activate", lambda a, p: print("Help"))
    window.add_action(action_help)
    
    action_examples = Gio.SimpleAction.new("examples", None)
    action_examples.connect("activate", lambda a, p: print("Examples"))
    window.add_action(action_examples)

    file_menu = Gio.Menu.new()
    file_menu.append("_New Project", "win.new")
    file_menu.append("_Open Project...", "win.open")
    file_menu.append("_Save", "win.save")
    file_menu.append("Save _As...", "win.save_as")
    
    export_section = Gio.Menu.new()
    export_section.append("_Export...", "win.export")
    file_menu.append_section(None, export_section)
    
    quit_section = Gio.Menu.new()
    quit_section.append("_Quit", "win.quit")
    file_menu.append_section(None, quit_section)

    edit_menu = Gio.Menu.new()
    edit_menu.append("_Undo", "win.undo")
    edit_menu.append("_Redo", "win.redo")
    
    edit_ops_section = Gio.Menu.new()
    edit_ops_section.append("Cu_t", "win.cut")
    edit_ops_section.append("_Copy", "win.copy")
    edit_ops_section.append("_Paste", "win.paste")
    edit_ops_section.append("_Delete", "win.delete")
    edit_menu.append_section(None, edit_ops_section)
    
    selection_section = Gio.Menu.new()
    selection_section.append("Select _All", "win.select_all")
    edit_menu.append_section(None, selection_section)

    view_menu = Gio.Menu.new()
    view_menu.append("_Zoom In", "win.zoom_in")
    view_menu.append("_Zoom Out", "win.zoom_out")
    view_menu.append("_Fit to Window", "win.fit_to_window")
    
    display_section = Gio.Menu.new()
    display_section.append("Show _Grid", "win.grid")
    display_section.append("Show _Rulers", "win.rulers")
    view_menu.append_section(None, display_section)

    insert_menu = Gio.Menu.new()
    insert_menu.append("_Laser", "win.insert_laser")
    insert_menu.append("_Modulator", "win.insert_modulator")
    insert_menu.append("_Fiber", "win.insert_fiber")
    insert_menu.append("_Detector", "win.insert_detector")
    insert_menu.append("_Amplifier", "win.insert_amplifier")
    insert_menu.append("_Filter", "win.insert_filter")

    tools_menu = Gio.Menu.new()
    tools_menu.append("_Properties", "win.properties")
    tools_menu.append("_Script Editor", "win.script_editor")
    tools_menu.append("_Component Library", "win.component_library")
    
    settings_section = Gio.Menu.new()
    settings_section.append("_Preferences", "win.preferences")
    tools_menu.append_section(None, settings_section)

    simulation_menu = Gio.Menu.new()
    simulation_menu.append("_Run Simulation", "win.run_simulation")
    simulation_menu.append("_Stop Simulation", "win.stop_simulation")
    
    config_section = Gio.Menu.new()
    config_section.append("Simulation _Parameters", "win.simulation_parameters")
    config_section.append("_Monitor Simulation", "win.monitor_simulation")
    simulation_menu.append_section(None, config_section)

    results_menu = Gio.Menu.new()
    results_menu.append("_View Results", "win.view_results")
    results_menu.append("_Export Results", "win.export_results")
    
    plotting_section = Gio.Menu.new()
    plotting_section.append("Plot _Eye Diagram", "win.plot_eye_diagram")
    plotting_section.append("Plot _Spectrum", "win.plot_spectrum")
    plotting_section.append("Plot _BER", "win.plot_ber")
    results_menu.append_section(None, plotting_section)

    help_menu = Gio.Menu.new()
    help_menu.append("_Help", "win.help")
    help_menu.append("_Examples", "win.examples")
    
    about_section = Gio.Menu.new()
    about_section.append("_About OpenOpti", "win.about")
    help_menu.append_section(None, about_section)

    menu_model = Gio.Menu.new()
    menu_model.append_submenu("_File", file_menu)
    menu_model.append_submenu("_Edit", edit_menu)
    menu_model.append_submenu("_View", view_menu)
    menu_model.append_submenu("_Insert", insert_menu)
    menu_model.append_submenu("_Tools", tools_menu)
    menu_model.append_submenu("_Simulation", simulation_menu)
    menu_model.append_submenu("_Results", results_menu)
    menu_model.append_submenu("_Help", help_menu)

    menubar = Gtk.PopoverMenuBar.new_from_model(menu_model)
    return menubar

def show_about_dialog(action, param):
    """Callback to show a simple About dialog."""
    dialog = Gtk.AboutDialog()
    dialog.set_program_name("OpenOpti")
    dialog.set_version("0.1.0")
    dialog.set_comments("An open-source optical system simulator")
    dialog.set_website("https://github.com/qxrein/openopti") 
    
    try:
        import os
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets", "OS.png")
        if os.path.exists(icon_path):
            icon = Gtk.Image.new_from_file(icon_path)
            dialog.set_logo(icon.get_paintable())
        else:
            dialog.set_logo_icon_name("applications-science")
    except Exception as e:
        print(f"Warning: Could not load custom icon: {e}")
        dialog.set_logo_icon_name("applications-science")
    
    dialog.show()
