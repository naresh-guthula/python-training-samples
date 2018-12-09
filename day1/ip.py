import subprocess
import sys

if sys.platform == 'linux':
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

op = subprocess.check_output(cmd)
print(op.decode('ascii'))
