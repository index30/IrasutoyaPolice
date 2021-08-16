from bs4 import BeautifulSoup
from logging import DEBUG, getLogger, StreamHandler, WARNING
import requests
import time

SITEMAP_URL = "https://www.irasutoya.com/sitemap.xml"

logger = getLogger(__name__)
logger.setLevel(WARNING)
# logger.addHandler(StreamHandler())


def irasutoya_crawler(src_xml):
    time.sleep(2)
    irasutoya_sitemap = requests.get(src_xml).text
    soup = BeautifulSoup(irasutoya_sitemap)
    site_tags = soup.find_all("sitemap")
    result = []
    if site_tags:
        for site_tag in site_tags:
            result.extend(irasutoya_crawler(site_tag.text))
    else:
        url_tags = soup.find_all("url")
        for url_tag in url_tags:
            result.append(url_tag.find("loc").text)
    return result


def find_img_names(img_links_list):
    result = []
    for img_link in img_links_list:
        time.sleep(2)
        img_page = requests.get(img_link).text
        soup = BeautifulSoup(img_page)
        img_src = soup.find('div', class_='separator')
        if img_src:
            img_name_src = img_src.find("img")
            if img_name_src:
                img_name = img_name_src.attrs['src'].split("/")[-1]
                title_src = soup.find('div', class_='title')
                if title_src:
                    title_name_src = title_src.find("h2")
                    if title_name_src:
                        title_name = title_name_src.text.strip()
                        result.append((title_name, img_name))
    return result
