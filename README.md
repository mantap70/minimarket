# Hitung Biaya Pengiriman

## Deskripsi
Program ini digunakan untuk menghitung biaya pengiriman berdasarkan beberapa faktor, yaitu berat paket, jarak pengiriman, opsi pengiriman express, dan status keanggotaan pelanggan.

## Struktur Kode
Fungsi utama dalam program ini adalah `hitung_biaya_pengiriman()`, yang memiliki parameter berikut:
- `berat`: Berat paket dalam satuan kilogram (kg).
- `jarak`: Jarak pengiriman dalam satuan kilometer (km).
- `express`: Boolean (`True/False`) yang menunjukkan apakah pengiriman menggunakan layanan ekspres.
- `member`: Boolean (`True/False`) yang menunjukkan apakah pelanggan adalah anggota (member) yang mendapatkan diskon.

### Aturan Perhitungan Biaya
1. Biaya dasar pengiriman adalah **10.000**.
2. Jika berat paket lebih dari **5 kg**, biaya bertambah **5.000**.
3. Jika jarak pengiriman lebih dari **10 km**, biaya bertambah **8.000**.
4. Jika opsi ekspres dipilih (`express=True`), biaya bertambah **20.000**.
5. Jika pelanggan adalah anggota (`member=True`), diberikan diskon **10%** dari total biaya.

## Implementasi Kode
Berikut adalah implementasi kode Python:

```python
def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    biaya = 10000

    if berat > 5:
        biaya += 5000

    if jarak > 10:
        biaya += 8000

    if express:
        biaya += 20000

    if member:
        biaya *= 0.9  # Diskon 10%

    return int(biaya)

# Contoh penggunaan
print(hitung_biaya_pengiriman(6, 15, express=True, member=True))
```

## Contoh Penggunaan
Jika kita memanggil fungsi dengan parameter berikut:
```python
hitung_biaya_pengiriman(6, 15, express=True, member=True)
```
Maka perhitungan biaya adalah sebagai berikut:
- Biaya dasar: **10.000**
- Berat > 5 kg: **+5.000** → **15.000**
- Jarak > 10 km: **+8.000** → **23.000**
- Express: **+20.000** → **43.000**
- Diskon member (10% dari 43.000): **43.000 × 0.9 = 38.700**

Sehingga output dari program adalah:
```python
38700
```

## Kesimpulan
Program ini membantu dalam menghitung biaya pengiriman dengan mempertimbangkan beberapa faktor seperti berat, jarak, layanan ekspres, dan status keanggotaan. Dengan cara ini, pengguna dapat dengan mudah mengetahui biaya total sebelum melakukan pengiriman.

