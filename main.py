# DDP LAB-2
print("NIM\t\t : 0110220045")
print("Nama\t : Evry Nazyli Ciptanto")
print("Program Studi Teknik Informatika - TI08\n")
# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print("SOAL 1 - Mencetak bilangan")
# set variable a = 100
a = 100
# melakukan perulangan dengan nilai awal = 0, nilai akhir = 100, dan selang = 2
for i in range(0, a, 2):
  # nilai i akan bernilai 0,2,4, ..., 98, 100.
  #jadi semisal (a = 100 dan i = 0 maka x =100), (a=100 dan i=2, maka x=98), dan seterusnya.
  j=a-i
  #fungsi end = untuk meberikan jarak antar 1 bilangan dengan bilangan yg lain
  print(j,end=' ')




# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
print("\n\nSOAL 2 - Menghitung rata-rata")
# mendapatkan nilai input dari pengguna dan menyimpan ke variabel lotsOfData
lotsOfData = int(input('Masukkan banyaknya angka : '));
#membuat variabel total dengan set nilai awal 0
total = 0
#melakukan perulangan sesuai nilai variabel lotsOfData 
for i in range(lotsOfData):
  #mendapatkan nilai input, memakai float agar input user bisa bilangan decimal
  #format fungsi untuk penggabungan string dan number,
  #i+1, karena i index dimulai dari 0, maka perlu +1 untuk mendapatkan nomor yg dimulai dari 1,
  c = float(input('Masukkan angka ke-{0} : '.format(i+1)));
  #update variabel total menjadi nilai dari input, increment input
  total=total + c

# menhitung rata" total didapat dari jumlah total semua data, lotsOfData yaitu banyaknya data, kemudian di simpan di variabel avg
avg = total /lotsOfData
# tampilkan nila hasil variabel avg ke layar
print("Rata - Rata : ", avg)

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("\nSOAL 3 - Mencetak Persegi")
# mendapatkan nilai input dari pengguna dan menyimpan ke variabel integers
integers = int(input('Masukkan sebuah bilangan bulat : '));

# melakukan looping sebanyak data input
for i in range(integers):
  # akan melakukan cetak "#" ke kanan sebanyak data integers. proses akan di ulang sebanyak nilai data variabel integers
  print("# "*integers)

