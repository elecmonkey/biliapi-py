import urllib.request
import random

def getHttpPage(url):
    Headers = [{
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"    
    },{
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    },{
        "User-Agent":
        "Mozilla/5.0 (Linux; Android 7.1.1; Mi Note 3 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36"
    },{
        "User-Agent":
        "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
    },{
        "User-Agent":
        "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
    }]
    return urllib.request.urlopen(urllib.request.Request(url=url, headers=Headers[random.randint(0,4)])).read().decode()
