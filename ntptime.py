import arrow
import socket
import struct
import sys

def RequestTimefromNtp(addr='0.de.pool.ntp.org'):
    REF_TIME_1970 = 2208988800      # Reference time
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    data = b'\x1b' + 47 * b'\0'
    client.sendto( data, (addr, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        t = struct.unpack( '!12I', data )[10]
        t -= REF_TIME_1970
    return arrow.get(t)

def now():
    if (sys.platform == "win32"):
        return time.clock() + time0
    return time.time()

print(RequestTimefromNtp())
print(now())
