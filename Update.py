import sys
import time
import socket
print('Checking for updates...')
REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

if is_connected(REMOTE_SERVER):
    time.sleep(15)
    sys.stdout.write('\rNo New Updates Are Available at this time. Check back later.\n')
else:
    sys.stdout.write('\rYou are not connected to the internet!\n')