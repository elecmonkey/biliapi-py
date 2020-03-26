# -- coding: utf-8 --


import json
import math
import urllib.request
from .lib.gethttp import *

class Upper:
    __uid = 0
    __caching = {'getUpperVideo': '', 'getUpperNavnum': '', 'getUpperStat': '',
                'getUpperRelationstat': '', 'getUpperSpaceTop': '', 'getUpperInfo': ''}

    def __init__(self, uid):
        self.__uid = uid
    def setUid(self, uid):
        self.__uid = uid
    def getUid(self, uid):
        return self.__uid

    def getUpperVideo(self, method = 0):
        # 获取UP主所有视频
        if method == 0 and self.__caching['getUpperVideo'] != '':
            return self.__caching['getUpperVideo']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/space/arc/search?mid=" + str(self.__uid) + "&pn=1&ps=1")
            DicData = json.loads(JsonData)
            UpperPage = math.ceil(int(DicData['data']['page']['count']) / 20)
            ReData = {"error": 0}
            VideoCount = 0
            for iFolderPage in range(1, UpperPage + 1):
                JsonData = getHttpPage("https://api.bilibili.com/x/space/arc/search?mid=" + str(self.__uid) + "&pn=" + str(iFolderPage) + "&ps=20")
                DicData = json.loads(JsonData)
                for DicData_key in DicData['data']['list']['vlist']:
                    VideoCount = VideoCount + 1
                    ReData[VideoCount] = DicData_key['aid']
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
            self.__caching = ReData
        return ReData

    def getUpperNavnum(self, method = 0):
        # 获取UP主作品数量
        if method == 0 and self.__caching['getUpperNavnum'] != '':
            return self.__caching['getUpperNavnum']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/space/navnum?mid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            self.__caching['getUpperNavnum'] = {"error": 0,
                    "video" : DicData['data']['video'],
                    "audio" : DicData['data']['audio']
            }
        except KeyError:
            self.__caching['getUpperNavnum'] = {"error": 1}
        except:
            self.__caching['getUpperNavnum'] = {"error": 2}
        return self.__caching['getUpperNavnum']

    def getUpperStat(self, method = 0):
        # 获取UP主作品总数据
        if method == 0 and self.__caching['getUpperStat'] != '':
            return self.__caching['getUpperStat']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/space/upstat?mid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            self.__caching['getUpperStat'] = {"error": 0,
                    "archive" : DicData['data']['archive']['view'],
                    "article" : DicData['data']['article']['view'],
                    "likes" : DicData['data']['likes']
            }
        except KeyError:
            self.__caching['getUpperStat'] = {"error": 1}
        except:
            self.__caching['getUpperStat'] = {"error": 2}
        return self.__caching

    def getUpperRelationstat(self, method = 0):
        # 获取UP主关注人数、粉丝数
        if method == 0 and self.__caching['getUpperRelationstat'] != '':
            return self.__caching['getUpperRelationstat']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/relation/stat?vmid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            self.__caching['getUpperRelationstat'] = {"error": 0,
                    "following" : DicData['data']['following'], # 关注数
                    "follower" : DicData['data']['follower'] # 粉丝数
            }
        except KeyError:
            self.__caching['getUpperRelationstat'] = {"error": 1}
        except:
            self.__caching['getUpperRelationstat'] = {"error": 2}
        return self.__caching

    def getUpperSpaceTop(self, method = 0):
        # 获取UP主首页推荐
        if method == 0 and self.__caching['getUpperSpaceTop'] != '':
            return self.__caching['getUpperSpaceTop']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/space/top/arc?vmid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            if DicData['message'] == '没有置顶视频':
                self.__caching['getUpperSpaceTop'] = {"error": 1}
            else:
                self.__caching['getUpperSpaceTop'] = {
                    "error": 0,
                    "aid": DicData['data']['aid'],  # AID
                    "title": DicData['data']['title'],  # 标题
                    "pic": DicData['data']['pic'],  # 封面url
                    "videos": DicData['data']['videos'],  # 分P数
                    "tid": DicData['data']['tid'],  # 分区编号
                    "tname": DicData['data']['tname'],  # 版名
                    "copyright": DicData['data']['copyright'],  # 作品类型
                    "pubdate": DicData['data']['pubdate'],  # 投稿时间
                    "desc": DicData['data']['desc'],  # 简介
                    "duration": DicData['data']['duration'],  # 时常
                    "reason": DicData['data']['reason'] # 推荐理由
                }
        except KeyError:
            self.__caching['getUpperSpaceTop'] = {"error": 1}
        except:
            self.__caching['getUpperSpaceTop'] = {"error": 2}
        return self.__caching['getUpperSpaceTop']

    def getUpperInfo(self, method = 0):
        # 获取UP主信息
        if method == 0 and self.__caching['getUpperInfo'] != '':
            return self.__caching['getUpperInfo']
        try:
            JsonData = getHttpPage("https://api.bilibili.com/x/space/acc/info?mid=" + str(self.__uid))
            DicData = json.loads(JsonData)
            ReData = {
                "error": 0,
                "name" : DicData['data']['name'], # ID
                "sex" : DicData['data']['sex'], # 性别
                "face" : DicData['data']['face'], # 头像url
                "sign" : DicData['data']['sign'], # 个性签名
                "level" : DicData['data']['level'], # 等级
                "birthday" : DicData['data']['birthday'], # 生日
                "official_title" : DicData['data']['official']['title'], # 官方认证信息
                "top_photo" : DicData['data']['top_photo'] # 空间横幅url
            }
        except KeyError:
            ReData = {"error": 1}
        except:
            ReData = {"error": 2}
        self.__caching = ReData
        return ReData