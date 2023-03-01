from Lib.Translate import Bing
from Lib.Network import Network
from flask import Flask, request


# s = Network({},log_level=10)
B = Bing()
B.get_token()

to = "zh-Hans"
app = Flask(__name__)


@app.route("/")
def index():
    text = request.args["text"]
    for i in ["Lv"]:
        if i in text:
            return text
    try:
        int(text)
        return text
    except:
        pass
    try:
        return B.translate(text, to)
    except:
        B.get_token()
        return B.translate(text, to)


app.run(port=9000, host='0.0.0.0')
