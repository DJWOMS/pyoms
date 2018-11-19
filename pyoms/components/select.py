# coding=utf-8
from core.inner import Inner
from components.component import Component

class Select(Component):
    """Компонент выподающего списка"""
    data = [
        {"value": "usd"},
        {"value": "eur"},
        {"value": "btc"},
    ]

    def created(self):
        # directives = {"option": {"value": 2}}
        Inner(".balance").render(self.data)
        # Inner(".balance").set_value("1")

    @classmethod
    def change(self, value):
        """Выбор элемента списка"""
        print(value)

# app = Select()