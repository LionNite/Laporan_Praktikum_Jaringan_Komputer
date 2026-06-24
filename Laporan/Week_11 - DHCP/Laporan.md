# Laporan Praktikum - Jaringan Komputer - Week 11
Modul 11: DHCP

## Pengantar
DHCP atau Dynamic Host Configuration Protocol digunakan untuk memberikan konfigurasi jaringan secara otomatis kepada host. Konfigurasi tersebut meliputi alamat IP, subnet mask, default gateway, DNS server, dan masa sewa alamat IP. Alur umum DHCP dikenal sebagai DORA, yaitu Discover, Offer, Request, dan Acknowledgement.

---

## Langkah Percobaan

### MacOS

1. Cek nama interface aktif di Wireshark melalui `Capture > Options`.
2. Jika interface adalah `en0`, jalankan perintah berikut di terminal:

```bash
sudo ipconfig set en0 none
```

3. Mulai capture Wireshark pada interface tersebut.
4. Jalankan perintah berikut:

```bash
sudo ipconfig set en0 dhcp
```

5. Tunggu beberapa detik, lalu hentikan capture.
6. Gunakan filter berikut:

```text
dhcp
```

Jika filter `dhcp` tidak menampilkan paket, gunakan:

```text
bootp
```

### Linux

```bash
sudo ip addr flush en0
sudo dhclient -r
sudo dhclient en0
```

### Windows

```bat
ipconfig /release
ipconfig /renew
```

Jika capture langsung tidak berhasil, gunakan trace `dhcp-wireshark-trace1-1.pcapng` dari file berikut:

```text
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip
```
