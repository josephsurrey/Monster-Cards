---

kanban-plugin: basic

---

## Decomposition

- [ ] Main Window
- [ ] Monster Card
- [ ] Add/edit card dialog


## Main Window - ui

- [ ] Search Box
- [ ] Scroll Area to hold Monster Card widgets
- [ ] Print, Select, Delete and Add buttons


## Main Window - functionality

- [ ] Update cards function
- [ ] Add card function
- [ ] Selection functionality
- [ ] Delete card function
- [ ] Print cards function
- [ ] Edit card function


## Main Window - functionality - Update cards

- [ ] Clear monster cards
- [ ] Calculate scroll area size
- [ ] Set details of the card
- [ ] Calculate card position
- [ ] Add monster card widget to scroll area and align


## Main Window - functionality - Add card

- [ ] Link add button to add_card function
- [ ] Open AddCardDialog
- [ ] Get card information from dialog
- [ ] Update dictionary
- [ ] Update cards


## Main Window - functionality - Select cards

- [ ] Link select button to toggle_selection_mode function
- [ ] Change button text
- [ ] Toggle selection mode
- [ ] Change selection_mode attribute for MonsterCard instnaces
- [ ] Deselect all cards if selection mode is disabled


## Main Window - functionality - Delete card

- [ ] Link delete button to delete_card function
- [ ] Iterate through all cards and check if they are selected
- [ ] If card is selected, remove from dictionary
- [ ] Update cards
- [ ] Set selection mode to false, button text to select, and set selection mode for Monster Card instances to false


## Main Window - functionality - Print cards

- [ ] Link print button to print_cards function
- [ ] Check if any cards are selected
- [ ] If some are, format all selected cards and add to print_output
- [ ] Otherwise format all cards and add to print_output
- [ ] Print print_output


## Monster Card - ui

- [ ] Label for title
- [ ] Image placeholder
- [ ] Labels for monster stats


## Monster Card - functionality

- [ ] Select card
- [ ] Edit card


## Monster Card - functionality - Select card

- [ ] On mousePressEvent check if selection mode is true
- [ ] If true and card is selected, deselect
- [ ] If true and card not selected, select


## Monster Card- functionality - Edit card

- [ ] On mouseDoublePressEvent check if selection mode is false
- [ ] If false:
- [ ] Get information of card to be edited
- [ ] Open AddCardDialog with card stats as arguments
- [ ] Get updated card information from dialog
- [ ] Update dictionary
- [ ] Update cards


## Add/edit card dialog - ui

- [ ] QLineEdit for monster name
- [ ] Spinboxes and labels for the values


## Add/edit card dialog - functionality

- [ ] Optional arguments to take default details for monster


## Advanced Functionality (only if have time)

- [ ] View cards in a list (only names, statistics can be shown in an expanded view/dialog)
- [ ] Sort function
- [ ] Use print dialogue to print to a printer
- [ ] Image in Monster Card




%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%