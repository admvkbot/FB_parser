import io

import requests as requests
from PIL import Image
from lxml import html

class Parse:
    errors = []

    def __init__(self, gp_name):
        self.gp_name = gp_name

    def add_error(self, message, print_error=True, ret=None):
        """
        Add error message and ret value on error
        """
        if print_error:
            print(message)
        self.errors.append(message)
        return ret

    def has_errors(self):
        """
        Check if has errors
        """
        return len(self.errors) > 0

    def first_error(self):
        """
        Get first error or None
        """
        return self.errors[0] if self.has_errors() else None

    def query(self, url):
        """
        Загружаем страницу и распарсиваем её в XPath
        :param url:
        :return:
        :rtype: requests.Response[]
        :raises: :exc:
        """
        headers = {"Accept-Language": "de-DE,en;q=0.5",
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 Safari/537.36"}
        r = requests.get(url, headers=headers)
        if r.status_code != requests.codes.ok: raise Exception(f"http code == {r.status_code}")
        if not r.content or len(r.content) < 7: raise Exception(f"no content at {url}")
        # инициализирую lxml для парсинга xpath
        return html.fromstring(r.content.decode('utf-8'))

    def raw_query(self, url):
        """
        Загружаем страницу и распарсиваем её в XPath
        :param url:
        :return:
        :rtype: requests.Response[]
        :raises: :exc:
        """
        headers = {"Accept-Language": "de-DE,en;q=0.5"}
        r = requests.get(url, headers=headers)
        if r.status_code != requests.codes.ok: raise Exception(f"http code == {r.status_code}")
        if not r.content or len(r.content) < 7: raise Exception(f"no content at {url}")
        # инициализирую lxml для парсинга xpath
        return r.content.decode('utf-8')

    def xp(self, dom, xpath, throw_exc=False, attr_name='text', index=0, ret_none=None):
        """
        Поиск нужного элемента в доме и возврат нужного аттрибута
        с обработкой ошибок в нужном виде и выбросом исключением только если это нужно
        :param ret_none:
        :param dom:
        :param xpath:
        :param throw_exc: Можно указать что писать в искл.
        :param attr_name:
        :param index:
        :return:
        """
        try:
            el = dom.xpath(xpath)[index]
            if not attr_name:
                return el
            v = el.text_content() if attr_name == 'text' else el.get(attr_name)
            return v
        except Exception as e:
            if throw_exc:
                raise e
            return self.add_error(str(e), ret_none)

    def download_image(self, url, filename):
        """
        Сохраняю картинки в data/xxx.jpg
        :param url:
        :param filename:
        :return:
        """
        r = requests.get(url)
        if r.status_code != requests.codes.ok: raise Exception(f"image downloading error: http code == {r.status_code}")

        path = f"data/{filename}.jpg"
        with Image.open(io.BytesIO(r.content)) as im:
            im.save(path)