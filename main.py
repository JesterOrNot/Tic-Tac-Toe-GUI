from kivy.app import App
from kivy.uix.gridlayout import GridLayout
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
        areaOne.bind(on_press=self.updateOne)
        areaTwo = Button(text=str(self.two))
        areaThree = Button(text=str(self.three))
        areaFour = Button(text=str(self.four))
        areaFive = Button(text=str(self.five))
        areaSix = Button(text=str(self.six))
        areaSeven = Button(text=str(self.seven))
        areaEight = Button(text=str(self.eight))
        areaNine = Button(text=str(self.nine))
        self.add_widget(areaOne)
        self.add_widget(areaTwo)
        self.add_widget(areaThree)
        self.add_widget(areaFour)
        self.add_widget(areaFive)
        self.add_widget(areaSix)
        self.add_widget(areaSeven)
        self.add_widget(areaEight)
        self.add_widget(areaNine)

    def updateOne(self, instance):
        if self.playerOnesTurn:
            self.one = str('X')
            self.playerOnesTurn = False
        else:
            self.one = str("O")
            self.playerOnesTurn = True
        print(self.one)


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MyApp().run()
