import json
import math
from .lib.gethttp import getHttpPage

class Folder:
    __fid = 0
    __caching = {'getFolder': ''}

    def __init__(self, fid):
        self.__fid = fid
    def setFid(self, fid):
        self.__fid = fid
    def getFid(self, fid):
        return self.__fid

    def getFolder(self, page = 1, method = 0):
        # 获取收藏夹下所有视频
        if method == 0 and self.__caching['getFolder'] != '':
            return self.__caching['getFolder']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/medialist/gateway/base/spaceDetail?media_id=" + str(self.__fid) + "&pn=" + str(page) + "&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp")
            DicData = json.loads(JsonData)
            FolderPage = math.ceil(int(DicData['data']['info']['media_count']) / 20)
            ReData = {"error": 0, 'page': FolderPage}
            VideoCount = 0
            for DicData_key in DicData['data']['medias']:
                VideoCount = VideoCount + 1
                ReData[VideoCount] = DicData_key['id']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getFolder'] = ReData
        return ReData