# coding=utf-8
class Ajax:
    """
    Отправка ajax запросов
    """
    def __init__(self, header=False, value=False):
        self.header = header
        self.value = value

    # @staticmethod
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
        url = "{}{}".format(url, self.formatParams(data))
        xhr = self.send("GET", url)
        if (xhr.status == 200 or xhr.status == 0):
            return JSON.parse(xhr.responseText)
        else:
            return xhr.responseText

    def post_json(self, url, data={}):
        """POST запрос возвращает json"""
        # print("data - {}".format(data))
        body = self.formatData(data)
        # print("body - {}".format(body))
        xhr = self.send("POST", url, body)
        if (xhr.status != 200):
            return xhr.responseText
        else:
            return JSON.parse(xhr.responseText)

    def get_text(self, url, data={}):
        """GET запрос возвращает text"""
        url = "{}{}".format(url, self.formatParams(data))
        xhr = self.send("GET", url)
        if xhr.readyState == 4:
            if xhr.status == 200 or xhr.status == 0:
                r = xhr.responseText
            else:
                r = xhr.responseText

        return r

    @staticmethod
    def formatParams(params):
        l = '?{}'.format('&'.join(['{}={}'.format(k, v) for k, v in params.items()]))
        return l

    @staticmethod
    def formatData(data):
        d = '{}'.format('&'.join(['{}={}'.format(k, v) for k, v in data.items()]))
        return d