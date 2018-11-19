# coding=utf-8

class Onload:
    """Загрузка страницы"""
    def __init__(self, func):
        document.addEventListener("DOMContentLoaded", func) #self.load)

    def load(self):
        pass