

@SK_KAZI
Sk-Kazi Update sk2.py
 1 contributor
63 lines (60 sloc)  1.92 KB
#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 infect.xo")

try:
    os.mkdir("/sdcard/infect-tool")
except OSError:
    pass

sk = """
\033[1;97m  ____  _  __   ___  _____ _____ ___ ____ ___    _    _
/ ___|| |/ /  / _ \|  ___|  ___|_ _/ ___|_ _|  / \  | |
\___ \| ' /  | | | | |_  | |_   | | |    | |  / _ \ | |
 ___) | . \  | |_| |  _| |  _|  | | |___ | | / ___ \| |___
|____/|_|\_\  \___/|_|   |_|   |___\____|___/_/   \_\_____|
\033[1;97m     
\033[1;93m      
\033[1;93m      
\033[1;93m      
\033[1;97m     
\033[1;97m     
\033[1;97m------------------------------------------------- 
\033[1;97m(~) Author  : SK Official
\033[1;97m(~) Github  : https://github.com/mrsk3395/sk.git
\033[1;97m(~) Fb Page : https://facebook.com/sk.picchi
\033[1;97m-------------------------------------------------
"""

def main():
    os.system("clear")
    print(sk)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(sk)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install sk tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install infect extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    sk_kazi = raw_input("\n[!] Select a valid option : ")
    if sk_kaI =="1":
        os.system("cd data && python2 data")
    if tech_abm =="2":
        os.system("cd exts && python2 exts")
    if sk_kazi =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()
