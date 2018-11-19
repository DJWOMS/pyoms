# coding=utf-8
from components import menu
from core.inner import Inner
from .home import Posts

class Menu(menu.Menu):
    """Компонент навигации по сайту"""
    def __init__(self):
        self.tag = '.content'
        self.nav = {
            'home': './home.html',
            "search": './search.html'
        }

    def component(self):
        if self.name == "home":
            Posts().created()

app = Menu()