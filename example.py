import sys
import pygments

from pathlib import Path

from syntaxedit.core import SyntaxEdit;

from qtpy.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QWidget
)

from qtpy.QtWidgets import QApplication

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        contents = Path(__file__).read_text()

        self.editor = SyntaxEdit(contents, language = "Python")
        self.editor.textChanged.connect(self.editor_changed)

        style_language = QHBoxLayout()
        style_language.setContentsMargins(0, 0, 0, 0)

        self.lexers = QComboBox()
        self.lexers.setEditable(False)
        self.lexers.addItems([i[0] for i in pygments.lexers.get_all_lexers()])
        self.lexers.setCurrentText(self.editor.language())
        self.lexers.currentIndexChanged.connect(self.language_changed)

        self.styles = QComboBox()
        self.styles.setEditable(False)
        self.styles.addItems(pygments.styles.get_all_styles())
        self.styles.setCurrentText(self.editor.style())
        self.styles.currentIndexChanged.connect(self.style_changed)

        style_language.addWidget(self.lexers)
        style_language.addWidget(self.styles)

        style_languagewidget = QWidget()
        style_languagewidget.setLayout(style_language)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(style_languagewidget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def language_changed(self):
        self.editor.setLanguage(self.lexers.currentText())
        print("Language changed")

    def style_changed(self):
        self.editor.setStyle(self.styles.currentText())
        print("Style changed")

    def editor_changed(self):
        print("editor changed")
        print(self.editor.toPlainText())

window = MainWindow()
window.show()
app.exec()
