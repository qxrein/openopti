import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gsk, Graphene
import math

class DesignCanvas(Gtk.DrawingArea):
    """A blank canvas for designing optical circuit diagrams."""
    
    def __init__(self):
        super().__init__()
        
        self.zoom_level = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self.grid_size = 20
        self.show_grid = True
        self.snap_to_grid = True
        
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        
        self.components = []
        
        self.set_draw_func(self.on_draw)
        self.set_size_request(800, 600)
        
        click_controller = Gtk.GestureClick()
        click_controller.connect("pressed", self.on_button_press)
        click_controller.connect("released", self.on_button_release)
        self.add_controller(click_controller)
        
        motion_controller = Gtk.EventControllerMotion()
        motion_controller.connect("motion", self.on_motion_notify)
        self.add_controller(motion_controller)
        
        scroll_controller = Gtk.EventControllerScroll()
        scroll_controller.connect("scroll", self.on_scroll)
        self.add_controller(scroll_controller)
        
        self.add_css_class("design-canvas")
    
    def on_draw(self, area, cr, width, height):
        """Handle drawing of the canvas."""
        cr.set_source_rgb(1, 1, 1)  
        cr.paint()
        
        cr.translate(self.pan_x, self.pan_y)
        cr.scale(self.zoom_level, self.zoom_level)
        
        if self.show_grid:
            self.draw_grid(cr, width, height)
        
        self.draw_components(cr)
        
        if self.is_dragging:
            self.draw_selection_rectangle(cr)
    
    def draw_grid(self, cr, width, height):
        """Draw the grid pattern."""
        start_x = math.floor(-self.pan_x / self.zoom_level / self.grid_size) * self.grid_size
        start_y = math.floor(-self.pan_y / self.zoom_level / self.grid_size) * self.grid_size
        end_x = start_x + (width / self.zoom_level) + self.grid_size * 2
        end_y = start_y + (height / self.zoom_level) + self.grid_size * 2
        
        cr.set_source_rgba(0.8, 0.8, 0.8, 0.5)  
        cr.set_line_width(0.5)
        
        x = start_x
        while x <= end_x:
            cr.move_to(x, start_y)
            cr.line_to(x, end_y)
            x += self.grid_size
        cr.stroke()
        
        y = start_y
        while y <= end_y:
            cr.move_to(start_x, y)
            cr.line_to(end_x, y)
            y += self.grid_size
        cr.stroke()
    
    def draw_components(self, cr):
        """Draw components on the canvas (placeholder)."""
        pass
    
    def draw_selection_rectangle(self, cr):
        """Draw selection rectangle during drag operations."""
        if not self.is_dragging:
            return
        
        start_x = min(self.drag_start_x, self.last_mouse_x)
        start_y = min(self.drag_start_y, self.last_mouse_y)
        end_x = max(self.drag_start_x, self.last_mouse_x)
        end_y = max(self.drag_start_y, self.last_mouse_y)
        
        cr.set_source_rgba(0.2, 0.6, 1.0, 0.3) 
        cr.set_line_width(1.0)
        cr.rectangle(start_x, start_y, end_x - start_x, end_y - start_y)
        cr.fill_preserve()
        
        cr.set_source_rgba(0.2, 0.6, 1.0, 0.8) 
        cr.stroke()
    
    def on_button_press(self, gesture, n_press, x, y):
        """Handle mouse button press events."""
        button = gesture.get_current_button()
        
        if button == 1:  
            self.is_dragging = True
            self.drag_start_x = (x - self.pan_x) / self.zoom_level
            self.drag_start_y = (y - self.pan_y) / self.zoom_level
            self.last_mouse_x = self.drag_start_x
            self.last_mouse_y = self.drag_start_y
            
            self.grab_focus()
        
        elif button == 2: 
            self.is_dragging = True
            self.drag_start_x = (x - self.pan_x) / self.zoom_level
            self.drag_start_y = (y - self.pan_y) / self.zoom_level
            self.last_mouse_x = self.drag_start_x
            self.last_mouse_y = self.drag_start_y
    
    def on_button_release(self, gesture, n_press, x, y):
        """Handle mouse button release events."""
        self.is_dragging = False
    
    def on_motion_notify(self, controller, x, y):
        """Handle mouse motion events."""
        if self.is_dragging:
            new_pan_x = x - self.drag_start_x * self.zoom_level
            new_pan_y = y - self.drag_start_y * self.zoom_level
            
            self.pan_x = new_pan_x
            self.pan_y = new_pan_y
            
            self.last_mouse_x = (x - self.pan_x) / self.zoom_level
            self.last_mouse_y = (y - self.pan_y) / self.zoom_level
            
            self.queue_draw()
    
    def on_scroll(self, controller, x, y, dx, dy):
        """Handle scroll events for zooming."""

        if dx != 0: 
            self.pan_x -= dx * 10
            self.queue_draw()
        elif dy != 0:  
            self.pan_y -= dy * 10
            self.queue_draw()
    
    def zoom_in(self):
        """Zoom in by a fixed amount."""
        self.zoom_level = min(5.0, self.zoom_level * 1.2)
        self.queue_draw()
    
    def zoom_out(self):
        """Zoom out by a fixed amount."""
        self.zoom_level = max(0.1, self.zoom_level / 1.2)
        self.queue_draw()
    
    def zoom_fit(self):
        """Zoom to fit all content in view."""
        self.zoom_level = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self.queue_draw()
    
    def toggle_grid(self):
        """Toggle grid visibility."""
        self.show_grid = not self.show_grid
        self.queue_draw()
    
    def set_grid_size(self, size):
        """Set grid size in pixels."""
        self.grid_size = max(5, min(100, size))
        self.queue_draw()
    
    def snap_to_grid_coordinate(self, x, y):
        """Snap coordinates to grid if enabled."""
        if not self.snap_to_grid:
            return x, y
        
        snapped_x = round(x / self.grid_size) * self.grid_size
        snapped_y = round(y / self.grid_size) * self.grid_size
        return snapped_x, snapped_y
    
    def get_canvas_coordinates(self, screen_x, screen_y):
        """Convert screen coordinates to canvas coordinates."""
        canvas_x = (screen_x - self.pan_x) / self.zoom_level
        canvas_y = (screen_y - self.pan_y) / self.zoom_level
        return canvas_x, canvas_y
    
    def get_screen_coordinates(self, canvas_x, canvas_y):
        """Convert canvas coordinates to screen coordinates."""
        screen_x = canvas_x * self.zoom_level + self.pan_x
        screen_y = canvas_y * self.zoom_level + self.pan_y
        return screen_x, screen_y
