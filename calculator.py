import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#TO SET THE SIZE OF THE APP
Window.size = (500,700)
kv = '''

<Button>
    size_hint: (0.2, 0.2)
    font_size: 32
    background_normal: ''
    background_color: (1,0,0)
<MyLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            id: input
            text: "0"
            halign: "right"
            font_size: 65
            size_hint: (1,0.15)
        
        GridLayout:
            cols: 4
            rows: 5

            Button:
                text: "%"
                on_press: root.math_sign("%")
            Button:
                text: "<--"
                on_press: root.back()
            Button:
                id: clear
                text: "C"
                on_press: root.clear()
            Button:
                text: "/"
                on_press: root.math_sign("/")
            Button:
                text: "7"
                on_press: root.button_press(7)
                # background_normal: ''
                # background_color: (1,1,0,1)
            Button:
                text: "8"
                on_press: root.button_press(8)
            Button:
                text: "9"
                on_press: root.button_press(9)
            Button:
                text: "X"
                on_press: root.math_sign("*")
            Button:
                text: "4"
                on_press: root.button_press(4)
            Button:
                text: "5"
                on_press: root.button_press(5)
            Button:
                text: "6"
                on_press: root.button_press(6)
            Button:
                text: "-"
                on_press: root.math_sign("-")
            Button:
                text: "1"
                on_press: root.button_press(1)
            Button:
                text: "2"
                on_press: root.button_press(2)
            Button:
                text: "3"
                on_press: root.button_press(3)
            Button:
                text: "+"
                on_press: root.math_sign("+")
            Button:
                text: "+/-"
                on_press: root.pos_neg()
            Button:
                text: "0"
                on_press: root.button_press(0)
            Button:
                text: "."
                on_press: root.dot()
            Button:
                text: "="
                on_press: root.equal()'''
Builder.load_string(kv)
# Builder.load_string()
#class is now inherited from widget
class MyLayout(Widget):
    def clear(self):
        self.ids.input.text = "0"
    def button_press(self, button):
        #to remove the already existing vaue i.e 0 and adding new value there
        previous = self.ids.input.text
        if "Error" in previous:
            previous = ''

        if previous =="0":
            self.ids.input.text = ''
            self.ids.input.text = f'{button}'
        else:
            self.ids.input.text = f'{previous}{button}'
    def equal(self):
        previous = self.ids.input.text
        #using evaluate funtion with error handling
        try:
            answer = eval(previous)
            self.ids.input.text = str(answer)
            
        except:
            self.ids.input.text = "Error"
        if "%" in previous:
            num_list = previous.split("%")
            for number in num_list[:-1]:
                answer = float(number)/100
                self.ids.input.text = str(answer)
        
    def math_sign(self, sign):
        previous = self.ids.input.text
        self.ids.input.text = f'{previous}{sign}'
    def dot(self):
        previous = self.ids.input.text
        num_list = previous.split("+")
        if "+" in previous and "." not in num_list[-1]:
            previous = f'{previous}.'
            self.ids.input.text = previous
        elif "." in previous:
            pass
        else:
            previous = f'{previous}.'
            self.ids.input.text = previous
    def back(self):
        previous = self.ids.input.text
        previous = previous[ : -1]
        self.ids.input.text = previous
    def pos_neg(self):
        previous = self.ids.input.text
        if "-" in previous:
            self.ids.input.text = f'{previous.replace("-", "")}'
        else:
            self.ids.input.text = f'-{previous}'


class MyCalculator(App):
    def build(self):
        return MyLayout()
if __name__=='__main__':
    MyCalculator().run()
