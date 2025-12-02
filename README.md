Judul Program: 
Kalkulator Sederhana

Pendahuluan: 
Program ini adalah aplikasi kalkulator sederhana yang berjalan pada terminal/command prompt.
Pengguna dapat memasukkan dua angka dan memilih jenis operasi yang ingin digunakan. Program kemudian akan menampilkan hasil perhitungan.Tujuan pembuatan aplikasi ini adalah untuk melatih dasar-dasar pemrograman Python, seperti fungsi, input/output, dan percabangan.

Fitur Utama:
- Melakukan operasi penjumlahan (tambah)
- Melakukan operasi pengurangan (kurang)
- Melakukan operasi perkalian (kali)
- Melakukan operasi pembagian, termasuk menangani error pembagian dengan nol
- Menyediakan menu interaktif yang memudahkan pengguna memilih operasi
- Meminta input dua angka dan langsung menampilkan hasil perhitungan

# Panduan Instalasi
Pastikan Python sudah terinstal (program menggunakan Python 3.13.7)

Clone repository:
git clone <https://github.com/JessicaTamunu/KalkulatorProject.git>

Masuk ke folder project
cd KalkulatorProject

# Panduan Menjalankan Program
Jalankan file Python utama:
python Kalkulator.py

Program akan menampilkan menu:

=== KALKULATOR SEDERHANA ===
1. Tambah
2. Kurang
3. Kali
4. Bagi
Lalu pengguna memasukkan angka dan hasil akan muncul.

# Dokumentasi Teknis
![GAMBAR FLOWCHART](<FLOWCHART.png>)

# Penjelasan
Flowchart tersebut menggambarkan alur kerja sebuah program kalkulator sederhana yang dapat melakukan empat operasi dasar, yaitu penjumlahan, pengurangan, perkalian, dan pembagian. Proses dimulai dari simbol “Mulai”, lalu program menampilkan menu yang berisi pilihan operasi matematika. Pengguna kemudian diminta memilih salah satu operasi dengan memasukkan angka 1 sampai 4. Setelah itu, program meminta dua input angka, yaitu angka pertama dan angka kedua, yang akan digunakan sebagai operand dalam proses perhitungan.

Setelah mendapatkan kedua angka, program memasuki tahap percabangan berdasarkan pilihan operasi. Jika pengguna memilih penjumlahan, maka program akan menghitung nilai a + b. Jika memilih pengurangan, program akan memproses a – b. Apabila pilihan adalah perkalian, hasil yang dihitung adalah a × b. Namun, khusus untuk pembagian, program harus memastikan bahwa angka kedua (b) tidak bernilai nol. Oleh karena itu, flowchart memberikan percabangan tambahan untuk memeriksa apakah b sama dengan nol. Jika b bernilai nol, program menampilkan pesan kesalahan bahwa pembagian tidak dapat dilakukan. Jika b bukan nol, maka perhitungan a ÷ b dilakukan seperti biasa.

Setelah operasi selesai, apa pun jenis hasilnya—baik angka maupun pesan error—program akan menampilkannya kepada pengguna. Pada tahap akhir, flowchart menunjukkan bahwa proses berakhir dengan simbol “Selesai”. Secara keseluruhan, flowchart ini menjelaskan dengan jelas bagaimana sebuah kalkulator sederhana bekerja, mulai dari input, pemilihan operasi, pengecekan kondisi khusus, hingga menampilkan hasil kepada pengguna.

