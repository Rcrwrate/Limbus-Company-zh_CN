from .Network import Network
import re


class Bing():
    BING = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=84E388387BD544F3A3AC8102AEED9EFE&IID=translator.5023.1"
    BING_INDEX = "https://cn.bing.com/translator?ref=TThis&text={text}&from=&to={to}"

    def __init__(self, text, to, s=Network({})) -> None:
        '''
        to: ja
        '''
        self.s = s
        time, token = self.__get_token(
            self.BING_INDEX.format(text=text, to=to))
        data = f"&fromLang=auto-detect&text={text}&to={to}&token={token}&key={time}".encode(
            "utf-8")
        self.data = self.__translate(data)
        self.text = self.data[0]["translations"][0]["text"]

    def __get_token(self, url):
        r = self.s.get(url)
        r = re.findall(
            r'''var params_AbusePreventionHelper = \[([\s\S]+?)\]''', r.text)[0].split(",")
        return r[0], r[1].replace("\"", "")

    def __translate(self, data):
        self.s.changeHeader({
            "content-type": "application/x-www-form-urlencoded"
        })
        r = self.s.post(self.BING, data=data)
        return r.json()
