import json
import re
import random
from random import choice
from string import ascii_letters

from parse import Parse

class Gp(Parse):

    def __init__(self):
        Parse.__init__(self, gp_name="akusherstvo.ru")

    def get_dom(self, url):
        try:
            dom = self.query(url)
            return dom

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_title(self, dom):
        try:

            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//h1', throw_exc=True, index=0)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_date(self, dom):
        try:
            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[1]//span//div[1]//span', throw_exc=True, index=0)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            #for item in el:
            #    print(item)
            #print(el)
            #sys.exit()
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_date_ios(self, dom):
        try:
            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[1]//span//div[1]//span', throw_exc=True, index=0)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            #for item in el:
            #    print(item)
            #print(el)
            #sys.exit()
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)


    def get_size(self, dom):
        try:
            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[2]//span//div[1]//span', throw_exc=True, index=0)#, attr_name=None)
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_version(self, dom):
        try:
            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[4]//span//div[1]//span', throw_exc=True, index=0)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            #for item in el:
             #   print(item)
            #print(el)
            #sys.exit()
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_meta_description(self, dom):
        try:
            el = self.xp(dom, '//head//meta[11]', throw_exc=True, index=0, attr_name='content')
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_company_url(self, dom):
        try:
            el = self.xp(dom, '//head//meta[18]', throw_exc=True, index=0, attr_name='content')
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_company_email(self, dom):
        try:
            try:
                el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[11]//span//div[1]//span[1]//div[2]', throw_exc=True, index=0)
            except:
                try:
                    el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[10]//span//div[1]//span[1]//div[2]', throw_exc=True, index=0)
                except:
                    el = self.xp(dom,
                                 '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[9]//span//div[1]//span[1]//div[2]',
                                 throw_exc=True, index=0)
            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_company_policy(self, dom):
        try:
            try:
                el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[11]//span//div[1]//span[1]//div[3]//a', throw_exc=True, index=0, attr_name='href')
            except:
                try:
                    el = self.xp(dom, '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[10]//span//div[1]//span[1]//div[3]//a', throw_exc=True, index=0, attr_name='href')
                except:
                    el = self.xp(dom,
                                 '//div[1]//div[4]//div[2]//div[1]//main//c-wiz[4]//div[1]//div[2]//div[1]//div[9]//span//div[1]//span[1]//div[3]//a', throw_exc=True, index=0, attr_name='href')

            return el

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_comment_code(self, dom):
        lot = {}
        try:
            el = self.xp(dom, '//div/c-wiz', throw_exc=True, index=0, attr_name=None)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            for item in el:
                print(item)
            #print(el)

            lot['lot_id'] = int(re.sub("[^0-9]", "", el.get("id")))  # из tover_price_123456 выделяю id товара
            lot['price'] = int(el.get('content'))

            lot['title'] = self.xp(dom, '//title', throw_exc=True)
            lot['img'] = "https:" + self.xp(dom, "//div[@id='itemCard']//div[contains(@class,'itemImg')]//img[1]",
                                            throw_exc=True, attr_name='src')
            self.download_image(lot['img'], f"{self.gp_name}-{lot['lot_id']}")

            t = self.xp(dom, '//div[@itemprop="description"]', throw_exc=False, ret_none="")
            lot['description'] = re.sub("(\t|\n|\r)", "", t)[:160]

            print("lot = ", json.dumps(lot, ensure_ascii=False))

            return lot

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_comment_code2(self, dom):
        lot = {}
        try:
            el = self.xp(dom, '//div//div//c-wiz', throw_exc=True, index=0, attr_name=None)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            print(el)

            lot['lot_id'] = int(re.sub("[^0-9]", "", el.get("id")))  # из tover_price_123456 выделяю id товара
            lot['price'] = int(el.get('content'))

            lot['title'] = self.xp(dom, '//title', throw_exc=True)
            lot['img'] = "https:" + self.xp(dom, "//div[@id='itemCard']//div[contains(@class,'itemImg')]//img[1]",
                                            throw_exc=True, attr_name='src')
            self.download_image(lot['img'], f"{self.gp_name}-{lot['lot_id']}")

            t = self.xp(dom, '//div[@itemprop="description"]', throw_exc=False, ret_none="")
            lot['description'] = re.sub("(\t|\n|\r)", "", t)[:160]

            print("lot = ", json.dumps(lot, ensure_ascii=False))

            return lot

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    def get_url(self, url):
        try:
            dom = self.raw_query(url)
        except:
            dom = ""
        return dom

    def get_lot_static(self, url):
        """
        Парсим карточку товара
        !!! Парсинг поплывет как только источник изменит верстку
        :param url: ссылка на карточку
        :return:
        """
        lot = {}
        try:
            dom = self.query(url)

            # удобный тег - из аттр. content получю цену, а из id - lot_id
            el = self.xp(dom, '//div', throw_exc=True, index=0, attr_name=None)
            #el = self.xp(dom, '//span[@itemprop="price"]', throw_exc=True, attr_name=None)
            print(el)

            lot['lot_id'] = int(re.sub("[^0-9]", "", el.get("id")))  # из tover_price_123456 выделяю id товара
            lot['price'] = int(el.get('content'))

            lot['title'] = self.xp(dom, '//title', throw_exc=True)
            lot['img'] = "https:" + self.xp(dom, "//div[@id='itemCard']//div[contains(@class,'itemImg')]//img[1]",
                                            throw_exc=True, attr_name='src')
            self.download_image(lot['img'], f"{self.gp_name}-{lot['lot_id']}")

            t = self.xp(dom, '//div[@itemprop="description"]', throw_exc=False, ret_none="")
            lot['description'] = re.sub("(\t|\n|\r)", "", t)[:160]

            print("lot = ", json.dumps(lot, ensure_ascii=False))

            return lot

        except Exception as e:
            print("err:", e)
            return self.add_error(e, True)

    @staticmethod
    def rand_str(s_min, s_max):
        s1 = ''.join(choice(ascii_letters).lower() for l in range(random.randint(s_min, s_max)))
        s2 = ''.join(choice(ascii_letters).lower() for l in range(random.randint(s_min, s_max)))
        return s1 + '-' + s2

    def get_divs(self, num=6, param=''):
        div_str = ""
        i=0
        i_max = random.randint(1, num)
        i_param = random.randint(1, i_max) - 1
        flag = 0
        while i < i_max:
            class_str = self.rand_str(2, 3)
            div_str = div_str + '<div class="' + class_str + '">' + "\n"

            j=0
            j_max = random.randint(1, num)
            j_param = random.randint(1, j_max) - 1
            while j < j_max:
                class_str = ''.join(choice(ascii_letters).lower() for l in range(random.randint(3, 6)))
                div_str = div_str + '   <div style="' + class_str + '">' + "\n"

                k=0
                k_max = random.randint(1, num)
                while k < k_max:
                    class_str = self.rand_str(1, 4)
                    div_str = div_str + '<div class="' + class_str + '">'

                    if not flag and i == i_param and j == j_param:
                        div_str = div_str + param
                        flag = 1

                    div_str = div_str + '</div>'
                    k = k + 1

                div_str = div_str + '</div>'+"\n"
                j = j + 1

            div_str = div_str + '</div>'+"\n"
            i = i + 1

        return div_str
