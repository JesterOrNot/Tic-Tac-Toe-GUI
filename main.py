from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 3
        self.playerOnesTurn = True
        areaOne = Button(text='-', font_size=50)
        areaOne.bind(on_press=self.updateStuff)
        areaTwo = Button(text='-', font_size=50)
        areaTwo.bind(on_press=self.updateStuff)
        areaThree = Button(text='-', font_size=50)
        areaThree.bind(on_press=self.updateStuff)
        areaFour = Button(text='-', font_size=50)
        areaFour.bind(on_press=self.updateStuff)
        areaFive = Button(text='-', font_size=50)
        areaFive.bind(on_press=self.updateStuff)
        areaSix = Button(text='-', font_size=50)
        areaSix.bind(on_press=self.updateStuff)
        areaSeven = Button(text='-', font_size=50)
        areaSeven.bind(on_press=self.updateStuff)
        areaEight = Button(text='-', font_size=50)
        areaEight.bind(on_press=self.updateStuff)
        areaNine = Button(text='-', font_size=50)
        areaNine.bind(on_press=self.updateStuff)
        print(areaNine.text)
        self.add_widget(areaOne)
        self.add_widget(areaTwo)
        self.add_widget(areaThree)
        self.add_widget(areaFour)
        self.add_widget(areaFive)
        self.add_widget(areaSix)
        self.add_widget(areaSeven)
        self.add_widget(areaEight)
        self.add_widget(areaNine)

    def updateStuff(self, instance):
        if self.playerOnesTurn:
            if instance.text == '-':
                instance.text = 'X'
                self.playerOnesTurn = False
            else:
                popup = Popup(title="", content=Label(
                    text='Spot Taken'), size_hint=(None, None), size=(100, 100))
                popup.open()
        else:
            if instance.text == '-':
                instance.text = "O"
                self.playerOnesTurn = True
            else:
                popup = Popup(title="", content=Label(
                    text='Spot Taken'), size_hint=(None, None), size=(100, 100))
                popup.open()


class TicTacToeApp(App):
    def build(self):
        root = RootWidget()
        return root


if __name__ == "__main__":
    TicTacToeApp().run()
