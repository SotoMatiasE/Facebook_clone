from msilib.schema import Property
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.app import StringProperty


class OnlineAvatarImage(MDRelativeLayout):
    avatar = StringProperty()