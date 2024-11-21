#<\>!python3.12
#<\>coded by ART
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf FILE.so')
except:
    pass
os.system('rm -rf FILE.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('FILE.so'):
        os.system('curl -L https://github.com/ARTTTTTT-404/FILE/blob/main/FILE.cpython-312.so?raw=true -o FILE.so') 
        import FILE  
    else:
        import FILE
elif bit == '32bit':
    exit('\033[1;31m\n SORRY SYSTEM OR 32BIT DEVICE NOT SUPPORTED ')
