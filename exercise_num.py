import json
def getinfo():
    infos = open("exercise_num_.json", "r")
    st = infos.read()
    t = json.loads(st)
    infos.close()
    return t["choose"],t["fill"],t["decide"]
def addinfo(x:int):
    info=open("exercise_num_.json", "r")
    st = info.read()
    t = json.loads(st)
    if x==1:
        t["choose"]+=1
    elif x==2:
        t["fill"]+=1
    elif x==3:
        t["decide"]+=1
    s=json.dumps(t)
    infos = open("exercise_num_.json", "w")
    infos.write(s)
    infos.close()

