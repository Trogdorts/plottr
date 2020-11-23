f = open('character_archetypes.txt', "r")
contents = f.read().splitlines()
len_contents = len(contents)
archetypes = {}

while True:
    if len_contents >=1:
        tmp = {}
        try:
            tmp['name'] = contents.pop(0)
        except:
            break
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        key, item = contents.pop(0).split(": ")
        tmp[key] = item
        try:
            key, item = contents.pop(0).split("is also known as: ")
        except:
            item = contents.pop(0)
        tmp['aka'] = item
        archetypes[tmp['name']] = tmp
        


    False
import json
print(json.dumps(archetypes, indent=5))
