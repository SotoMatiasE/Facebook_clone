from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.app import StringProperty


class StoryWidget(MDRelativeLayout):
    name = StringProperty()
    avatar = StringProperty()
    image = StringProperty()