import http.cookiejar,urllib,sys,time,http
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
exheaders=[      ('Host','passport.tianya.cn'),
                    ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'),  
                    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                    ('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
                    ('Accept-Encoding','gzip,deflate'),
                     ('Referer','http://www.tianya.cn/'),
                    ('Connection','keep-alive'),
                    ('Content-Type','application/x-www-form-urlencoded')

              ]
opener.addheaders=exheaders
loginurl='https://passport.tianya.cn/login?from=index&_goto=login'
postdate=urllib.parse.urlencode({'vwriter': 'xxx',
                            'vpassword': 'yyy',
                          })
re=opener.open(loginurl,postdate.encode('utf-8'))
#print (re.info())

response = urllib.request.urlopen('http://bbs.tianya.cn/post-stocks-1959291-13.shtml')
html = response.read()
#print ('html=', html)
f = open("a.html", 'w')
f.write(html.decode('utf8'))
f.close()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html.decode('utf8'))
#print (soup.prettify())
#for div in soup.find_all('div'):
#    print('------------------')
#    print(div)
#    if div.has_attr('js_username'):
#        print(div.js_username)
#
#
f = open('量子之鹰.txt', 'r')
last_time = f.read()
f.close()

time_list = []
for div in soup.find_all("div", class_='atl-item'):
    #print('------------------')
    #print(div.name)
    #print(div.attrs['js_username'], div.attrs['js_restime'])
    #print(div.attrs)
    if div.attrs['js_username'] == '量子之鹰':
        matched = True
        time_list.append(div.attrs['js_restime'])
        print(div.attrs['js_username'], div.attrs['js_restime'])
print('last_time:', last_time)
print('time_list:', time_list)

if len(time_list) > 0 and time_list[-1] != last_time:
    f = open('量子之鹰.txt', 'w')
    print('wirte...', time_list[-1])
    f.write(time_list[-1])
    f.flush()

    #from pythonzenity import Calendar
    #result = Calendar(title="Awesome Calendar",text_info="Your birthday ?")
    #print (result)
    print("ok")
    import subprocess

    applescript = """
        display dialog "量子之鹰说话了..." ¬
with title "This is a pop-up window" ¬
with icon caution ¬
buttons {"OK"}
    """
    
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)

f.close()
