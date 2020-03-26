import json
import urllib.parse
from .lib.gethttp import getHttpPage

class Search:
    __keyword = ''
    __caching = {}

    def __init__(self, keyword):
        self.__keyword = keyword
    def setUid(self, keyword):
        self.__keyword = keyword
    def getUid(self, keyword):
        return self.__keyword

    def getSearch(self, page = 1, method = 0):
        # 全站搜索接口
        # 每页20条，page为页数。
        if method == 0 and self.__caching != {}:
            return self.__caching
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/web-interface/search/type?context=&page=" + str(page) + "&order=&keyword=" + urllib.parse.quote(self.__keyword) + "&duration=&tids_1=&tids_2=&__refresh__=true&search_type=video&highlight=1&single_column=0")
            DicData = json.loads(JsonData)
            PageData = {
                "numResults" : DicData['data']['numResults'],
                "numPages": DicData['data']['numPages']
            }
            ReData = { }
            if (page == PageData['numPages']):
                iPage = PageData['numResults'] - 20 * (page - 1)
            else :
                iPage = 20
            for iGetVideo in range(0, iPage):
                ReData[iGetVideo] = {
                    "aid" : DicData['data']['result'][iGetVideo]['aid'],
                    "author" : DicData['data']['result'][iGetVideo]['author'],
                    "uid" : DicData['data']['result'][iGetVideo]['mid'],
                    "typeid" : DicData['data']['result'][iGetVideo]['typeid'],
                    "typename" : DicData['data']['result'][iGetVideo]['typename'],
                    "title" : DicData['data']['result'][iGetVideo]['title'],
                    "description" : DicData['data']['result'][iGetVideo]['description'],
                    "pic" : DicData['data']['result'][iGetVideo]['pic'],
                    "tag" : DicData['data']['result'][iGetVideo]['tag']
                }
            self.__caching = {"error": 0, "Page" : PageData, "Data" : ReData}
        except KeyError:
            self.__caching = {"error": 1}
        except:
            self.__caching = {"error": 2}
        return self.__caching