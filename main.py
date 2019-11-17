from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 3
        self.playerOnesTurn = True
        self.one = "-"
        self.two = "-"
        self.three = "-"
        self.four = "-"
        self.five = "-"
        self.six = "-"
        self.seven = "-"
        self.eight = "-"
        self.nine = "-"
        areaOne = Button(text=str(self.one))
        areaOne.bind(on_press=self.updateStuff)
        areaTwo = Button(text=str(self.two))
        areaTwo.bind(on_press=self.updateStuff)
        areaThree = Button(text=str(self.three))
        areaThree.bind(on_press=self.updateStuff)
        areaFour = Button(text=str(self.four))
        areaFour.bind(on_press=self.updateStuff)
        areaFive = Button(text=str(self.five))
        areaFive.bind(on_press=self.updateStuff)
        areaSix = Button(text=str(self.six))
        areaSix.bind(on_press=self.updateStuff)
        areaSeven = Button(text=str(self.seven))
        areaSeven.bind(on_press=self.updateStuff)
        areaEight = Button(text=str(self.eight))
        areaEight.bind(on_press=self.updateStuff)
        areaNine = Button(text=str(self.nine))
        areaNine.bind(on_press=self.updateStuff)
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
            if instance.text == str('-'):
                instance.text = str('X')
                self.playerOnesTurn = False
        else:
            if instance.text == str('-'):
                instance.text = str("O")
                self.playerOnesTurn = True


class MyApp(App):
    def build(self):
        root = RootWidget()
        return root


if __name__ == "__main__":
    MyApp().run()
