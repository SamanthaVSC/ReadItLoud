"""
ThemeModel — Manages theme state and persistence using external template files.

Responsibilities:
  - Loading theme templates from config/themes/templates/*.xml
  - Persisting the current theme choice to config/themes/default.txt
  - Toggling between the modern dark and modern light templates
  - Providing the active theme file path and metadata to the Controller
"""

from pathlib import Path

# ── Project-relative paths ──────────────────────────────────────
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # ReadItLoud/

_TEMPLATES_DIR = _PROJECT_ROOT / "config" / "themes" / "templates"
_DEFAULT_FILE = _PROJECT_ROOT / "config" / "themes" / "default.txt"
_WALLPAPERS_DIR = _PROJECT_ROOT / "config" / "wallpapers"


class ThemeModel:
    """Encapsulates theme state and configuration persistence.

    Instead of using the built-in qt_material themes (dark_teal.xml,
    light_blue.xml), this model loads custom XML template files from
    ``config/themes/templates/``.  The last selected theme is always
    persisted so the app opens with the same look the user left.

    Attributes:
        DARK_THEME:  Identifier for the modern dark template.
        LIGHT_THEME: Identifier for the modern light template.
    """

    DARK_THEME = "modern_dark"
    LIGHT_THEME = "modern_light"

    # ── Valid theme identifiers ─────────────────────────────────
    _VALID_THEMES = {DARK_THEME, LIGHT_THEME}

    def __init__(
        self,
        templates_dir: Path | str | None = None,
        config_path: Path | str | None = None,
    ) -> None:
        self._templates_dir = Path(templates_dir) if templates_dir else _TEMPLATES_DIR
        self._config_path = Path(config_path) if config_path else _DEFAULT_FILE
        self._current_theme: str = self._load_theme()

    # ── Properties ──────────────────────────────────────────────

    @property
    def current_theme(self) -> str:
        """The currently active theme identifier (e.g. 'modern_dark')."""
        return self._current_theme

    @property
    def current_theme_path(self) -> str:
        """Absolute path to the current theme's XML template file.

        This is the value that should be passed to
        ``qt_material.apply_stylesheet(theme=...)``.
        """
        return str(self._resolve_path(self._current_theme))

    @property
    def is_dark(self) -> bool:
        """True when the dark template is active."""
        return self._current_theme == self.DARK_THEME

    @property
    def invert_secondary(self) -> bool:
        """Whether ``invert_secondary=True`` should be passed to
        ``apply_stylesheet`` for the current theme.

        Light themes need secondary colours inverted so that surfaces
        look correct; dark themes do not.
        """
        return self._current_theme == self.LIGHT_THEME

    @property
    def wallpaper_path(self) -> Path:
        """Absolute path to the wallpaper image that matches the current theme.

        Returns ``config/wallpapers/night.jpeg`` for the dark theme and
        ``config/wallpapers/light.jpeg`` for the light theme.
        """
        filename = "night.jpeg" if self.is_dark else "light.jpeg"
        return _WALLPAPERS_DIR / filename

    # ── Public API ──────────────────────────────────────────────

    def toggle(self) -> tuple[str, bool]:
        """Switch between dark and light templates.

        Persists the choice and returns a tuple of:
          (theme_path: str, invert_secondary: bool)

        The caller can pass both directly to ``apply_stylesheet``::

            path, invert = model.toggle()
            apply_stylesheet(app, theme=path, invert_secondary=invert)
        """
        if self._current_theme == self.DARK_THEME:
            self._current_theme = self.LIGHT_THEME
        else:
            self._current_theme = self.DARK_THEME

        self._save_theme(self._current_theme)
        return self.current_theme_path, self.invert_secondary

    def apply_initial(self) -> tuple[str, bool]:
        """Return (theme_path, invert_secondary) for the persisted theme.

        Called once at startup so the application opens with the last
        theme the user selected.
        """
        return self.current_theme_path, self.invert_secondary

    # ── Private helpers ─────────────────────────────────────────

    def _resolve_path(self, theme_name: str) -> Path:
        """Convert a theme identifier to its absolute XML file path."""
        return self._templates_dir / f"{theme_name}.xml"

    def _load_theme(self) -> str:
        """Read the saved theme from disk.

        Falls back to ``modern_dark`` when:
          - the config file does not exist yet
          - the file is empty
          - the saved value references a template file that does not exist
        """
        try:
            theme = self._config_path.read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            return self.DARK_THEME

        if not theme or theme not in self._VALID_THEMES:
            return self.DARK_THEME

        # Verify the template file actually exists on disk
        if not self._resolve_path(theme).is_file():
            return self.DARK_THEME

        return theme

    def _save_theme(self, theme_name: str) -> None:
        """Persist the given theme identifier to disk."""
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(theme_name, encoding="utf-8")
