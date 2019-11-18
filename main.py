from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button


class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 3
        self.playerOnesTurn = True
        global areaOne
        global areaTwo
        global areaThree
        global areaFour
        global areaFive
        global areaSix
        global areaSeven
        global areaEight
        global areaNine
        areaOne = Button(text='-', font_size=50)
        areaTwo = Button(text='-', font_size=50)
        areaThree = Button(text='-', font_size=50)
        areaFour = Button(text='-', font_size=50)
        areaFive = Button(text='-', font_size=50)
        areaSix = Button(text='-', font_size=50)
        areaSeven = Button(text='-', font_size=50)
        areaEight = Button(text='-', font_size=50)
        areaNine = Button(text='-', font_size=50)
        areaOne.bind(on_press=self.updateStuff)
        areaTwo.bind(on_press=self.updateStuff)
        areaThree.bind(on_press=self.updateStuff)
        areaFour.bind(on_press=self.updateStuff)
        areaFive.bind(on_press=self.updateStuff)
        areaSix.bind(on_press=self.updateStuff)
        areaSeven.bind(on_press=self.updateStuff)
        areaEight.bind(on_press=self.updateStuff)
        areaNine.bind(on_press=self.updateStuff)
        areaOne.background_normal=""
        areaTwo.background_normal=""
        areaThree.background_normal=""
        areaFour.background_normal=""
        areaFive.background_normal=""
        areaSix.background_normal=""
        areaSeven.background_normal=""
        areaEight.background_normal=""
        areaNine.background_normal=""
        self.add_widget(areaOne)
        self.add_widget(areaTwo)
        self.add_widget(areaThree)
        self.add_widget(areaFour)
        self.add_widget(areaFive)
        self.add_widget(areaSix)
        self.add_widget(areaSeven)
        self.add_widget(areaEight)
        self.add_widget(areaNine)

    def reset_board(self):
        areaOne.text = "-"
        areaTwo.text = "-"
        areaThree.text = "-"
        areaFour.text = "-"
        areaFive.text = "-"
        areaSix.text = "-"
        areaSeven.text = "-"
        areaEight.text = "-"
        areaNine.text = "-"
        areaOne.background_normal=""
        areaTwo.background_normal=""
        areaThree.background_normal=""
        areaFour.background_normal=""
        areaFive.background_normal=""
        areaSix.background_normal=""
        areaSeven.background_normal=""
        areaEight.background_normal=""
        areaNine.background_normal=""

    def updateStuff(self, instance):
        if self.playerOnesTurn:
            if instance.text == '-':
                instance.text = 'X'
                instance.font_size = 1
                instance.background_normal = "assets/X.png"
                self.playerOnesTurn = False
            else:
                popup = Popup(title="", content=Label(
                    text='Spot Taken'), size_hint=(None, None), size=(100, 100))
                popup.open()
        else:
            if instance.text == '-':
                instance.text = "O"
                instance.background_normal = "assets/O.png"
                self.playerOnesTurn = True
            else:
                popup = Popup(title="", content=Label(
                    text='Spot Taken'), size_hint=(None, None), size=(100, 100))
                popup.open()
        if (areaOne.text == "X" and areaFour.text == "X" and areaSeven.text == "X") or \
            (areaTwo.text == "X" and areaFive.text == "X" and areaEight.text == "X") or \
            (areaThree.text == "X" and areaSix.text == "X" and areaNine.text == "X") or \
            (areaOne.text == "X" and areaTwo.text == "X" and areaThree.text == "X") or \
            (areaFour.text == "X" and areaFive.text == "X" and areaSix.text == "X") or \
            (areaSeven.text == "X" and areaEight.text == "X" and areaNine.text == "X") or \
            (areaOne.text == "X" and areaFive.text == "X" and areaNine.text == "X") or \
                (areaSeven.text == "X" and areaFive.text == "X" and areaThree.text == "X"):
            self.reset_board()
            popup = Popup(title="", content=Label(text='X Wins'),
                          size_hint=(None, None), size=(100, 100))
            popup.open()
            self.playerOnesTurn = True
        elif (areaOne.text == "O" and areaFour.text == "O" and areaSeven.text == "O") or \
            (areaTwo.text == "O" and areaFive.text == "O" and areaEight.text == "O") or \
            (areaThree.text == "O" and areaSix.text == "O" and areaNine.text == "O") or \
            (areaOne.text == "O" and areaTwo.text == "O" and areaThree.text == "O") or \
            (areaFour.text == "O" and areaFive.text == "O" and areaSix.text == "O") or \
            (areaSeven.text == "O" and areaEight.text == "O" and areaNine.text == "O") or \
            (areaOne.text == "O" and areaFive.text == "O" and areaNine.text == "O") or \
                (areaSeven.text == "O" and areaFive.text == "O" and areaThree.text == "O"):
            self.reset_board()
            popup = Popup(title="", content=Label(text='O Wins'),
                          size_hint=(None, None), size=(100, 100))
            popup.open()
            self.playerOnesTurn = True
        occupiedCount = 0
        theList = [areaOne.text, areaTwo.text, areaThree.text, areaFour.text,
                   areaFive.text, areaSix.text, areaSeven.text, areaEight.text, areaNine.text]
        for i in theList:
            if i == "X" or i == "O":
                occupiedCount += 1
        if occupiedCount == 9:
            self.reset_board()
            popup = Popup(title="", content=Label(text='Draw'),
                          size_hint=(None, None), size=(100, 100))
            popup.open()
            self.playerOnesTurn = True


class TicTacToeApp(App):
    def build(self):
        root = RootWidget()
        return root


if __name__ == "__main__":
    TicTacToeApp().run()
