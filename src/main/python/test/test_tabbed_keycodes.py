import sys
import unittest
from pathlib import Path

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication

sys.path.append(str(Path(__file__).resolve().parents[1]))

from editor.keymap_editor import KeymapEditor
from editor.layout_editor import LayoutEditor
from tabbed_keycodes import TabbedKeycodes


app = QApplication.instance() or QApplication([])


class TestTabbedKeycodes(unittest.TestCase):

    def test_hidden_by_default(self):
        widget = TabbedKeycodes()
        self.assertTrue(widget.isHidden())

    def test_keymap_editor_does_not_attach_tabbed_keycodes_widget(self):
        editor = KeymapEditor(LayoutEditor())
        self.assertFalse(hasattr(editor, "tabbed_keycodes"))

    def test_keyboard_scale_is_saved_and_restored(self):
        settings = QSettings("Vial", "Vial")
        settings.remove("keymap_scale")

        editor = KeymapEditor(LayoutEditor())
        editor.container.set_scale(1.35)
        editor.save_scale()

        restored_editor = KeymapEditor(LayoutEditor())
        self.assertAlmostEqual(restored_editor.container.get_scale(), 1.35)

        settings.remove("keymap_scale")
