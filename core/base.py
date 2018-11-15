# coding=utf-8
a = require('../static/lib/jquery.js')
class Base:

    """Базовый класс компонента"""
    data = {}

    def __init__(self, func):
        document.addEventListener("DOMContentLoaded", self.created)

    def created(self):
        """Работает при открытии страницы"""
        pass

    def get_data(self):
        """Получить data"""
        return self.data