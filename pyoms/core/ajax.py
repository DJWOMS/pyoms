# coding=utf-8
class Ajax:
    """
    Отправка ajax запросов
    """
    def __init__(self, header=False, value=False):
        self.header = header
        self.value = value

    def send(self, method, url, data='null'):
        """Отпрака ajax запроса"""
        xhr = __new__(XMLHttpRequest())
        xhr.open(method, url, False)
        if method == 'POST':
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        if self.header and self.value:
            xhr.setRequestHeader(self.header, self.value)
        xhr.send(data)
        return xhr

    def get_json(self, url, data={}):
        """GET запрос возвращает json"""
        url = "{}{}".format(url, self.format_params(data))
        xhr = self.send("GET", url)
        if xhr.status == 200 or xhr.status == 0:
            return JSON.parse(xhr.responseText)
        else:
            return xhr.responseText

    def post_json(self, url, data={}):
        """POST запрос возвращает json"""
        body = self.format_data(data)
        xhr = self.send("POST", url, body)
        if xhr.status != 200:
            return xhr.responseText
        else:
            return JSON.parse(xhr.responseText)

    def get_text(self, url, data={}):
        """GET запрос возвращает text"""
        url = "{}{}".format(url, self.format_params(data))
        xhr = self.send("GET", url)
        if xhr.readyState == 4:
            if xhr.status == 200 or xhr.status == 0:
                r = xhr.responseText
            else:
                r = xhr.responseText
        else:
            r = False
        return r

    @staticmethod
    def format_params(params):
        l = '?{}'.format('&'.join(['{}={}'.format(k, v) for k, v in params.items()]))
        return l

    @staticmethod
    def format_data(data):
        d = '{}'.format('&'.join(['{}={}'.format(k, v) for k, v in data.items()]))
        return d