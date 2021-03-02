from kivy.uix.widget import Widget
from kivymd.app import MDApp
from webview import WebView
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<MyWebView>
    MDFlatButton:
        text: "Push"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press: root.Push()
""")

class MyWebView(MDScreen):
    def Push(self):
        WebView("https://www.google.com")


class MyWebApp(MDApp):
    def build(self):
        return MyWebView()


if __name__ == '__main__':
    MyWebApp().run

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
