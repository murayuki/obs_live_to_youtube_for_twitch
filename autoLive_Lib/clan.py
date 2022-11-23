clan = {}

def setClan(key, value):
    clan[key] = value

def getClan(key):
    return clan[key]

def removeClan(key):
    del clan[key]

def isClanKey(key):
    return key in clan.keys()

async def setClanAsync(key, value):
    clan[key] = value

async def getClanAsync(key):
    return clan[key]

async def removeClanAsync(key):
    del clan[key]

async def isClanKeyAsync(key):
    return key in clan.keys()