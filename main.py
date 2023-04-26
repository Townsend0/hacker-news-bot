import bs4
import requests

soup = bs4.BeautifulSoup(requests.get("https://news.ycombinator.com/").text, "lxml")
soup = soup.find_all("span", class_ = "score")
soup = { int(soup[a].string.split(" ")[0]): soup[a].get("id").split("_")[1] for a in range(len(soup)) }
id = soup[max(soup)]

soup = bs4.BeautifulSoup(requests.get("https://news.ycombinator.com/").text, "lxml")
soup = soup.find("tr", class_ = "athing", id = id).find("span", class_ = "titleline").find("a").get("href")

print(soup)
    