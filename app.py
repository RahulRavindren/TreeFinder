from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.camera import *
class CameraWidget(Camera,Widget):
    def onpress(self,Object):
        camp.play = true



class FindTree(App,Camera):
        def build(self):
            cambtn = Button(text='click')
     #       cambtn.bind(on_press=CameraWidget.onpress(cam))

            camwidget = Widget()
            cam = Camera(resolution=(640,480) ,size=(500,500))
            cam.play = True
            camwidget.add_widget(cam)
            return camwidget




if __name__ == '__main__':
    FindTree().run()
