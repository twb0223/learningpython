
def makeSessionId(st):
    import md5,time,base64,string
    m.update('this iiii')
    m.update(str(time.time()))
    m.update(st)
    return string.replace(base64.encodestring(m.digest())[:-3],'/','/span>')


print(makeSessionId("dasdqw"))
