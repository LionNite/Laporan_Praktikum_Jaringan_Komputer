# Laporan Praktikum - Jaringan Komputer - Week 12
Modul 6: ICMP

## Pengantar

ICMP digunakan untuk mengirim pesan kontrol dan pesan kesalahan pada jaringan IP. Pada modul ini, ICMP diamati melalui perintah ping dan traceroute. Ping menghasilkan pesan ICMP Echo Request dan Echo Reply, sedangkan traceroute memanfaatkan pesan ICMP TTL exceeded dari router perantara.

---

## Langkah Percobaan Ping

1. Buka Wireshark dan mulai capture pada interface aktif.
2. Jalankan perintah ping. Pada MacOS atau Linux:

```bash
ping -c 10 www.ust.hk
```

Pada Windows:

```bat
ping -n 10 www.ust.hk
```

3. Hentikan capture setelah ping selesai.
4. Gunakan filter berikut:

```text
icmp
```

---

## Langkah Percobaan Traceroute

Pada MacOS atau Linux:

```bash
traceroute www.inria.fr
```

Pada Windows:

```bat
tracert www.inria.fr
```

Setelah selesai, hentikan capture dan gunakan filter:

```text
icmp
```

---

## Program ICMP Pinger

File program tersedia pada:

```text
code/icmp_pinger.py
```

Cara menjalankan di MacOS atau Linux:

```bash
sudo python3 code/icmp_pinger.py google.com
```

Program ini membutuhkan hak akses administrator karena raw socket ICMP biasanya tidak boleh dibuat oleh user biasa.

---

## Penjelasan Program `icmp_pinger.py`

1. Program menerima hostname dari argument terminal.
2. Hostname diubah menjadi alamat IP dengan `socket.gethostbyname()`.
3. Program membuat raw socket dengan protokol ICMP.
4. Program membentuk paket Echo Request berisi header ICMP dan payload waktu pengiriman.
5. Program mengirim paket ke host tujuan.
6. Program menunggu Echo Reply sampai batas timeout.
7. Jika balasan diterima, program menghitung RTT berdasarkan selisih waktu kirim dan waktu terima.

---