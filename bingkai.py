import io
from PIL import Image
import requests
import cloudinary.uploader

cloudinary.config(
    cloud_name='YOUR CLOUD NAME',
    api_key='YOU API',
    api_secret='YOU SCRET'
)
import pandas as pd


def savecsv(nama):
    anjai = pd.DataFrame([[nama]])
    anjai.to_csv('url_baru.csv', mode='a', header=False)


a = pd.read_csv('url_original.csv')
row = a["img"].count()
for x in range(row):
    url_original = a['img'][x]
    response = requests.get(url_original)
    image_bytes = io.BytesIO(response.content)
    gambar1 = Image.open(image_bytes)
    ukuran = gambar1.size
    gambar2 = "bingkai.png"
    bingkai = Image.open(gambar2)
    b = bingkai.resize(ukuran)
    gambar1.paste(b, (0, 0), b)
    tipe = gambar1.format
    simpan = "gambar_temp." + tipe.lower()
    gambar1.save(simpan)
    c = cloudinary.uploader.upload(simpan)
    savecsv(c["url"])
    print("Done")
