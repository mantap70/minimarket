def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    biaya = 10000

    if berat > 5:
        biaya += 5000
    
    if jarak > 10:
        biaya += 8000

    if express:
        biaya += 20000

    if member:
        biaya *= 0.9

    return int(biaya)

print(hitung_biaya_pengiriman(6, 15, express=True, member=True))