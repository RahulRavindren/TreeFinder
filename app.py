from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.camera import *
from kivy.uix.modalview import *

# class CameraWidget(Camera,Widget):
#     def onpress(self,object):

class FindTree(App):

    def display(self,instance):
        x = instance
        cam = Camera(play=True)
        x.add_widget(cam)


    def build(self):
        camwidget = Widget()
        cambtn=Button(text='click',size_hint=(0.1,0.1),pos_hint={'x':1,'y':1})
        camwidget.add_widget(cambtn)
        cambtn.bind(on_press=self.display)
        return camwidget


if __name__ == '__main__':
    FindTree().run()
