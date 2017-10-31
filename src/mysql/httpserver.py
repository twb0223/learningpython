import socket
import signal
import errno

from time import sleep


def HttpRespone(header, html):
    f = file(html)
    contextlist = f.readlines()
    context = ''.join(contextlist)
    respone = "%s %d\n\n%s\n\n" % (header, len(context), context)
    return respone
