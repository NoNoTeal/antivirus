import time
import sys
import random

n = 0
print('Updating Security Protocol. This May Take a While')
for x in range(0, 101):
    a = 'Updating ' + random.choice(['Antivirus.lib','Security.lib','TrojanBlocker.lib','VPN.lib','IPExposer.lib','DeleteSystem32.lib','CoreSystem.lib', 'Framework.lib', 'Framework.lib', 'Framework.lib', 'Framework.lib', 'Framework.lib']) + ': ' + n.__str__() + '%' + ' done...'
    n = n + 1
    sys.stdout.write("\r"+a)
    time.sleep(random.randint(5, 10))
if n == 101:
    time.sleep(3)
    sys.stdout.write('\r' + 'Security was updated successfully!' + '\n')