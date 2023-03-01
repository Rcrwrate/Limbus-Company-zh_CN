import json

o = {}

with open("list.txt", "r", encoding="utf-8") as f:
    l = f.readlines()


def to_json(l: list, ori_dict: json = {}):

    for i in l:
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


o = to_json(l, o)

with open("API.json", "w") as f:
    json.dump(o, f)
