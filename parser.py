import requests
import re
import demjson
from gp import Gp
import random
from random import choice
from string import digits
from string import ascii_letters


data = {}

data['url'] = 'https://play.google.com/store/apps/details?id=com.sweet.candy.splash.judyblast.free'
template_name = 'google-play-main-2.tmpl'
path = "../_WHITE/white.com/"
        
gp = Gp()

content = gp.get_url(data['url'])
#print(content)
j = re.findall(r'AF_initDataCallback\((.+?})\)', content)
#print(json.loads(j))

for item in j:
    js_dict = demjson.decode(item)
    #print(js_dict)
    if js_dict['key'] == 'ds:18':
        for item_key in js_dict['data']:
            data['comment_text'] = item_key[0][4]
            data['comment_author'] = item_key[0][1][0]
            data['comment_avatar'] = item_key[0][1][1][3][2]
            if data['comment_avatar'][-3:] == '=mo':
                data['comment_avatar'] = data['comment_avatar'][:-3]
            data['comment_avatar'] = data['comment_avatar'] + '=w48-h48-n-rw'
            print("rrr", data['comment_avatar'])
            break

    if js_dict['key'] == 'ds:5':
        for item_key in js_dict['data']:
            #print(item_key)
            #i = 0
            #for t in item_key[12][0]:
            #    print(i, t)
            #    i = i + 1
            data['description'] = item_key[10][0][1]
            data['logo'] = item_key[12][1][3][2] + '=s180-rw'
            data['title'] = item_key[0][0]
            data['image1'] = item_key[12][0][0][3][2] + '=w720-h310-rw'
            data['image2'] = item_key[12][0][1][3][2] + '=w720-h310-rw'
            data['image3'] = item_key[12][0][2][3][2] + '=w720-h310-rw'
            #print("ggg", data['image1'])
            break

#    if js_dict['key'] == 'ds:5':
#        for item_key in js_dict['data']:
#            print(item_key)
#            print("===")
#            description_text = item_key[10][0][1]
#            print(description_text)
#            break
#            for item_data in item_key:
#                print(item_data)


#sys.exit()

dom = gp.get_dom(data['url'])

data['date'] = gp.get_date(dom)
data['size'] = gp.get_size(dom)
data['version'] = gp.get_version(dom)
data['meta_description'] = gp.get_meta_description(dom)
data['company_url'] = gp.get_company_url(dom)
data['company_email'] = gp.get_company_email(dom)
data['company_policy'] = gp.get_company_policy(dom)
#comment = gp.get_comment_code(dom)

for data_item, value in data.items():
    print(data_item, ": ", value)

f = open('templates/'+template_name, 'r+', encoding='utf8')
str_template = f.read()
f.close()

def download_file(file_url):
    global dump
    file = requests.get(file_url, stream=True).content
    filename = file_url.split('/')[-1]
    f = open(path+filename, 'wb')
    f.write(file)
    f.close()

str_template = re.sub("{{title}}", data['title'], str_template)
str_template = re.sub("{{comment-text}}", data['comment_text'], str_template)
str_template = re.sub("{{comment-author}}", data['comment_author'], str_template)

download_file(data['logo'])
download_file(data['image1'])
download_file(data['image2'])
download_file(data['image3'])
download_file(data['comment_avatar'])

data['logo'] = data['logo'].split('/')[-1]
data['image1'] = data['image1'].split('/')[-1]
data['image2'] = data['image2'].split('/')[-1]
data['image3'] = data['image3'].split('/')[-1]
data['comment_avatar'] = data['comment_avatar'].split('/')[-1]

str_template = re.sub("{{comment-avatar}}", data['comment_avatar'], str_template)
str_template = re.sub("{{description}}", data['description'], str_template)
str_template = re.sub("{{logo}}", data['logo'], str_template)
str_template = re.sub("{{image1}}", data['image1'], str_template)
str_template = re.sub("{{image2}}", data['image2'], str_template)
str_template = re.sub("{{image3}}", data['image3'], str_template)
str_template = re.sub("{{date}}", data['date'], str_template)
str_template = re.sub("{{size}}", data['size'], str_template)
str_template = re.sub("{{version}}", data['version'], str_template)
str_template = re.sub("{{meta_description}}", data['meta_description'], str_template)
str_template = re.sub("{{company-url}}", data['company_url'], str_template)
str_template = re.sub("{{company-email}}", data['company_email'], str_template)
str_template = re.sub("{{company-policy}}", data['company_policy'], str_template)
str_template = re.sub("{{url}}", data['url'], str_template)

rnd_str_10 = ''.join(choice(digits) for i in range(10))
rnd_str_13 = ''.join(choice(digits) for i in range(13))
rnd_str_3 = ''.join(choice(digits) for i in range(3))
rnd_str_7 = ''.join(choice(digits) for i in range(7))

lits_16 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
rnd_data_cfemail = ''.join(choice(lits_16) for i in range(44))

str_template = re.sub("{{inn}}", rnd_str_10, str_template)
str_template = re.sub("{{phone_code}}", rnd_str_3, str_template)
str_template = re.sub("{{phone_number}}", rnd_str_7, str_template)
str_template = re.sub("{{rnd_data_cfemail}}", rnd_data_cfemail, str_template)
str_template = re.sub("{{orgn}}", rnd_str_13, str_template)


class_str = ''.join(choice(ascii_letters).lower() for l in range(random.randint(3, 6)))
str_template = re.sub("{{class_name}}", class_str, str_template)

str_template = re.sub("{{div_1}}", gp.get_divs(param='<title>' + data['title'] + '</title>'), str_template)
str_template = re.sub("{{div_2}}", gp.get_divs(param='<img src="' + data['logo'] + '">'), str_template)
str_template = re.sub("{{div_3}}", gp.get_divs(param=data['title']), str_template)
str_template = re.sub("{{div_4}}", gp.get_divs(param='<a href="'+data['url']+'&hl=de&gl=de" class="knopa"><img src="images/google.png" height="60%" width="60%"></a>'), str_template)
str_out = re.sub("{{orgn}}", rnd_str_13, str_template)



f = open(path+'white.php', 'w+', encoding='utf8')
f.write(str_out)
f.close()
f = open(path+'gray.php', 'w+', encoding='utf8')
f.write(str_out)
f.close()
