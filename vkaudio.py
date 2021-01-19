'''
# TG  = https://t.me/zakovskiy
# Git = https://github.com/Zakovskiy
# Vk  = https://vk.com/id514492216
'''

import json
import requests

class Client():

    '''
    #-> param "token" -- VK User Token - get this - https://oauth.vk.com/authorize?client_id=6121396&scope=501198815&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1
    '''
    def __init__(self, token:str = None, api_version:str = "5.102"):
        if token == None:
            exit("Empty param = `token`");
        else:
            self.token = token;
            self.v     = api_version;
            self.api   = "https://api.vk.com/method/";

    # return the user or group audio list
    def audio_get(self, owner_id:int = 1, count:int = 500):
        response = requests.get(f"{self.api}audio.get?access_token={self.token}&v={self.v}&owner_id={owner_id}&count={count}").json();
        return response;

    def audio_add(self, owner_id:int = 1, audio_id:int = 0):
        response = requests.get(f"{self.api}audio.add?access_token={self.token}&v={self.v}&owner_id={owner_id}&audio_id={audio_id}").json();
        return response;

    def audio_delete(self, owner_id:int = 1, audio_id:int = 0):
        response = requests.get(f"{self.api}audio.delete?access_token={self.token}&v={self.v}&owner_id={owner_id}&audio_id={audio_id}").json();
        return response;

    def audio_search(self, text:str = None, count:int = 100):
        response = requests.get(f"{self.api}audio.search?access_token={self.token}&v={self.v}&count={count}&q={text}").json();
        return response;

    def get_popular_audio(self, count:int = 10):
        response = requests.get(f"{self.api}audio.getPopular?access_token={self.token}&v={self.v}&count={count}").json();
        return response;
