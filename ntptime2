import ntplib
from datetime import datetime

client = ntplib.NTPClient()
server = 'pool.ntp.org'

resp = client.request(server, version=3)

print("offset", resp.offset)
print("delay", resp.delay)

# timestamps are converted to native "UNIX" timestamps
print(resp.orig_time)
