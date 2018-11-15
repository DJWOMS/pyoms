# coding=utf-8
__pragma__ ('alias', 'S', '$')

class Show:
    """Скрыть или показать элементы на странице"""

    def show_hide(self, id):
        """Отображает или скрывает"""
        x = document.getElementById(id)
        if x.style.display == "none":
            x.style.display = "block"
        else:
            x.style.display = "none"

    def show(self, tag):
        """Показывает"""
        # x = document.getElementById(id)
        # x.style.display = "block"
        S(tag).show()

    def hide(self, tag):
        """Скрывает элемент"""
        S(tag).hide()
        # x = document.getElementById(id)
        # x.style.display = "none"