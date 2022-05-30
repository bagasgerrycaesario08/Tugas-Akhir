# Tugas-Akhir Arsitektur Jaringan Terkini

## Membuat EC2 Instance di AWS Academy

- Ketentuan :
  - Name and tags : Tugas Akhir
    - ![](ss/1.png)
  - OS Images : Ubuntu Server 22.04 LTS 64 bit
    - ![](ss/2.png)
  - Instance type : t2.medium
    - ![](ss/3.png)
  - Key pair : vockey
    - ![](ss/4.png)
  - Edit Network settings : allow SSH, allow HTTP, allow HTTPS, allow TCP port 8080, allow TCP port 8081
    - ![](ss/5.png)
    - ![](ss/6.png)
  - Configure storage : 30 GiB, gp3
    - ![](ss/7.png)

## 1. Langkah Pertama Lakukan Update

- Lakukan update dan upgrade dengan perintah :

```
sudo apt -yy update && sudo apt -yy upgrade
```

## 2. Instalasi Mininet + OpenFlow

Mininet adalah sebuah emulator jaringan yang dapat digunakan untuk membuat sebuah jaringan virtual (dapat terdiri atas host, switch, router, controller, dan link). host pada mininet menjalankan software Linux standar dan switch pada mininet mendukung protokol OpenFlow yang sangat fleksibel untuk dimodifikasi dan mendukung Software-Defined Networking (SDN).

- Unduh repositori Mininet

```
git clone https://github.com/mininet/mininet
```

- Instal mininet

```
mininet/util/install.sh -nfv
```

## 3. Instalasi RYU

Ryu adalah sebuah framework software untuk SDN Controller dan pengembangan aplikasi SDN dan menyediakan beragam komponen software lengkap dengan API yang memudahkan pengembang melakukan pembuatan aplikasi berbasis controller SDN.

- Download repository Ryu dan lakukan instalasi

```
git clone https://github.com/osrg/ryu.git
cd ryu; pip install .
cd
```

Setelah instal Flowmanager, lakukan rebooting Linux untuk membuat lingkungan operasional Python, Mininet, Ryu dan OpenFlow dapat berjalan dengan baik.

## 4. Percobaan Sederhana

- Interaksi dengan Host dan Switch
  - ![](ss/9.png)
  - ![](ss/8.png)

```
sudo mn
```

Perintah ini secara default membuat topologi 2 host dengan 1 switch dan 1 OpenFlow reference controller.

- Menampilkan apa saja daftar perintah Mininet CLI :

```
mininet> help
```

- Menampilkan nodes :

```
mininet> nodes
```

- Menampilkan links :

```
mininet> net
```

- Menampilakan informasi semua nodes :

```
mininet> dump
```

- Tes koneksi antar Host

```
ubuntu@ip-172-31-85-120:~$ sudo mn
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2
*** Adding switches:
s1
*** Adding links:
(h1, s1) (h2, s1)
*** Configuring hosts
h1 h2
*** Starting controller
c0
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
mininet> h1 ping -c 2 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.267 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.065 ms

--- 10.0.0.2 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1032ms
rtt min/avg/max/mdev = 0.065/0.166/0.267/0.101 ms
mininet>
```
