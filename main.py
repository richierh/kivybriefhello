
"""
My first application
"""
import sys
import os
print(sys.path)
os.environ["KIVY_GL_BACKEND"]= "angle_sdl2"
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class MyApp(App):

    def build(self):
        return Button(text='Hello world')

def main():
    # This should start and launch your app!
    ap = MyApp()
    ap.run()
main()
