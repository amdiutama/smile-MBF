from bs4 import BeautifulSoup as bs
import requests, re
import lib
import shutil

class users:
     def __init__(self, cookies):
           try: shutil.rmtree("lib/__pycache__")
           except: pass
           self.cookies = cookies

     def getGrup(self, next=None):
           use = [[[],[]]]
           url = "https://m.facebook.com"
           req = requests.get(f"{url}{next}", cookies={'cookie': self.cookies})
           nama = parser = bs(req.text.encode("utf-8"), "html.parser").title.text
           print(f"               \x1b[30;1m: \x1b[32;1m{nama}")
           while True:
                grup = requests.get(f"{url}{next}", cookies={'cookie': self.cookies})
                parser = bs(grup.text.encode("utf-8"), "html.parser")
                if parser.find_all("a", class_="bd") != []:
                           div = parser.find_all("a", class_="bd")
                else:
                           div = parser.find_all("a", class_="bf")
                for i in div:
                     try:
                         id = re.findall('/?id=(.*?)&', i['href'])
                         if len(id) == 0:
                              id = re.findall('/(.*?)\\?ref=', i['href'])
                              if len(id) == 0:
                                    id = re.findall('/\\?uid=(.*?)&', i['href'])
                     except TypeError:
                          id = []
                     if len(id) == 1:
                             use[0][0].append(id[0])
                             use[0][1].append(i.text)

                if 'Lihat Selengkapnya' in str(parser):
                      next = parser.find('a', string='Lihat Selengkapnya')['href']
                else:
                      break

           print(f"\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mTOTAL USER \x1b[30;1m: \x1b[32;1m{len(use[0][1])}\n\x1b[36;1m─────────────────────────\n")
           lib.setting.seting(use, self.cookies)

     def getUser(self, count, next=None):
           use = [[[],[]]]
           status = False
           url = "https://m.facebook.com"
           while True:
               if "https://m.facebook.com/search/people/" in str(next):
                        teman = requests.get(f"{next}", cookies={'cookie': self.cookies})
                        parser = bs(teman.text.encode("utf-8"), "html.parser")
                        div = parser.find_all('a')
               else:
                        teman = requests.get(f"{url}{next}", cookies={'cookie': self.cookies})
                        parser = bs(teman.text.encode("utf-8"), "html.parser")
                        div = parser.find_all(style='vertical-align: middle')
               for i in div:
                   if i.find("a") == None:
                         x = i.find("div")
                         if x == None:
                              continue
                         else:
                              try:
                                   id = re.findall('\\?id=(.*?)&', str(i))
                                   if len(id) == 0:
                                         id = re.findall('/(.*?)\\?refid=', str(i))
                              except TypeError:
                                   id = []
                   else:
                        x = i.find("a")
                        try:
                             id = re.findall('/?id=(.*?)&', x['href'])
                             if len(id) == 0:
                                  id = re.findall('/(.*?)\\?fref=', x['href'])
                                  if len(id) == 0:
                                       id = re.findall('/\\?uid=(.*?)&', x['href'])
                        except TypeError:
                          id = []
                   if len(id) == 1:
                         use[0][0].append(id[0])
                         use[0][1].append(x.text)
                   if len(use[0][0]) >= count:
                         status = True
                         break

               if status == False:
                    if 'Lihat Teman Lain' in str(parser):
                            next = parser.find('a', string='Lihat Teman Lain')['href']
                    elif 'Lihat selengkapnya' in str(parser):
                            next = parser.find('a', string='Lihat selengkapnya')['href']
                    elif 'Lihat Hasil Selanjutnya' in str(parser):
                            next = parser.find('a', string='Lihat Hasil Selanjutnya')['href']
                    else:
                            break
               else:
                    break

           print(f"\x1b[32;1m(\x1b[36;1m*\x1b[32;1m) \x1b[36;1mTOTAL USER \x1b[30;1m: \x1b[32;1m{len(use[0][1])}\n\x1b[36;1m─────────────────────────\n")
           lib.setting.seting(use, self.cookies)

