import json
from .lib.gethttp import getHttpPage

class Video:
    __aid = 0
    __caching = {'getVideoInfo': '', 'getVideoData': '', 'getVideoTag': ''} # 缓存

    def __init__(self, aid):
        self.__aid = aid
    def setAid(self, aid):
        self.__aid = aid
    def getAid(self, aid):
        return self.__aid

    def getVideoInfo(self, method = 0):
        # 获取视频信息
        if method == 0 and self.__caching['getVideoInfo'] != '':
            return self.__caching['getVideoInfo']
        try:
            JsonData = getHttpPage("http://api.bilibili.com/x/web-interface/view?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)
            ReData = {
                "error" : 0,
                "cid" : DicData['data']['cid'], # CID
                "title" : DicData['data']['title'], # 标题
                "pic" : DicData['data']['pic'], # 封面url
                "videos" : DicData['data']['videos'], # 分P数
                "tid" : DicData['data']['tid'], # 分区编号
                "tname" : DicData['data']['tname'], # 版名
                "copyright" : DicData['data']['copyright'], # 作品类型
                "pubdate" : DicData['data']['pubdate'], # 投稿时间
                "desc" : DicData['data']['desc'], # 简介
                "duration" : DicData['data']['duration'], # 时常
                "up" : { # UP主信息
                    "mid" : DicData['data']['owner']['mid'], # UID
                    "name" : DicData['data']['owner']['name'], # 用户名
                    "face" : DicData['data']['owner']['face'] # 头像url
                }
            }
            StaffInfoReturn = ""
            if 'staff' in DicData['data']:
                StaffInfo = DicData['data']['staff']
                for StaffInfo_Value in StaffInfo:
                    StaffInfoReturn += str(StaffInfo_Value['mid']) + ',' + StaffInfo_Value['name'] + ',' + StaffInfo_Value['title'] + '|'
            else:
                StaffInfoReturn = str(DicData['data']['owner']['mid']) + ',' + DicData['data']['owner']['name'] + ',UP主|'
            ReData['staff'] = StaffInfoReturn[0:-1]
            # 构建staff列表字符串
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoInfo'] = ReData
        return ReData

    def getVideoData(self, method = 0):
        # 获取视频实时数据
        if method == 0 and self.__caching['getVideoData'] != '':
            return self.__caching['getVideoData']
        try:
            JsonData = getHttpPage("http://api.bilibili.com/archive_stat/stat?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)
            ReData = {
                "error" : 0,
                "view" : DicData['data']['view'], # 播放量
                "danmaku" : DicData['data']['danmaku'], # 弹幕
                "reply" : DicData['data']['reply'], # 评论
                "favorite" : DicData['data']['favorite'], # 收藏
                "coin" : DicData['data']['coin'], # 硬币
                "share" : DicData['data']['share'], # 分享
                "like" : DicData['data']['like'] # 点赞
            }
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoData'] = ReData
        return ReData

    def getVideoTag(self, method = 0):
        if method == 0 and self.__caching['getVideoTag'] != '':
            return self.__caching['getVideoTag']
        # 获取视频所有Tag
        try:
            JsonData = getHttpPage("http://api.bilibili.com/x/tag/archive/tags?aid=" + str(self.__aid))
            DicData = json.loads(JsonData)['data']
            ReData = {"error": 0}
            for DicData_Key in DicData:
                ReData[DicData_Key['tag_id']] = DicData_Key['tag_name']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching['getVideoTag'] = ReData
        return ReData
