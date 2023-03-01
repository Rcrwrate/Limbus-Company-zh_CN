from .Network import Network
import re
from urllib.parse import quote


class Bing():
    BING = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=84E388387BD544F3A3AC8102AEED9EFE&IID=translator.5023.1"
    BING_INDEX = "https://cn.bing.com/translator?ref=TThis&text={text}&from=&to={to}"

    def __init__(self, s=Network({})) -> None:
        '''
        to: ja
        '''
        self.s = s

    def get_token(self, url="https://cn.bing.com/translator"):
        r = self.s.get(url)
        r = re.findall(
            r'''var params_AbusePreventionHelper = \[([\s\S]+?)\]''', r.text)[0].split(",")
        self.time, self.token = r[0], r[1].replace("\"", "")
        return r[0], r[1].replace("\"", "")

    def _translate(self, data):
        self.s.changeHeader({
            "content-type": "application/x-www-form-urlencoded"
        })
        r = self.s.post(self.BING, data=data)
        return r.json()

    def run(self, text, to) -> None:
        '''
        to: ja
        '''
        time, token = self.get_token(
            self.BING_INDEX.format(text=text, to=to))
        # .encode("utf-8")
        data = f"&fromLang=auto-detect&text={quote(text)}&to={to}&token={token}&key={time}"
        self.data = self._translate(data)
        return self.data[0]["translations"][0]["text"]

    def translate(self, text, to):
        data = f"&fromLang=auto-detect&text={quote(text)}&to={to}&token={self.token}&key={self.time}"
        self.data = self._translate(data)
        return self.data[0]["translations"][0]["text"]
