from bs4 import BeautifulSoup
from pathlib import Path
import requests
import sys
import urllib.request as urlreq

sys.path.append(Path(Path(__file__).resolve().parents[1], 'secrets').as_posix())
# URL格納先
import secret_assets

html_doc = requests.get(secret_assets.SECRET_SINGLE_URL).text
soup = BeautifulSoup(html_doc, 'lxml')
real_page_tags =soup.select('div.boxim > a')

# 特定のページから画像名をリストで取得
# 単一のページのみ対応。次のページに遷移などは課題。
count = 0
for tag in real_page_tags:
    img_src = Path(tag.contents[0].contents[0].split("\"")[1])
    if img_src.suffix in ['.jpg', '.png']:
        print(img_src.name)
        count += 1

print("Count: {}".format(count))
