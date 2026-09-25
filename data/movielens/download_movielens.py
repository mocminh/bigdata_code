# -*- coding: utf-8 -*-
"""Tải ml-latest-small và trích ratings.csv vào data/movielens/ (Đoạn mã 7.4)."""
import os, urllib.request, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
dich = os.path.join(HERE, "ratings.csv")
if os.path.exists(dich):
    print("Da co", dich)
else:
    zip_path = os.path.join(HERE, "ml-latest-small.zip")
    urllib.request.urlretrieve(URL, zip_path)
    with zipfile.ZipFile(zip_path) as z:
        with z.open("ml-latest-small/ratings.csv") as src, open(dich, "wb") as dst:
            dst.write(src.read())
    os.remove(zip_path)
    print("Da tai", dich)
