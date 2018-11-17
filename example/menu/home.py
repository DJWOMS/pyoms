# coding=utf-8
from components.component import Component
from core.inner import Inner
from core.ajax import Ajax

class Posts(Component):
    """Компонент новостей"""
    def created(self):
        self.news = [{'title': 'Первая новость', 'text': 'Текст для первой тестовой ''новости'},
                     {'title': 'Вторая новость', 'text': 'Текст для второй текстовой новости'}]
        print(self.news)
        p = Inner('.text').value()
        print(p)
        Inner('.block-news').render(self, self.news)

# news = Posts()