from browser import document, html
from browser.widgets.dialog import InfoDialog
import random
import moves2




#create empty list for previously stored divs
stored = []
vals = []

def valid_move(t1,t2):
  """This is a place holder for other code people are working 
  to see if a move is valid"""
  if t1 != t2 and t1 == "":
    return True
  else:
    return False

def action(event):
    """Moves pieces based on a click if moves are valid."""
    #use global variables since I'm using a stored list
    global stored
    global vals
    # The element the user clicked on is the attribute "target" of the
    # event object
    element = event.target
    print(element)
    # The text printed on the box is the element's "text" attribute
    value = element.text
    #gets the vaue of the target cell
    if len(stored) == 0:
      #if there is no value stored, the value is added 
      #to the list of stored values
      if(value)!= "":
        #print(value)
        #add value and div id to the two lists
        vals.append(element.text)
        stored.append(element)
      else:
        InfoDialog("Error", f"Nothing here to move!")
        vals = []
        stored = []
    elif checkmove (chessboard, x, y, x7, y7, piece):
      #if the move is valid, change the new cell to the
      #stored cell value and empty the old cell
      element.text = vals[0]
      stored[0].text = ""
      #clear the lists since value no longer is stored
      vals = []
      stored = []
    else:
      #prompt the user for invalid moves and clear stored values
      InfoDialog("Error", f"Invalid Move!")
      vals = []
      stored = []

# Associate function action() to the event "click" on all buttons
#if the item is in the class "divTableCell", this will bind
#it to the click event
for box in document.select("div"):
  if box.attrs['class'] == "white" or box.attrs['class']=="black":
    box.bind("click", action)