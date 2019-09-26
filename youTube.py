from bs4 import BeautifulSoup
import requests
import random



def search(query):
    prev_href=""

    with requests.session() as web:
        web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0"
        r = web.get("https://www.youtube.com/results?search_query=" + query)
        soup = BeautifulSoup(r.content, "html.parser")
        ret_ = "Top three results:\n"
        datas = []
        for data in soup.select(".yt-lockup-title > a[title]"):
            if "&lists" not in data["href"]:
                if data["href"] not in datas:
                    datas.append(data)
                    result = datas
                    for r in result:
                       if len(result) == 3 and r["href"]!=prev_href:
                           prev_href=r["href"]
                           ret_ += "\n {}".format(str(r["title"])) + ":"
                           ret_ += "\nhttps://www.youtube.com{}".format(str(r["href"]))
                           ret_ += "\n\n"
    return ret_