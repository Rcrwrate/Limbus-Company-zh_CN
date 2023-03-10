import os
from Lib.Network import Network

PATH = os.path.join("Translation", "zh-Hans", "Text",
                    "_AutoGeneratedTranslations.txt")

API_JSON = ""


def load():
    with open(PATH, "r", encoding="utf-8") as fn:
        ori = fn.readlines()

    ori_dict = {}
    for i in ori:
        tmp = i.split("=")
        L = len(tmp)
        J = tmp[0:int(L/2)]
        K = tmp[int(L/2):L]
        j = ""
        k = ""
        for i in J:
            j += i
            j += "="
        for i in K:
            k += i
            k += "="
        j = j[:-1]
        k = k[:-1]
        ori_dict[j] = k
    return ori_dict


def save(fin_dict):
    with open(PATH, "w", encoding="utf-8") as fn:
        for i in fin_dict:
            fn.write(i+"="+fin_dict[i])


def change(ori_dict):
    s = Network({})
    r = s.get(API_JSON).json()
    for i in r:
        ori_dict[i] = r[i]
    return ori_dict


save(change(load()))
