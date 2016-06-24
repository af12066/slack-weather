#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
from slacker import Slacker

class Slack(object):
    """
    SlackにポストするためのSlackerクラス
    """
    __slacker = None

    def __init__(self, token):
        self.__slacker = Slacker(token)

    def get_channel_list(self):
        """
        SlackチームのチャンネルID, チャンネル名の取得
        """
        raw_data = self.__slacker.channels.list().body
        result = []

        for data in raw_data['channels']:
            result.append(dict(channel_id=data['id'], channel_name=data['name']))

        return result

    def post_message_to_channel(self, channel, message):
        """
        Slackチームの任意のチャンネルにメッセージを投稿
        """
        channel_name = '#' + channel
        self.__slacker.chat.post_message(channel_name, message)

def getjsondata():
    """
    天気Web APIからJSONデータの取得
    """
    response = urllib.request.urlopen("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010").read().decode("utf-8") # cityで東京のidを指定
    response = json.loads(response)
    
    response = response['forecasts'][0] #[0]:今日，[1]:明日，[2]:明後日
    response.update({'city':response['location']['city']})

    return response['forecasts'][0]
