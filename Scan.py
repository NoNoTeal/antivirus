import time
import sys

a = 'Scanning System...'
print(a)
for x in range(0, 100):
    r = x + 1
    sys.stdout.write('\r'+r.__str__()+'% Done!')
    time.sleep(3)

if r == 100:
    time.sleep(3)
    sys.stdout.write('\r' + 'No viruses were found.' + '\n')