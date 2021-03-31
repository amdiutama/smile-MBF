from bs4 import BeautifulSoup as bs
import requests
import data
import shutil
from time import sleep

class menu:
     def __init__(self, cookies):
            try: shutil.rmtree("data/__pycache__")
            except: pass
            login, title, ip = data.login.smile(cookies).login()
            self.cookies = cookies
            self.title = title
            self.ip = ip

     def menuP(self):
           data.logo.banner()
           total = requests.get("https://ase-xc.com/getuser.php", headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36"}).json()
           print(f' \x1b[36;1mTOTAL \x1b[32;1m{len([i["ip"] for i in total["data"]])} \x1b[36;1mPENGGUNA AKTIF \x1b[32;1m!!\n \x1b[36;1mWELCOME \x1b[32;1m{self.title} \x1b[36;1m!!\n         \x1b[32;1m(\x1b[37;1m{self.ip}\x1b[32;1m)\n\x1b[36;1m─────────────────────────\n\x1b[32;1m(\x1b[36;1m1\x1b[32;1m) \x1b[36;1mCIPOK ID TEMAN\n\x1b[32;1m(\x1b[36;1m2\x1b[32;1m) \x1b[36;1mCIPOK ID TEMAN \x1b[32;1m-> \x1b[36;1mTEMAN\n\x1b[32;1m(\x1b[36;1m3\x1b[32;1m) \x1b[36;1mCIPOK ID PENCARIAN\n\x1b[32;1m(\x1b[36;1m4\x1b[32;1m) \x1b[36;1mCIPOK ID GRUP\n\x1b[32;1m(\x1b[36;1m5\x1b[32;1m) \x1b[36;1mTENTANG SAYA\n\x1b[32;1m(\x1b[31;1m0\x1b[32;1m) \x1b[37;1mKELUARIN DONG')
           pil = input("\x1b[36;1m>>>\x1b[32;1m| \x1b[33;1m")
           if pil == "1":
                 count = int(input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mJUMLAH     \x1b[30;1m: \x1b[32;1m"))
                 next = "/friends/center/friends/"
                 data.getuser.users(self.cookies).getUser(count, next)

           elif pil == "2":
                 next = input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mURL TEMAN  \x1b[30;1m: \x1b[32;1m").replace("https://m.facebook.com","")
                 count = int(input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mJUMLAH     \x1b[30;1m: \x1b[32;1m"))
                 data.getuser.users(self.cookies).getUser(count, next)

           elif pil == "3":
                 url = "https://m.facebook.com/search/people/?q="
                 nama = input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mNAMA       \x1b[30;1m: \x1b[32;1m")
                 count = int(input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mJUMLAH     \x1b[30;1m: \x1b[32;1m"))
                 data.getuser.users(self.cookies).getUser(count, (url+nama))

           elif pil == "4":
                 idgrup = input("\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mURL GRUP   \x1b[30;1m: \x1b[32;1m").split("/")
                 next = f"/browse/group/members/?id={idgrup[4]}&start=0&listType=list_nonfriend_nonadmin&ref=group_browse"
                 data.getuser.users(self.cookies).getGrup(next)

           elif pil == "5":
                 data.logo.banner()
                 print("\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mNAMA       \x1b[30;1m: \x1b[37;1mMUHAMMAD FATHUL\n\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mALAMAT     \x1b[30;1m: \x1b[37;1mCILEGON\x1b[32;1m-\x1b[37;1mBANTEN\n\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mFACEBOOK   \x1b[30;1m: \x1b[32;1m(\x1b[37;1mfacebook\x1b[32;1m)\x1b[37;1m/muhammad.fathul.5055\n\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mINSTAGRAM  \x1b[30;1m: \x1b[32;1m(\x1b[37;1minstagram\x1b[32;1m)\x1b[37;1m/arrokm.1\n\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mGITHUB     \x1b[30;1m: \x1b[32;1m(\x1b[37;1mgithub\x1b[32;1m)\x1b[37;1m/ArroKM\n\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mSUPPORT BY \x1b[30;1m: \x1b[37;1mXIUZCODE TEAM\n\x1b[36;1m(\x1b[32;1m+\x1b[36;1m) \x1b[32;1mFOLLOW JIKA BERKENAN \x1b[36;1m:v")
                 pi = input("\x1b[32;1m(\x1b[36;1mENTER\x1b[32;1m) \x1b[36;1mUNTUK KEMBALI \x1b[32;1m>> ")
                 self.menuP()

           elif pil == "0":
                 exit("\x1b[32;1m(\x1b[31;1m!\x1b[32;1m) \x1b[31;1mINGET DOSA COKK...")
           else: exit("\x1b[32;1m(\x1b[31;1m!\x1b[32;1m) \x1b[31;1mPILIHAN TIDAK ADA!!")
