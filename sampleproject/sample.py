import urllib.request as req

import pandas as pd

# ファイルのダウンロード
url = (
    "https://raw.githubusercontent.com"
    + "/kujirahand/book-mlearn-gyomu/master/src/ch2/iris"
    + "/iris.csv"
)

savefile = "iris.csv"
req.urlretrieve(url, savefile)
print("保存しました")

# ダウンロードしたファイルの内容を表示
csv = pd.read_csv(savefile, encoding="utf-8")
print(csv)
