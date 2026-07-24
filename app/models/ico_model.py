import json
from pathlib import Path
from PySide6.QtGui import QIcon

Path_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # ReadItLoud/
CONFIG_FILE = Path_PROJECT_ROOT / "config" / "themes" / "ico_theme_config.json"

class IconManager:
    """Model: Manages icon state and theme data"""
    
    def __init__(self):
        self._is_dark = False
        
        self._icons = {
            "delete": {  
                "modern_light": "config/white-icons/trash.svg",
                "modern_dark": "config/black-icons/trash.svg"
            },
            "copy": {
                "modern_light": "config/white-icons/copy.svg",
                "modern_dark": "config/black-icons/copy.svg"
            },
            "cut": {
                "modern_light": "config/white-icons/cut.svg",
                "modern_dark": "config/black-icons/cut.svg"
            },
            "paste": {
                "modern_light": "config/white-icons/paste.svg",
                "modern_dark": "config/black-icons/paste.svg"
            },
            "undo": { 
                "modern_light": "config/white-icons/undo.png",
                "modern_dark": "config/black-icons/undo.png"
            },
            "redo": {  
                "modern_light": "config/white-icons/redo.png",
                "modern_dark": "config/black-icons/redo.png"
            },
            "export": {  
                "modern_light": "config/white-icons/export.svg",
                "modern_dark": "config/black-icons/export.svg"
            },
            "clear": {  
                "modern_light": "config/white-icons/clear.svg",
                "modern_dark": "config/black-icons/clear.svg"
            },
            "read": {  
                "modern_light": "config/white-icons/read.png",
                "modern_dark": "config/black-icons/read.png"
            },
            "qualify": {  #
                "modern_light": "config/white-icons/practice.png",
                "modern_dark": "config/black-icons/practice.png"
            },
            "translate": {  
                "modern_light": "config/white-icons/translate.svg",
                "modern_dark": "config/black-icons/translate.svg"
            },
            "transcribe": {  
                "modern_light": "config/white-icons/caption.svg",
                "modern_dark": "config/black-icons/caption.svg"
            },
            "play": {
                "modern_light": "config/white-icons/play.svg",
                "modern_dark": "config/black-icons/play.svg"
            },
            "stop": {
                "modern_light": "config/white-icons/stop.svg",
                "modern_dark": "config/black-icons/stop.svg"
            },
            "settings": {
                "modern_light": "config/white-icons/settings.svg",
                "modern_dark": "config/black-icons/settings.svg"
            },
            "check_grammar": {
                "modern_light": "config/white-icons/grammar.png",
                "modern_dark": "config/black-icons/grammar.png"
            },
            "theme": {
                "modern_light": "config/white-icons/sun.svg",
                "modern_dark": "config/black-icons/moon.svg"
            },
            "open_book": {#
                "modern_light": "config/white-icons/open_book.svg",
                "modern_dark": "config/black-icons/open_book.svg"
            },
            "upload": {
                "modern_light": "config/white-icons/import.svg",
                "modern_dark": "config/black-icons/import.svg"
            },
            "reload_audio": {
                "modern_light": "config/white-icons/reload.svg",
                "modern_dark": "config/black-icons/reload.svg"
            },
            "rename": {#
                "modern_light": "config/white-icons/rename.png",
                "modern_dark": "config/black-icons/rename.png"
            },
            "record_pause": {
                "modern_light": "config/white-icons/record.svg",
                "modern_dark": "config/black-icons/record.svg"
            },
            "about_engine": {
                "modern_light": "config/white-icons/about.svg",
                "modern_dark": "config/black-icons/about.svg"
            },
            "stop_record": {
                "modern_light": "config/white-icons/stop.svg",
                "modern_dark": "config/black-icons/stop.svg"
            },
            "save": {#
                "modern_light": "config/white-icons/save.svg",
                "modern_dark": "config/black-icons/save.svg"
            },
            "playlist": {
                "modern_light": "config/white-icons/playlist.svg",
                "modern_dark": "config/black-icons/playlist.svg"
            },
            "audio_preview": {
                "modern_light": "config/white-icons/preview.png",
                "modern_dark": "config/black-icons/preview.png"
            },
            "engine_section": {
                "modern_light": "config/white-icons/paste.svg",
                "modern_dark": "config/black-icons/paste.svg"
            },
            "feedback_section": {
                "modern_light": "config/white-icons/paste.svg",
                "modern_dark": "config/black-icons/paste.svg"
            },
            "translation_section": {
                "modern_light": "config/white-icons/paste.svg",
                "modern_dark": "config/black-icons/paste.svg"
            }
        }
        
        # Restore saved theme on startup
        self.load_theme()
    
    def toggle_theme(self) -> bool:
        """Toggle theme and return new state"""
        self._is_dark = not self._is_dark
        return self._is_dark
    
    def set_theme(self, is_dark: bool):
        """Set theme directly (used when loading saved state)"""
        self._is_dark = is_dark
    
    @property
    def is_dark(self) -> bool:
        return self._is_dark

    def get_icon(self, name: str) -> QIcon:
        """Get icon based on current theme"""
        theme = "modern_light" if self._is_dark else "modern_dark"
        
        icon_data = self._icons.get(name)
        
        # Check if the icon exists at all
        if not icon_data:
            print(f"Warning: Icon name '{name}' not found in _icons dictionary.")
            return QIcon()
            
        # If icon_data is a dictionary, safely look for the theme
        if isinstance(icon_data, dict):
            # Try the expected key first
            if theme in icon_data:
                return QIcon(icon_data[theme])
                
            # FALLBACK: If the keys are named differently (e.g., "light_path", "path_light")
            print(f"Warning: Expected key '{theme}' not found for '{name}'. Available keys: {list(icon_data.keys())}")
            
            # Try to find a key that starts with the theme name
            for key, value in icon_data.items():
                if key.startswith(theme):
                    return QIcon(value)
                    
            return QIcon() # Return empty icon if nothing matches
            
        # If icon_data is already a string path, just use it
        elif isinstance(icon_data, str):
            return QIcon(icon_data)
            
        return QIcon()
    
    def get_icon_names(self) -> list:
        """Return all available icon names"""
        return list(self._icons.keys())
    
    def save_theme(self):
        """Persist current theme to external JSON file"""
        data = {"is_dark": self._is_dark}
        
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(data, f, indent=4)
        except (IOError, OSError) as e:
            print(f"Warning: Could not save theme - {e}")
    
    def load_theme(self):
        """Load theme from external JSON file"""
        if not CONFIG_FILE.exists():
            return
        
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                self._is_dark = data.get("is_dark", False)
        except (json.JSONDecodeError, IOError, OSError) as e:
            print(f"Warning: Could not load theme - {e}")
