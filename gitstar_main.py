import requests
import time
from requests.auth import HTTPBasicAuth


class Gitstar():
    def __init__(self, url=""):
        self.NAME = "dianbaer"
        self.PASSWORD = "dianbaer111"
        self.GITNAME = "xp892124@sina.com"
        self.GITPASSWORD = "xp1986124A"

    def loginGitStar(self):
        r = requests.post("http://gitstar.top:88/api/user/login",
                          params={'username': self.NAME, 'password': self.PASSWORD})
        return r.headers['Set-Cookie']

    def getGitStarList(self):
        cookie = self.loginGitStar()
        url = "http://gitstar.top:88/api/users/{}/status/recommend".format(self.NAME)
        response = requests.get(url, headers={'Accept': 'application/json', 'Cookie': cookie})
        jsn = response.json()
        list = []
        for obj in jsn:
            list.append(obj['Repo'])
        return list

    def star(self, url):
        global AUTH
        AUTH = HTTPBasicAuth(self.GITNAME, self.GITPASSWORD)
        requests.put("https://api.github.com/user/starred/" + url
                     , headers={'Content-Length': '0'}
                     , auth=AUTH)


GS = Gitstar()
urls = GS.getGitStarList()
for url in urls:
    GS.star(url)
    print("Stared! -->{}".format(url))
    time.sleep(5.0)
