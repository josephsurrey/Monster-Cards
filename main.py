from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

import qdarktheme

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

    # Attribute to hold the list of selected cards
    selected_cards = []

    def __init__(self):
        super(MainWindow, self).__init__()
        # Loads the .ui file for the main window
        loadUi("mainwindow.ui", self)

        # Connects the add card button to the add_card function
        self.addButton = self.findChild(QtWidgets.QPushButton, "addButton")
        self.addButton.clicked.connect(self.add_card)

        # Variable to hold the selection mode
        self.selection_mode = False
        # Connects the select button to the toggle_selection_mode function
        self.selectButton = self.findChild(QtWidgets.QPushButton, "selectButton")
        self.selectButton.clicked.connect(self.toggle_selection_mode)

        # Connects the delete button to the delete_card function
        self.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.deleteButton.clicked.connect(self.delete_card)

        # Connects the print button to the print_cards function
        self.printButton = self.findChild(QtWidgets.QPushButton, "printButton")
        self.printButton.clicked.connect(self.print_cards)

        # Connects the search bar to the search function
        self.searchBar = self.findChild(QtWidgets.QLineEdit, "searchBar")
        self.searchBar.textChanged.connect(self.update_cards)

        # Connects the help button to the help function
        self.helpButton = self.findChild(QtWidgets.QToolButton, "helpButton")
        self.helpButton.clicked.connect(self.help)

        # Updates the cards
        self.update_cards()

    def resizeEvent(self, a0):
        """
        Function that updates the cards when the window is resized.
        """
        self.update_cards()

    def update_cards(self):
        """
        Updates the cards in the scroll area.
        """

        # Clear the scroll area
        card_layout = self.findChild(QtWidgets.QGridLayout, "scrollAreaGridLayout")
        for card in range(card_layout.count()):
            card_layout.itemAt(card).widget().hide()
            card_layout.itemAt(card).widget().deleteLater()

        # Find the size of the scroll area
        scroll_area = self.findChild(QtWidgets.QWidget, "scrollAreaWidgetContents")
        scroll_area_width = scroll_area.width()

        # Variable to keep track of the position of each card
        horizontal_grid_number = 0
        vertical_grid_number = 0
        total_width = 0

        # Adds each card to the scroll area
        for monster_name, stats in monster_cards.items():
            if self.searchBar.text().lower() in monster_name.lower():
                # Find the scroll area layout
                card_layout = self.findChild(QtWidgets.QGridLayout, "scrollAreaGridLayout")
                # Create a new instance of the card widget
                monster_card = MonsterCard(self)

                # Set the name of the card
                monster_card.findChild(QtWidgets.QLabel, "monster_name").setText(monster_name)

                # Set the stats of the card
                monster_card.findChild(QtWidgets.QLabel, "strength_stat").setText(f"Strength: {stats['Strength']}")
                monster_card.findChild(QtWidgets.QLabel, "speed_stat").setText(f"Speed: {stats['Speed']}")
                monster_card.findChild(QtWidgets.QLabel, "stealth_stat").setText(f"Stealth: {stats['Stealth']}")
                monster_card.findChild(QtWidgets.QLabel, "cunning_stat").setText(f"Cunning: {stats['Cunning']}")

                # Get the size of the card
                card_size = monster_card.sizeHint()
                total_width += card_size.width()

                # Check if the total width of the cards is greater than the scroll area
                if total_width > scroll_area_width:
                    vertical_grid_number += 1
                    horizontal_grid_number = 0
                    total_width = card_size.width()

                # Add the card to the scroll area layout
                card_layout.addWidget(monster_card, vertical_grid_number, horizontal_grid_number)
                # Align the card to the top left
                card_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

                # Increment the horizontal grid number
                horizontal_grid_number += 1

    def add_card(self):
        """
        Function to add a new card to the database.
        Opens a dialogue where the use will be prompted to enter the details of the new card.
        Adds the card to the database.
        """
        # Open the add card dialogue
        add_card_dialog = AddCardDialog()

        # Set the title of the dialog
        add_card_dialog.setWindowTitle("Add Card")

        # If the dialogue is accepted, add the card
        if add_card_dialog.exec():
            # Get the details of the new card
            monster_name = add_card_dialog.findChild(QtWidgets.QLineEdit, "monster_name_value").text()
            strength = add_card_dialog.findChild(QtWidgets.QSpinBox, "strength_stat_value").value()
            speed = add_card_dialog.findChild(QtWidgets.QSpinBox, "speed_stat_value").value()
            stealth = add_card_dialog.findChild(QtWidgets.QSpinBox, "stealth_stat_value").value()
            cunning = add_card_dialog.findChild(QtWidgets.QSpinBox, "cunning_stat_value").value()

            # Add the card to the monster_cards dictionary
            monster_cards[monster_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}

            # Update the cards
            self.update_cards()

    def toggle_selection_mode(self):
        """
        Toggles the selection mode.
        """
        # Changes the button text
        self.selectButton.setText("Select" if self.selection_mode else "Deselect")
        # Changes the selection mode
        self.selection_mode = not self.selection_mode
        # Changes the selection mode for all MonsterCard instances
        setattr(MonsterCard, "selection_mode", not MonsterCard.selection_mode)
        # Deselects all cards when the selection mode is disabled (False)
        if not self.selection_mode:
            for card in self.findChildren(MonsterCard):
                if card.selected:
                    card.selected = False
                    card.setStyleSheet("")
            # Clear the selected cards list
            self.selected_cards.clear()

    def delete_card(self):
        """
        Function to delete a card, iterating through MonsterCard children,
        removing selected cards from monster_cards, and updating the cards.
        """
        # Remove selected cards from monster_cards
        for card in self.selected_cards:
            monster_cards.pop(card)
        # Update cards list
        self.update_cards()
        # Set selection mode to False
        self.selection_mode = False
        # Change selection button text
        self.selectButton.setText("Select")
        # Changes the selection mode for all MonsterCard instances
        setattr(MonsterCard, "selection_mode", False)
        # Clear the selected cards list
        self.selected_cards.clear()

    def print_cards(self):
        """
        Function to print all selected cards.
        Gets the list of all the currently selected cards, formats them and prints them to the console.
        If no cards are selected, prints all card details to the console.
        """
        print_output = ""

        # If cards are selected, print them to the console, otherwise print all cards
        if self.selected_cards:
            for card in self.selected_cards:
                print_output += (f"--------------------------------\n"
                                 f"Monster Name: {card}\n"
                                 f"Strength: {monster_cards[card]['Strength']}\n"
                                 f"Speed: {monster_cards[card]['Speed']}\n"
                                 f"Stealth: {monster_cards[card]['Stealth']}\n"
                                 f"Cunning: {monster_cards[card]['Cunning']}\n")
        else:
            for card in monster_cards:
                print_output += (f"--------------------------------\n"
                                 f"Monster Name: {card}\n"
                                 f"Strength: {monster_cards[card]['Strength']}\n"
                                 f"Speed: {monster_cards[card]['Speed']}\n"
                                 f"Stealth: {monster_cards[card]['Stealth']}\n"
                                 f"Cunning: {monster_cards[card]['Cunning']}\n")

        print_output += "--------------------------------\n"
        # Print the print output to the console
        print(print_output)


    def help(self):
        """
        Function to open the help dialogue.
        """
        pass


