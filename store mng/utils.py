import json
def save(data,filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def load(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return data
