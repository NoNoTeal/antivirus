import time
import sys
import random

n = 0
for x in range(0, 101):
    a = 'Clean in Progress: ' + n.__str__() + '%' + ' done...'
    n = n + 1
    sys.stdout.write("\r"+a)
    time.sleep(random.randint(0, 1))
if n == 101:
    time.sleep(3)
    sys.stdout.write('\r' + 'Duplicate Files and Porn Folders were deleted!' + '\n')