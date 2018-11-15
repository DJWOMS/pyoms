# coding=utf-8
__pragma__ ('alias', 'S', '$')

class Inner:
    """Вставка в html"""
    # def __init__(self, tag, value):
    #     element = document.getElementById(tag)
    #     element.innerHTML = value
    @classmethod
    def set(cls, tag, value):
        """Вставка html по id элемента"""
        element = document.getElementById(tag)
        element.innerHTML = value

    def render(self, tag, value):
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
        S(tag).render(value)

    def style(self, tag, option, vaule):
        """Изменение style елемента"""
        S(tag).css(option, vaule)

    def value(self, tag):
        """Получение value"""
        val = S(tag).value()
        return val