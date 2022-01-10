import json
import requests


class Client:

    
    def __init__(self, access_token: str, api_version: str = "5.68"):
        """
        **Параметры**
            - access_token - уникальный ключ от аккаунта, получать > https://oauth.vk.com/authorize?client_id=6121396&scope=501198815&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1
        """
        
        self.headers = {
            "User-Agent":"VKAndroidAPP/5.12-2353 (this; library; _; by; zakovskiy)"
        }
        self.token = token
        self.v = api_version
        self.api = "https://api.vk.com/method/"

    def audio_get(self, owner_id: int, count: int = 500):
        return requests.get(f"{self.api}audio.get?access_token={self.token}&v={self.v}&owner_id={owner_id}&count={count}", headers=self.headers).json()

    def audio_add(self, owner_id: int, audio_id: int):
        return requests.get(f"{self.api}audio.add?access_token={self.token}&v={self.v}&owner_id={owner_id}&audio_id={audio_id}", headers=self.headers).json()

    def audio_delete(self, owner_id: int, audio_id: int):
        return requests.get(f"{self.api}audio.delete?access_token={self.token}&v={self.v}&owner_id={owner_id}&audio_id={audio_id}", headers=self.headers).json()

    def audio_search(self, text: str, count: int = 5):
        return requests.get(f"{self.api}audio.search?access_token={self.token}&v={self.v}&count={count}&q={text}", headers=self.headers).json()

    def get_popular_audio(self, count: int = 10):
        return requests.get(f"{self.api}audio.getPopular?access_token={self.token}&v={self.v}&count={count}", headers=self.headers).json()
