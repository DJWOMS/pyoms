from components import component
from core.inner import Inner

class Menu(component.Component):

    def __init__(self):
        """
            self.tag = '.class_tag_html'
            self.nav = {
                'home': './home.html',
                "search": './search.html'
                }
            self.name = key dict self.nav
        """
        self.tag = ''
        self.nav = {}
        self.name = ''

    def go(self, name):
        """Загружает в нужный элемент html из self.nav"""
        Inner(self.tag).html(Inner(self.tag).page(self.nav.get(name)))
        self.name = name
        self.component()

    def component(self):
        pass