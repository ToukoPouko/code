import requests
'''headers = \
                {
                    'Host': 'strawpoll.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en - us, en; q = 0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Charset': 'ISO - 8859 - 1, utf - 8; = 0.7, *;q = 0.7',
                    'Referer': 'https://strawpoll.com/1wgxrzw3,
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Length': '29',
                    'Cookie': 'lang=en',
                    'DNT': '1',
                    'Connection': 'close'
                }'''

payload = {'pid': "1wgxrzw3", 'oids': "check22728490"}

r = requests.post("https://strawpoll.com/vote", data=payload)
