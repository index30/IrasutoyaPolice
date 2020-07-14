from bs4 import BeautifulSoup
from pathlib import Path
import pickle
import requests
import sys
import time
import urllib.request as urlreq

sys.path.append(Path(Path(__file__).resolve().parents[1], 'secrets').as_posix())
# URL格納先
import secret_assets

def scraping_imgname(imgs_link):
    time.sleep(5)
    html_doc = requests.get(imgs_link).text
    soup = BeautifulSoup(html_doc, 'lxml')
    img_tags =soup.select('div.boxim > a')
    imgs_list = []

    # 特定のページから画像名をリストで取得
    for tag in img_tags:
        img_src = Path(tag.contents[0].contents[0].split("\"")[1])
        if img_src.suffix in ['.jpg', '.png']:
            imgs_list.append(img_src.name)

    # 次ページのリンク
    next_page = soup.find('a', class_='blog-pager-older-link')
    if next_page:
        next_page_link = next_page.attrs['href']
        return imgs_list + scraping_imgname(next_page_link)
    else:
        return imgs_list
    
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        imgs_link_arg = sys.argv[1]
    else:
        imgs_link_arg = secret_assets.SECRET_SINGLE_URL
    imgs_list = scraping_imgname(imgs_link_arg)
    print("The number of images: {}".format(len(imgs_list)))
    
    # If you want to save image list
    # with open('irasutoya.pkl', 'wb') as w:
    #     pickle.dump(imgs_list, w)
        
    # with open('irasutoya.pkl', 'rb') as r:
    #     pickle_list = pickle.load(r)
    #     print("Pickle: {}".format(len(pickle_list)))