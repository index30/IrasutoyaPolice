# IrasutoyaPolice
いらすとや警察

## What is this ?
スライド内に[いらすとや](https://www.irasutoya.com/)の素材を何点使用しているかを調査するCLI。  
商用利用の上限である20点を越えた素材を使用している場合、下記の警告が飛ぶ。
```
If this slide is for commercial purpose, you must keep within 20 irasutoya products
```

## How to use ?
```
$ git clone https://github.com/index30/IrasutoyaPolice.git
$ python3 -m venv IrasutoyaPolice
$ cd IrasutoyaPolice
$ source bin/activate
$ pip3 install -r requirements.txt
$ python3 src/main.py (YOUR PPT PATH)
```

