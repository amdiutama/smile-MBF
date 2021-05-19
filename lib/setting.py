import shutil
import data
import lib
import random
import asyncio
from lib.crack import *
#×××××××××××××××××××××××××××××××××××××××××××××××××××××
try: shutil.rmtree("data/__pycache__")
except: pass
try: shutil.rmtree("lib/__pycache__")
except: pass
#×××××××××××××××××××××××××××××××××××××××××××××××××××××
def seting(use, cookies):
        fas = []
        con = 0
        acak = random.choice(["sayang","indonesia","doraemon","rahasia","bangsat"])
        for i in range(len(use[0][0])):
            try:
                sandi = use[0][1][con].split(" ")
                fas.append(proses(use[0][0][con], (sandi[0]+"123").title()))
                fas.append(proses(use[0][0][con], (sandi[0]+"12345").title()))
                try:
                    fas.append(proses(use[0][0][con], (sandi[1]+"123").title()))
                    fas.append(proses(use[0][0][con], (sandi[0]+sandi[1]).lower()))
                except IndexError:
                    fas.append(proses(use[0][0][con], acak))

            except:
                    pass

            con += 1

        run = asyncio.get_event_loop()
        run.run_until_complete(multi(use, fas))
        pil = input("\n\x1b[32;1m(\x1b[36;1mKELUAR\x1b[32;1m) \x1b[36;1m(\x1b[32;1mY\x1b[30;1m/\x1b[32;1mT) \x1b[36;1m> \x1b[32;1m")
        if pil == "Y" or pil == "y":
               exit("\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mTERIMA KASIH")
        else:
               data.run.menu(cookies).menuP()
        run.close()
