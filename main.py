from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

monster_cards = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}


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
        self.scroll_area = self.findChild(QtWidgets.QScrollArea, "cardScrollArea")
        self.scroll_area.installEventFilter(self)

    def eventFilter(self, obj, event):
        """
        Filters out horizontal scroll events in the QScrollArea, so that it only scrolls vertically.
        """

    def update_cards(self):
        """
        Updates the cards in the scroll area.
        """
        # Varible to keep track of the position of each card
        grid_number = 0
        # Adds each card to the scroll area
        for monster_name, stats in monster_cards.items():
            # Find the scroll area layout
            card_layout = self.findChild(QtWidgets.QGridLayout, "scrollAreaGridLayout")

            # Create a new instance of the card widget
            monster_card = MonsterCard()

            # Set the name of the card and display it
            monster_card_name = monster_card.findChild(QtWidgets.QLabel, "monster_name")
            monster_card_name.setText(monster_name)

            # Set the stats of the card and display it
            monster_card_strength = monster_card.findChild(QtWidgets.QLabel, "strength_stat")
            monster_card_strength.setText(f"Strength: {stats['Strength']}")

            monster_card_speed = monster_card.findChild(QtWidgets.QLabel, "speed_stat")
            monster_card_speed.setText(f"Speed: {stats['Speed']}")

            monster_card_stealth = monster_card.findChild(QtWidgets.QLabel, "stealth_stat")
            monster_card_stealth.setText(f"Stealth: {stats['Stealth']}")

            monster_card_cunning = monster_card.findChild(QtWidgets.QLabel, "cunning_stat")
            monster_card_cunning.setText(f"Cunning: {stats['Cunning']}")

            # Add the card to the scroll area layout
            card_layout.addWidget(monster_card, 0, grid_number)
            # Align the card to the top left
            card_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            # Increment the grid number
            grid_number += 1


class MonsterCard(QtWidgets.QWidget):
    """
    New instance of MonsterCard class.
    Class to hold the card details.
    Each MonsterCard is a QWidget, which is placed into the MainWindow's QScrollArea
    """

    def __init__(self):
        super(MonsterCard, self).__init__()
        # Loads the .ui file for the monster card
        loadUi("monstercard.ui", self)


app = QtWidgets.QApplication([])
window = MainWindow()
window.update_cards()
window.show()
app.exec()
