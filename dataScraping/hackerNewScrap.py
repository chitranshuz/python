import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
http_page = BeautifulSoup(response.text, 'html.parser')


links = http_page.select('.titleline')
score = http_page.select('.subtext')


def create_custom_hn(links, score):
    hn = {}
    for idx, items in enumerate(links):
        if bool(score[idx].select('.score')):

            # URLs and name
            filter_tag = links[idx].find("a", attrs={"class": None})
            title = filter_tag.getText()
            urls = filter_tag.get('href')

            # points
            filter_score = score[idx].select('.score')
            points = filter_score[0].text.replace(" points", "")

            if int(points) > 300:
                hn[points] = []
                hn[points].append(f"{title}: {urls}")
    return hn


blog_list = create_custom_hn(links, score)
pprint.pprint(blog_list)
