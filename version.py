import json

ver = {
    "version": 0.5,
    "force": True,
    "msg": "发现新的更新咯，点击前往更新界面\nhttps://rcrwrate.github.io/Limbus-Company-zh_CN/\n\n快速安装\nhttps://limbus_company.lanzoul.com/b00wpywsh 密码: go0b\n\n",
    "forcemsg": "本次为强制更新，不更新会严重影响使用",
    "file": {
        "update.py": 1.0,
        "translate.py": 1.0
    }
}

with open("version.json", "w") as f:
    json.dump(ver, f)

for i in ver["file"]:
    # if i["ver"]:
    print(i)