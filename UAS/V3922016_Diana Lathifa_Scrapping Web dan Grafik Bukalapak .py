#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests  # Impor modul requests untuk melakukan permintaan HTTP
import csv  # Impor modul csv untuk memanipulasi file CSV

key = input('masukkan keyword :')  # Meminta input kata kunci dari pengguna
#bisa masukkan key nya sandal

write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))  # Membuka file CSV baru dengan nama file sesuai dengan kata kunci yang dimasukkan
header = ['Nama', 'Harga', 'Alamat']  # Menentukan header file CSV
write.writerow(header)  # Menulis header ke dalam file CSV

url = 'https://api.bukalapak.com/multistrategy-products'  # URL API untuk mengambil data produk
count = 0  # Inisialisasi variabel untuk menghitung jumlah produk

for page in range(1, 3):  # Melakukan pengulangan untuk mengambil beberapa halaman data
    parameter = {
        'keywords': 'hijab',
        'limit': 50,
        'offset': 50,
        'facet': True,
        'page': 2,
        'shouldUseSeoMultistrategy': False,
        'isLoggedIn': False,
        'show_search_contexts': True,
        'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg3MTUyMDAzLCJuYmYiOjE2ODcxNDQwMjMsImlhdCI6MTY4NzE0NDAyMywianRpIjoibHdrc0MyT0lNQWtzM2w5ZGpRV3N3USIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.Rw9r0lXHOkJ5-4aMmGsDh43bzTHf835-zbgi7SJuYwSygbqG4f9A-xXgB0CX7WM-vPyWlcsanaYvhzuew8Hov5sdrPBtJV6WMLdbrzWE1wsvBRnBU2OE4Zc5jVP8vhCOMRCZnMS8xKyCUOeiAPq4YqoYdHbsswUYAON1m3FquzP6hug1mufCaJpy-DShDLSK68vEf0-a9_mwoD3YVCHdDEwFGx-vZQYcFBSSqMkq3D2CsG2dgSLo1Wg84Amsh7LDJeaWdS0io8zduNk0RkbwGlcYjWRuaAVN_XH40tvBK27DCCdg_0ZeWF11P_H1vCCOzZqmjx0eaqzEEojgsRzO6w'
        # Access token untuk otentikasi
    }  # Menentukan parameter untuk permintaan API

    r = requests.get(url, params=parameter).json()  # Mengirim permintaan GET ke API dan mengambil respons dalam format JSON

    products = r['data']  # Mengambil data produk dari respons

    for p in products:  # Melakukan pengulangan untuk setiap produk
        nama = p['name']  # Mengambil nama produk
        harga = p['price']  # Mengambil harga produk
        alamat = p['store']['address']['city']  # Mengambil alamat toko

        count += 1  # Menambah jumlah produk

        print('No:', count, 'nama:', nama, 'harga:', harga, 'alamat', alamat)  # Menampilkan informasi produk di layar

        write = csv.writer(open('hasil/{}.csv'.format(key), 'a', newline=''))  # Membuka file CSV dalam mode append
        data = [nama, harga, alamat]  # Membuat data produk
        write.writerow(data)  # Menulis data produk ke dalam file CSV


# In[20]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/hijab.csv'.format(key), 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Mengabaikan header
    for row in reader:
        data.append(row)

# Mengambil kolom harga
harga = [float(row[1]) for row in data]

# Mengatur posisi x pada sumbu x
posisi_x = range(1, len(harga) + 1)

# Membuat line chart
plt.plot(posisi_x, harga)
plt.xlabel('Nomor Produk')
plt.ylabel('Harga')
plt.title('Line Chart Harga Produk')
plt.savefig('hasil/Line chart.jpg', format='jpg')
plt.show()


# In[21]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/hijab.csv'.format(key), 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Mengabaikan baris header
    for row in reader:
        data.append(row)

# Mengambil data alamat dan harga
alamat = [row[2] for row in data]
harga = [float(row[1]) for row in data]

# Membuat bar chart
plt.bar(alamat, harga)
plt.xlabel('Alamat')
plt.ylabel('Harga')
plt.title('Bar Chart Alamat vs Harga')

plt.xticks(rotation=90)  # Memutar label alamat agar tidak tumpang tindih
plt.tight_layout()  # Menyesuaikan layout
plt.savefig('hasil/Bar chart.jpg', format='jpg')
plt.show()  # Menampilkan grafik


# In[22]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/hijab.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Mengabaikan header
    for row in reader:
        data.append(row)

# Mengumpulkan data alamat dan harga
alamat = []
harga = []
for row in data:
    alamat.append(row[2])  # Kolom alamat
    harga.append(float(row[1]))  # Kolom harga (dikonversi ke float)

# Membuat histogram
plt.figure(figsize=(10, 6))
plt.hist(harga, bins=10, edgecolor='black')  # Ubah nilai bins sesuai kebutuhan
plt.xlabel('Harga')
plt.ylabel('Jumlah Produk')
plt.title('Histogram Harga Produk')
plt.grid(True)
plt.savefig('hasil/Histogram.jpg', format='jpg')
plt.show()


# In[23]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/hijab.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Membuat dictionary untuk menghitung jumlah harga berdasarkan alamat
harga_per_alamat = {}
for row in data:
    alamat = row[2]
    harga = int(row[1])
    if alamat in harga_per_alamat:
        harga_per_alamat[alamat] += harga
    else:
        harga_per_alamat[alamat] = harga

# Mengambil data alamat dan harga
alamat = list(harga_per_alamat.keys())
harga = list(harga_per_alamat.values())

# Membuat pie chart
plt.pie(harga, labels=alamat, autopct='%1.1f%%')
plt.title('Persentase Harga berdasarkan Alamat')

# Agar pie chart menjadi lingkaran
plt.axis('equal')  

# mencetak pie chart
plt.savefig('hasil/Pie chart.jpg', format='jpg')
plt.show()


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv('hasil/{}.csv'.format(key))

# Mendapatkan kolom 'Alamat' dan 'Harga'
alamat = data['Harga']
harga = data['Alamat']

# Membuat scatter plot
plt.scatter(harga, alamat)
plt.title('Scatter Alamat dan Harga')

# Memberikan label sumbu x dan y
plt.xlabel('Harga')
plt.ylabel('Alamat')

# Menampilkan scatter plot
plt.savefig('hasil/Scatter plot.jpg', format='jpg')
plt.show()


# In[ ]:




