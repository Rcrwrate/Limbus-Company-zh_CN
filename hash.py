import hashlib


def filehash(filename):
    try:
        with open(filename, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return ""


if __name__ == "__main__":
    print(filehash("update.py"))
