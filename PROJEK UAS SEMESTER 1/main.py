from data import indeks

riwayat_konversi = []

# Menggunakan fungsi
def konversi_suhu(suhu, suhu_asal, suhu_tujuan) :
    hasil_konversi = suhu

    if suhu_asal == 'c' :
        if suhu_tujuan == 'r' :
            hasil_konversi = (suhu * 4 / 5)
        elif suhu_tujuan == 'f' :
            hasil_konversi = (suhu * 9 / 5) + 32
        elif suhu_tujuan == 'k' :
            hasil_konversi = (suhu + 273)
        else:
            hasil_konversi = suhu
    elif suhu_asal == 'r' :
        if suhu_tujuan == 'c' :
            hasil_konversi = (suhu * 5 / 4)
        elif suhu_tujuan == 'f' :
            hasil_konversi = (suhu * 9 / 4) + 32
        elif suhu_tujuan == 'k' :
            hasil_konversi = (suhu * 5 / 4) + 273
        else:
            hasil_konversi = suhu
    elif suhu_asal == 'f' :
        if suhu_tujuan == 'c' :
            hasil_konversi = (5 / 9 * (suhu - 32))
        elif suhu_tujuan == 'r' :
            hasil_konversi = (4 / 9 * (suhu - 32))
        elif suhu_tujuan == 'k' :
            hasil_konversi = (5 / 9 * (suhu - 32) + 273)
        else:
            hasil_konversi = suhu
    elif suhu_asal == 'k' :
        if suhu_tujuan == 'c' :
            hasil_konversi = (suhu - 273)
        elif suhu_tujuan == 'f' :
            hasil_konversi = ((9 / 5) * (suhu - 273) + 32)
        elif suhu_tujuan == 'r' :
            hasil_konversi = (4 / 5 * (suhu - 273))
        else:
            hasil_konversi = suhu

    riwayat_konversi.append((suhu, suhu_asal, hasil_konversi, suhu_tujuan))
    return hasil_konversi

print('_' * 62)
print('*' * 62, '')
print('{:^62}'.format(' Kode Satuan Skala Suhu'))
print('{:^62}'.format('*******\n'))

# Library untuk menambahkan waktu
import datetime
now = datetime.datetime.now()
print('| Tanggal :', now.strftime('{:>46} |'.format('%d-%m-%Y')))
print('| Waktu   :', now.strftime('{:>48} |'.format('%H:%M:%S')))
print('*' * 62)
print('_' * 62, '\n')

# Untuk membuat tabel nama suhu dan kode suhu pada dictionary indeks
for i in indeks :
    print('||Satuan Suhu :', i, '{:>23}'.format('\t     Kode Suhu : \t'), indeks[i], '||')
print('_' * 62)
print('*' * 62)

# Perulangan untuk konfirmasi ingin melanjutkan konversi atau tidak
while True :    
    # inputan
    print()
    print('=' * 62)
    suhu = float(input('\nMasukkan Suhu (Angka)       : '))
    suhu_asal = input('Masukkan Kode Suhu Asal     : ').lower()
    suhu_tujuan = input('Masukkan Kode Suhu Tujuan   : ').lower()
    hasil_konversi = konversi_suhu(suhu, suhu_asal, suhu_tujuan)
    print('-' * 62)
    print()
    if suhu_asal != suhu_tujuan:
        asal = [x for x, y in indeks.items() if y == suhu_asal][0]
        tujuan = [x for x, y in indeks.items() if y == suhu_tujuan][0]
        print(suhu, '°', asal, '---Hasilnya-->', hasil_konversi, '°', tujuan)
    else:
        print('Hasil konversi sama dengan nilai input.')
    
    # Persetujuan ingin melanjutkan atau tidak
    print()
    print('=' * 62)
    konfirmasi = input('Apakah Ingin Melanjutkan Konfersi Suhu? [Y/N] : ')
    if konfirmasi == 'y' or konfirmasi == 'Y' :
        pass
    else:
        # Menampilkan riwayat dari hasil konversi yang sudah dijalankan
        print('\nRiwayat Konversi:')
        print('_' * 62)
        print('  Suhu Asal', ' Kode Asal', ' Hasil Konversi', ' Kode Tujuan')
        print('_' * 62)
        for riwayat in riwayat_konversi:
            suhu_asal, kode_asal, hasil_konversi, kode_tujuan = riwayat
            suhu_asal_konversi = str(suhu_asal) + '° ' + [x for x, y in indeks.items() if y == kode_asal][0]
            suhu_hasil_konversi = str(hasil_konversi) + '° ' + [x for x, y in indeks.items() if y == kode_tujuan][0]
            print('| ', suhu_asal_konversi, kode_asal, suhu_hasil_konversi, '|', kode_tujuan, '|')
        break

