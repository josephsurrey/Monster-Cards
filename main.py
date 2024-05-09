from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    """
    New instance of MainWindow class.
    Class to hold the main window of the program, which includes the search bar,
    QScrollArea which holds the cards, and the select, delete, add, and print buttons.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        # Loads the .ui file for the main window
        loadUi("mainwindow.ui", self)

