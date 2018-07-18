# -*- encode: utf-8 -*-
'''
@name pg-spider
@author honpery<honpery@gmail.com>
'''
import requests


class PgSpider(object):
    cookie = ""

    # main entry
    def run(self):
        print('pg-spider run success.')

        buttles = self.fetchList(
            openid='osewR0mH8noE7A7nkPWFmBHRb6wA',
            plat_id=1,
            mode_type=2,
            after_time=0,
            limit=20)

        buttle = self.fetchDetail({
            "openid": "osewR0mH8noE7A7nkPWFmBHRb6wA",
            "team_id": "11",
            "plat_id": "0",
            "battle_id": "164320883217363831",
            "mode": "103",
            "dt_event_time": "1531666524",
            "type": ""
        })

        print(buttles)

    # fetch list
    def fetchList(self, openid, plat_id, limit, mode_type, after_time):
        url = 'https://game.weixin.qq.com/cgi-bin/gamewap/getjdqssybattlelist'
        params = {
            "openid": openid,
            "plat_id": plat_id,
            "mode_type": mode_type,
            "after_time": after_time,
            "limit": limit
        }
        res = requests.get(url, params=params, headers=self.getHeader())
        json = res.json()

        if json["errcode"] != 0:
            print("获取列表失败\nurl: %s\nstatus: %d\nmessage: %s" %
                  (res.url, json["errcode"], json["errmsg"]))
            return []

        if res.status_code >= 400:
            print("获取列表出错\nurl: %s\nstatus: %d" % (res.url, res.status_code))
            return []

        return json["battle_list"]

    # fetch detail
    def fetchDetail(self, params={}):
        url = 'https://game.weixin.qq.com/cgi-bin/gamewap/getjdqssybattledetail'
        res = requests.get(url, params=params, headers=self.getHeader())
        json = res.json()

        if json["errcode"] != 0:
            print("获取详情失败\nurl: %s\nstatus: %d\nmessage: %s" %
                  (res.url, json["errcode"], json["errmsg"]))
            return {}

        if res.status_code >= 400:
            print("获取详情出错\nurl: %s\nstatus: %d" % (res.url, res.status_code))
            return {}

        return json

    def getHeader(self):
        return {"cookie": self.cookie}


if __name__ == '__main__':
    pg = PgSpider()
    pg.run()
