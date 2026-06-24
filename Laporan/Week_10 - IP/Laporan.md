# # Laporan Praktikum - Jaringan Komputer - Week 10
Modul 10: IP

## Pengantar

Modul IP membahas datagram IPv4, proses traceroute, fragmentasi IP, dan contoh paket IPv6. Traceroute digunakan karena setiap paket memiliki nilai TTL yang berbeda. Ketika TTL habis di router, router akan mengirim pesan ICMP TTL exceeded kembali ke host asal.

---

## Langkah Percobaan

### Bagian 1 - IPv4 Dasar

1. Jalankan Wireshark dan mulai capture pada interface aktif.
2. Jalankan perintah berikut di terminal MacOS atau Linux:

```bash
traceroute gaia.cs.umass.edu 56
```

3. Jalankan traceroute kedua dengan ukuran paket lebih besar:

```bash
traceroute gaia.cs.umass.edu 3000
```

4. Hentikan capture Wireshark.
5. Gunakan filter berikut untuk melihat paket UDP dan ICMP:

```text
udp || icmp
```

6. Jika menggunakan Windows, gunakan perintah berikut untuk bagian IPv4 dasar:

```bat
tracert gaia.cs.umass.edu
```

7. Jika capture langsung tidak berhasil, gunakan trace `ip-wireshark-trace1-1.pcapng` dari file berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```

### Bagian 2 - Fragmentasi

1. Hapus semua display filter.
2. Urutkan paket berdasarkan kolom Time.
3. Cari datagram dari traceroute ukuran 3000 byte.
4. Amati field `Identification`, `Flags`, `Fragment Offset`, dan `Total Length` pada header IPv4.

### Bagian 3 - IPv6

1. Buka file trace `ip-wireshark-trace2-1.pcapng`.
2. Amati paket DNS AAAA untuk domain `youtube.com`.
3. Perhatikan perbedaan field IPv6 dibanding IPv4, seperti `Traffic Class`, `Flow Label`, `Payload Length`, `Next Header`, dan `Hop Limit`.

---