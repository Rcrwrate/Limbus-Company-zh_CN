from Lib.Network import Network
import os


s = Network({})
r = s.get("https://rcrwrate.github.io/Limbus-Company-Work-Dataset/Substitutions.txt")
with open(os.path.join("Translation", "zh-Hans", "Text",
                       "_Substitutions.txt"), "wb") as f:
    f.write(r.content)
