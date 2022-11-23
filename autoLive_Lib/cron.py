from datetime import datetime
import asyncio

LastTime = None
Tasks = []

def RunAt(m, cb):
    Tasks.append({
        "min": m,
        "cb": cb
    })

def GetTime():
    now = datetime.now()
    return { "hour": now.hour, "min": now.minute, "sec": now.second }

def OnTime(h, m, s):
    for task in Tasks:
        if task["min"] == m:
            asyncio.run(task["cb"]())

def InitLastTime():
    global LastTime
    time = GetTime()

    if LastTime == None:
        LastTime = time
        print("Run Init LastTime {}:{}:{}".format(time["hour"], time["min"], time["sec"]))

def Tick():
    global LastTime

    time = GetTime()

    if time["min"] != LastTime["min"]:
        OnTime(time["hour"], time["min"], time["sec"])
        LastTime = time