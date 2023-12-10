from kivy.uix.button import Button 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class MessageBox(Popup):
    def __init__(self, title, content, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.title = title
        self.content = Label(text=content)
        self.size_hint = (None, None)
        self.size = (400, 300)
        
class Calculator(App):
	def build(self):
		layout = FloatLayout()
		lin = Label(text="________________________________",font_size=45, color=(0,1,0,1))
		b1 = Button(text="1", size_hint=(None, None), size=(122, 122), font_size=75)
		b2 = Button(text="2",size_hint=(None, None),size=(122, 122), font_size=75)
		b3 = Button(text="3",size_hint=(None, None),  size=(122,122,), font_size=75)
		b4 =  Button(text="4",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b5 =  Button(text="5",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b6 =  Button(text="6",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b7 =  Button(text="7",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b8 =  Button(text="8",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b9 =  Button(text="9",size_hint=(None, None),  size=(122, 122,), font_size=75)
		b0 =  Button(text="0",size_hint=(None, None),  size=(122, 114,), font_size=75)
		dot =Button(text=".",size_hint=(None, None),  size=(122, 114), font_size=95,color=(0,1,0,1))
		plus = Button(text="+",size_hint=(None, None),  size=(122, 122,),color=(0,1,0,1),font_size=95)
		sub =  Button(text="−",size_hint=(None, None),  size=(122, 122),color=(0,1,0,1), font_size=105)
		mul =  Button(text="×",size_hint=(None, None),  size=(122, 122),color=(0,1,0,1), font_size=95)
		div =  Button(text="÷",color=(0,1,0,1),size_hint=(None, None),  size=(122, 122,), font_size=95)
		equ =  Button(text="=",background_color=(0,1,0,1),size_hint=(None, None),  size=(122, 114), font_size=95)
		clear = Button(text="C",size_hint=(None, None),  size=(122, 122),color=(1,0,0.3,1),font_size=95)
		bra1 = Button(text="(",size_hint=(None, None),  size=(122, 122), font_size=75,color=(0,1,0,1))
		bra2= Button(text=")",size_hint=(None, None),  size=(122, 122), font_size=75,color=(0,1,0,1))
		entry = TextInput(background_color=(0,0,0,1),foreground_color=(1,1,1,1),multiline=True, size_hint=(None, None), size=(729,450),font_size=100)
		self.entry = entry
		cl =  Button(text="DEL",size_hint=(None, None),  size=(75, 43,), font_size=30)
		ex = Button(text="Exit", color=(1,0,0.3,1),size_hint=(None, None), size=(122,114), font_size=50)
		b1.pos = (40, 540)
		b2.pos=(210, 540)
		b3.pos=(380, 540)
		b4.pos=(40,370)
		b5.pos=(210,370)
		b6.pos=(380,370)
		b7.pos=(40,200)
		b8.pos=(210,200)
		b9.pos=(380,200)
		b0.pos=(210,50)
		dot.pos=(380,50)
		plus.pos=(550,710)
		sub.pos=(550,540)
		mul.pos=(550,370)
		div.pos=(550,200)
		equ.pos=(550,50)
		clear.pos=(40,710)
		bra1.pos=(210,710)
		bra2.pos=(380,710)
		self.entry.pos=(10, 970)
		cl.pos=(570, 930)
		ex.pos=(40, 50)
		lin.pos=(0, 170)
		layout.add_widget(b1)
		layout.add_widget(b2)
		layout.add_widget(b3)
		layout.add_widget(b4)
		layout.add_widget(b5)
		layout.add_widget(b6)
		layout.add_widget(b7)
		layout.add_widget(b8)
		layout.add_widget(b9)
		layout.add_widget(b0)
		layout.add_widget(dot)
		layout.add_widget(plus)
		layout.add_widget(div)
		layout.add_widget(mul)
		layout.add_widget(sub)
		layout.add_widget(equ)
		layout.add_widget(clear)
		layout.add_widget(bra1)
		layout.add_widget(bra2)
		layout.add_widget(self.entry)
		layout.add_widget(cl)
		layout.add_widget(ex)
		layout.add_widget(lin) 
		b1.bind(on_press=self.calculate)
		b2.bind(on_press=self.calculate)
		b3.bind(on_press=self.calculate)
		b4.bind(on_press=self.calculate)
		b5.bind(on_press=self.calculate)
		b6.bind(on_press=self.calculate)
		b7.bind(on_press=self.calculate)
		b8.bind(on_press=self.calculate)
		b9.bind(on_press=self.calculate)
		b0.bind(on_press=self.calculate)
		bra1.bind(on_press=self.calculate)
		bra2.bind(on_press=self.calculate)
		plus.bind(on_press=self.calculate)
		sub.bind(on_press=self.calculate)
		div.bind(on_press=self.calculate)
		mul.bind(on_press=self.calculate)
		dot.bind(on_press=self.calculate)
		clear.bind(on_release=self.calculate)
		cl.bind(on_press=self.delete)
		equ.bind(on_press=self.calculate)
		ex.bind(on_release=self.close)
		return layout 
	def close(self, instance ):
		App.get_running_app().stop()
	def delete(self, instance):
		current_text = self.entry.text
		self.entry.text = current_text[:-1]
	def show_messagebox(self, instance):
	       title = "An error occurred"
	       content = "Invalid Calculation"
	       message_box = MessageBox(title=title, content=content)
	       message_box.open()

	def calculate(self, instance):
		      try:
		          current_text = self.entry.text
		          pressed_button_text = instance.text
		          if pressed_button_text == "=":
		      	       try:
		      	       	result = str(eval(current_text))
		      	       	self.entry.text = result
		      	       except Exception as e:
		      	       		self.show_messagebox()
		          elif pressed_button_text == "C":
		      	       		 self.entry.text = ""
		          elif pressed_button_text == "×":
		      	       		self.entry.text += "*"
		          elif pressed_button_text == "÷":
		      	       		self.entry.text += "/"
		          elif pressed_button_text == "−":
		      	               self.entry.text += "-"
		          else:
		      	    self.entry.text = current_text + pressed_button_text
		      except Exception as e:
		      	self.show_messagebox(instance)

		

if __name__=="__main__":
	Calculator().run()		