# Laporan Praktikum - Jaringan Komputer - Week 3
## Modul 3: HTML

## Tujuan Praktikum:
1. Mahasiswa dapat menginvestigasi cara kerja protokol HTTP menggunakan Wireshark.

## Alat & Bahan yang digunakan:
1. Wireshark
2. Browser (Edge)
3. Jaringan Internet

## Apa itu HTTP:
HTTP (Hypertext Transfer Protocol) adalah protokol komunikasi utama yang digunakan untuk mengirimkan dan menerima data di jaringan World Wide Web (WWW). Secara sederhana, HTTP adalah "aturan bahasa" yang memungkinkan web browser (seperti Chrome atau Firefox) dan web server (tempat website disimpan) untuk saling berkomunikasi.

#### 1. Basic HTTP GET/response interaction
1. Langkah 1: Buka browser web dan jalankan aplikasi Wireshark.
2. Langkah 2: Masukkan filter "http" pada kolom filter di Wireshark agar hanya paket HTTP yang ditampilkan.
3. Langkah 3: Akses URL target (contoh: http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html).
4. Langkah 4: Hentikan pengambilan paket (stop capture) setelah halaman berhasil dimuat sepenuhnya.
5. Langkah 5: Analisis pesan GET (permintaan dari browser) dan OK (tanggapan dari server) untuk melihat struktur header dasarnya.

>[image/Basic HTTP GET response interaction.png]

**Analisis:**
>[1. Analisis Pesan HTTP GET (Packet No. 8878)]
> Ini adalah pesan yang dikirim oleh browser kamu untuk meminta file.
> Metode HTTP: Menggunakan metode GET, yang digunakan untuk mengambil data dari server tanpa mengubah data tersebut
> URI (Uniform Resource Identifier): File yang diminta adalah /wireshark-labs/HTTP-wireshark-file1.html.
> Header Penting:
>> Host: Menunjukkan alamat server tujuan, yaitu gaia.cs.umass.edu.
>> User-Agent: Menginformasikan server tentang jenis browser dan sistem operasi yang kamu gunakan (dalam gambar terlihat menggunakan Chrome di Windows 10).
>> Accept-Language: Memberitahu server bahwa browser lebih menyukai konten dalam bahasa Inggris (en-US).

>[2. Analisis Pesan HTTP Response (Packet No. 9059)]
> Ini adalah balasan dari server setelah menerima permintaan GET tadi.
> Status Code: 200 OK. Ini menandakan bahwa server berhasil menemukan file yang diminta dan sedang mengirimkannya.
> Content-Type: Terdeteksi sebagai text/html, yang berarti data yang dikirim adalah dokumen web (HTML).
> Data Payload: Jika kamu melihat bagian Packet Bytes di Wireshark, kamu akan melihat kode HTML asli dari file tersebut (misalnya tag <html>, <body>, dsb).

>[3. Analisis Alamat IP dan Protokol Transport]
> IP Source & Destination: Terlihat klien menggunakan IP 192.168.1.12 dan server berada di IP 128.119.245.12.
> Enkapsulasi TCP: Sebelum pesan HTTP dikirim, terlihat pada panel detail bahwa HTTP berjalan di atas TCP (Transmission Control Protocol) menggunakan port 80. Hal ini menjamin bahwa data HTML sampai dengan utuh dan urut ke browser kamu.

#### 2. HTTP CONDITIONAL GET/response interaction
#### 3. Retrieving Long Documents
#### 4. HTML Documents dengan Embedded Objects
#### 5. HTTP Authentication

>[KESIMPULAN]
> 