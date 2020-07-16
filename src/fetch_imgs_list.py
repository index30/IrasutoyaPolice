from bs4 import BeautifulSoup
import requests
import sys
import time
import xml.etree.ElementTree as ET

SITEMAP_URL = "https://www.irasutoya.com/sitemap.xml"

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
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        sitemap_url = sys.argv[1]
    else:
        sitemap_url = SITEMAP_URL
    
    result = irasutoya_crawler(sitemap_url)
    print("result size {}".format(len(result)))