class MonsterCard(QtWidgets.QWidget):
    """
    New instance of MonsterCard class.
    Class to hold the card details.
    Each MonsterCard is a QWidget, which is placed into the MainWindow's QScrollArea
    """

    # Variable to hold the selection mode
    selection_mode = False

    def __init__(self, main_window):
        super(MonsterCard, self).__init__()
        # Loads the .ui file for the monster card
        loadUi("monstercard.ui", self)

        # Variable for the selection function
        self.selected = False

        self.window = main_window

    def mousePressEvent(self, event):
        """
        If selection mode is on, toggle the selected variable.
        """
        if MonsterCard.selection_mode:
            if self.selected:
                self.selected = False
                # Set the background color of the card to show it is not selected
                self.setStyleSheet("")

                # Remove the card from the list of selected cards
                MainWindow.selected_cards.remove(self.findChild(QtWidgets.QLabel, "monster_name").text())

            else:
                self.selected = True
                # Set the background color of the card to show it is selected
                self.setStyleSheet("background-color: rgb(0, 153, 153)")

                # Add the card to the list of selected cards
                MainWindow.selected_cards.append(self.findChild(QtWidgets.QLabel, "monster_name").text())

    def mouseDoubleClickEvent(self, a0):
        """
        If card is double-clicked, run edit_card function
        """
        if not self.selection_mode:
            self.edit_card()

    def edit_card(self):
        """
        Function to edit a Monster Card.
        When a card is double-clicked, function is run.
        Add card dialogue is used to edit the details of the card.
        """

        # Get the details of the card
        monster_name = self.findChild(QtWidgets.QLabel, "monster_name").text()
        strength = monster_cards[monster_name]["Strength"]
        speed = monster_cards[monster_name]["Speed"]
        stealth = monster_cards[monster_name]["Stealth"]
        cunning = monster_cards[monster_name]["Cunning"]

        # Open the edit card dialog
        edit_card_dialog = AddCardDialog(monster_name, strength, speed, stealth, cunning)

        # Set the title of the dialog
        edit_card_dialog.setWindowTitle("Edit Card")

        if edit_card_dialog.exec():
            # Remove the old version of the card from the monster_cards dictionary
            monster_cards.pop(monster_name)
            # Get the modified details of the card
            monster_name = edit_card_dialog.findChild(QtWidgets.QLineEdit, "monster_name_value").text()
            strength = edit_card_dialog.findChild(QtWidgets.QSpinBox, "strength_stat_value").value()
            speed = edit_card_dialog.findChild(QtWidgets.QSpinBox, "speed_stat_value").value()
            stealth = edit_card_dialog.findChild(QtWidgets.QSpinBox, "stealth_stat_value").value()
            cunning = edit_card_dialog.findChild(QtWidgets.QSpinBox, "cunning_stat_value").value()

            # Edit the card in the monster_cards dictionary
            monster_cards[monster_name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}

        # Update the cards
        self.window.update_cards()


class AddCardDialog(QtWidgets.QDialog):
    """
    New instance of AddCardDialog class.
    Class to hold the add card dialog.
    Takes monster name and stats as optional parameters to be used when editing a card.
    If these are provided, the dialog is set with the values.
    """

    def __init__(self, monster_name=None, strength=None, speed=None, stealth=None, cunning=None):
        super(AddCardDialog, self).__init__()
        # Loads the .ui file for the add card dialogue
        loadUi("add_card_dialog.ui", self)

        if monster_name:
            self.findChild(QtWidgets.QLineEdit, "monster_name_value").setText(monster_name)
            self.findChild(QtWidgets.QSpinBox, "strength_stat_value").setValue(strength)
            self.findChild(QtWidgets.QSpinBox, "speed_stat_value").setValue(speed)
            self.findChild(QtWidgets.QSpinBox, "stealth_stat_value").setValue(stealth)
            self.findChild(QtWidgets.QSpinBox, "cunning_stat_value").setValue(cunning)


# Run the application
app = QtWidgets.QApplication([])
qdarktheme.setup_theme("dark")
window = MainWindow()
window.show()
window.update_cards()
app.exec()
