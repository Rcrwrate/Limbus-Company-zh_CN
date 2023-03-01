from .AsyncNetwork import Network
import re
from urllib.parse import quote

class Bing():
    BING = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=26D2C06B2477362AAF32FA81CC90E54E&IID=translator.5022.5"
    BING_INDEX = "https://cn.bing.com/translator?ref=TThis&text={text}&from=&to={to}"

    def __init__(self, s=Network({})) -> None:
        '''
        to: ja
        '''
        self.s = s

    async def __get_token(self, url):
        r = await self.s.get(url)
        r = re.findall(
            r'''var params_AbusePreventionHelper = \[([\s\S]+?)\]''', await r.text())[0].split(",")
        return r[0], r[1].replace("\"", "")

    async def __translate(self, data):
        self.s.changeHeader({
            "content-type": "application/x-www-form-urlencoded"
        })
        r = await self.s.post(self.BING, data=data)
        return await r.json()

    async def run(self, text, to) -> None:
        '''
        to: ja
        '''
        time, token = await self.__get_token(
            self.BING_INDEX.format(text=text, to=to))
        data = f"&fromLang=auto-detect&text={quote(text)}&to={to}&token={token}&key={time}" #.encode("utf-8")
        self.data = await self.__translate(data)
        return self.data[0]["translations"][0]["text"]
