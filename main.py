import os
import shutil
import data
"""<--
×××××××××××××××××××××××××××××××××××××××××××××××××××××
Tools Description
Name    :  Smail-MBF
Author  :  AseCx
Support :  XiuzCode Team
Version :  Lates Version (0.1)
License :  MIT License
×××××××××××××××××××××××××××××××××××××××××××××××××××××
-->"""
class AseCx:
       def __init__(self):
             try: shutil.rmtree("data/__pycache__")
             except: pass

       def menghadeh(self):
             try:
                  cookies = open('session/cookies.log').read().strip()
                  login, title, ip = data.login.smile(cookies).login()
                  if login:
                        data.run.menu(cookies).menuP()
                  else:
                        os.remove('session/cookies.log')
                        data.logo.banner()
                        exit("\x1b[32;1m(\x1b[31;1m!\x1b[32;1m) \x1b[31;1mSESSION COOKIES HABIS, LOGIN ULANG!")
             except IOError:
                  data.logo.banner()
                  cookies = input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mCOOKIES   \x1b[30;1m: \x1b[32;1m")
                  login, title, ip = data.login.smile(cookies).login()
                  if login:
                       try:
                            os.mkdir("result")
                       except: pass
                       try:
                            os.mkdir("session")
                       except: pass
                       with open("session/cookies.log", "w") as f:
                              f.write(cookies.strip())
                       data.run.menu(cookies).menuP()
                  else:
                       data.logo.banner()
                       exit("\x1b[32;1m(\x1b[31;1m!\x1b[32;1m) \x1b[31;1mSESSION COOKIES HABIS, LOGIN ULANG!")


if __name__=='__main__':
       try:
            AseCx().menghadeh()
       except KeyboardInterrupt:
            exit("\n\x1b[32;1m(\x1b[31;1m!\x1b[32;1m) \x1b[31;1mINGET DOSA COKK...")

