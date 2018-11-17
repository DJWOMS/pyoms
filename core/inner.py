# coding=utf-8
__pragma__ ('alias', 'S', '$')

class Inner:
    """Вставка в html"""

    def __init__(self, tag):
        """Принемает атрибут тега"""
        self.tag = tag

    def html(self, value):
        """Вставка html в элемент"""
        S(self.tag).html(value)

    def text(self, value):
        """Вставка text в элемент"""
        S(self.tag).text(value)

    def render(self, value):
        """
        Нужно использовать словарь

        <div id="template">
          <span class="greeting"></span>
          <span data-bind="name"></span>
        </div>
        var hello = {
          greeting: 'Hello',
          name:     'world!'
        };
        Inner().render('#template', hello);

        <div id="template">
          <span class="greeting">Hello</span>
          <span data-bind="name">world!</span>
        </div>
        """
        S(self.tag).render(value)

    def style(self, option, vaule):
        """Изменение style элемента"""
        S(self.tag).css(option, vaule)

    def value(self):
        """Получение value"""
        val = S(self.tag).val()
        return val

    def set_value(self, value):
        """Установить value"""
        S(self.tag).val(value)

    def page(self, url):
        """Загрузить html"""
        return S(self.tag).load(url)
