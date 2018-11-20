# coding=utf-8
__pragma__ ('alias', 'S', '$')

class Show:
    """Скрыть или показать элементы на странице"""

    def __init__(self, tag):
        self.tag = tag

    def show_hide(self):
        """Отображает или скрывает"""
        x = document.getElementById(self.tag)
        if x.style.display == "none":
            x.style.display = "block"
        else:
            x.style.display = "none"

    def show(self):
        """Показывает"""
        # x = document.getElementById(id)
        # x.style.display = "block"
        S(self.tag).show()

    def hide(self):
        """Скрывает элемент"""
        S(self.tag).hide()
        # x = document.getElementById(id)
        # x.style.display = "none"