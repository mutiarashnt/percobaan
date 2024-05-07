print('Kalkulator Sederhana')

print('\n')

print('Operasi Matematika')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Keluar')

def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b

print('\n')

pilihan = int(input('Pilih Operasi : '))
bilangan1 = int(input('Masukkan Bilangan Pertama : '))
bilangan2 = int(input('Masukkan Bilangan Kedua : '))


if pilihan == 1:
    print('Hasil Penjumlahan = ', penjumlahan(bilangan1,bilangan2))
elif pilihan == 2:
    print('Hasil Pengurangan = ', pengurangan(bilangan1,bilangan2))
elif pilihan == 3:
    print('Hasil Perkalian = ', perkalian(bilangan1,bilangan2))
elif pilihan == 4:
    print('Hasil Pembagian = ', pembagian(bilangan1,bilangan2))
elif pilihan == 5:
    break
else:
    print('Terimakasih telah menggunakan kalkulator sederhana')





