import sys
import pyvisa_py
from PyQt5.QtWidgets import QApplication
from rigol_awg_gui.rigol_awg_gui import MainWindow


app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
app.exec()
