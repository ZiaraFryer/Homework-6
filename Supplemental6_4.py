# Supplemental Chapter 6 - Problem 4
# Requires graphics.py from class.
from graphics import *


def buttonClicked(point):
    x = point.getX()
    y = point.getY()

    if 100 <= x <= 300 and 150 <= y <= 250:
        return True
    else:
        return False


def main():
    win = GraphWin("Button Click", 400, 400)

    button = Rectangle(Point(100, 150), Point(300, 250))
    button.setFill("lightblue")
    button.draw(win)

    label = Text(Point(200, 200), "Click Here")
    label.draw(win)

    message = Text(Point(200, 300), "")
    message.draw(win)

    for i in range(10):
        click = win.getMouse()

        if buttonClicked(click):
            message.setText("Button was clicked!")
        else:
            message.setText("Button was not clicked!")

    win.getMouse()
    win.close()


main()
