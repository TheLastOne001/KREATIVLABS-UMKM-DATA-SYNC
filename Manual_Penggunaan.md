# MANUAL PENGGUNAAN APLIKASI
**KREATIVLABS UMKM DATA SYNC**

---

## IDENTITAS MAHASISWA
*   **Nama Lengkap:** *(isi nama lengkap kamu di sini)*
*   **NIM / ID:** *(isi NIM kamu di sini)*
*   **Mata Kuliah:** *(isi nama mata kuliah, opsional)*
*   **Tautan Repositori GitHub:** [https://github.com/username-kamu/kreativlabs-umkm-sync](https://github.com/username-kamu/kreativlabs-umkm-sync) *(ganti dengan link aslimu)*

---

## BAB I: PENDAHULUAN

### 1.1 Deskripsi Aplikasi
**KreativLabs UMKM Data Sync** adalah sebuah purwarupa (prototype) perangkat lunak berbasis Python yang berfungsi untuk mengotomatisasi interaksi ke layanan komputasi awan AWS (Amazon Web Services). Sistem ini dirancang untuk mensimulasikan penyimpanan data profil UMKM pada *AWS DynamoDB* (database NoSQL) dan penyimpanan aset digital pada *AWS S3 Bucket*. 

### 1.2 Tujuan Sistem
Aplikasi ini ditujukan sebagai lingkungan simulasi dan pengembangan (development environment) lokal. Menggunakan **LocalStack** sebagai emulator cloud, sistem ini mampu menjalankan seluruh fungsi AWS secara *offline* di mesin lokal tanpa memerlukan akun AWS sungguhan, sehingga menjamin efisiensi biaya dan keamanan data selama proses uji coba.

---

## BAB II: PERSYARATAN SISTEM

Untuk dapat menjalankan aplikasi ini dengan baik, komputer (host) harus memenuhi spesifikasi perangkat lunak berikut:

1.  **Sistem Operasi:** Windows 10/11, macOS, atau Linux.
2.  **Mesin Virtual:** **Docker Desktop** (versi terbaru) harus terinstal dan dalam keadaan berjalan (*running*).
3.  **Lingkungan Pemrograman:** **Python versi 3.10** atau yang lebih tinggi.
4.  **Pustaka Python (Dependencies):**
    *   `boto3`: AWS SDK for Python.
    *   `awscli-local` (`awslocal`): Command Line Interface khusus untuk LocalStack.

---

## BAB III: INSTALASI DAN KONFIGURASI

Berikut adalah langkah-langkah persiapan sebelum aplikasi dapat dioperasikan:

### 3.1 Menjalankan Mesin Docker
Pastikan aplikasi Docker Desktop telah dibuka. Tunggu hingga indikator mesin Docker berwarna hijau atau menunjukkan status *"Engine running"*.

### 3.2 Menjalankan LocalStack
Buka Terminal / Command Prompt pada direktori project, lalu jalankan perintah berikut untuk mengunduh dan menjalankan emulator LocalStack:
```bash
docker run -d --name localstack -p 4566:4566 -p 4510-4559:4510-4559 -e DOCKER_HOST=unix:///var/run/docker.sock localstack/localstack:3.8
```
*(Catatan: Tunggu sekitar 15-30 detik hingga container LocalStack siap menerima permintaan pada port 4566).*

### 3.3 Instalasi Dependensi Python
Instal pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal:
```bash
pip install boto3 awscli-local awscli
```

---

## BAB IV: PENGOPERASIAN APLIKASI

Setelah lingkungan *cloud* lokal berhasil dikonfigurasi, aplikasi utama dapat dijalankan.

### 4.1 Eksekusi Script Utama
Buka terminal pada direktori yang berisi file `app.py`, lalu jalankan perintah eksekusi standar Python:
```bash
python app.py
```

### 4.2 Proses Otomasi (Di Balik Layar)
Saat perintah di atas dijalankan, sistem secara otomatis melakukan rutinitas berikut:
1.  **Tahap Setup:** Membuat tabel DynamoDB bernama `UMKM-Profiles` dan membuat S3 Bucket bernama `kreativlabs-assets`.
2.  **Tahap Eksekusi (Database):** Memasukkan 1 baris data (item) JSON dummy ke dalam tabel DynamoDB yang memuat profil UMKM (ID, Nama Usaha, Pemilik, Kota, Kategori).
3.  **Tahap Eksekusi (Storage):** Menghasilkan sebuah file teks secara lokal (`dummy_asset.txt`), kemudian mengunggah (*upload*) file tersebut ke dalam keranjang AWS S3 yang telah dibuat pada tahap setup.

### 4.3 Output Sistem
Jika aplikasi berjalan tanpa galat (error), terminal akan menampilkan log (catatan) eksekusi seperti berikut:
```text
[SETUP] Membuat tabel DynamoDB 'UMKM-Profiles'...
[SETUP] Tabel 'UMKM-Profiles' berhasil dibuat.
[SETUP] Membuat S3 bucket 'kreativlabs-assets'...
[SETUP] Bucket 'kreativlabs-assets' berhasil dibuat.
[EXEC] Menyisipkan data profil UMKM ke DynamoDB...
[EXEC] Data profil UMKM berhasil disisipkan.
[EXEC] Membuat file lokal 'dummy_asset.txt'...
[EXEC] File 'dummy_asset.txt' berhasil dibuat.
[EXEC] Mengunggah 'dummy_asset.txt' ke S3 bucket...
[EXEC] File berhasil diunggah ke 'kreativlabs-assets'.

[DONE] Seluruh proses selesai.
```

---

## BAB V: VERIFIKASI HASIL (TESTING)

Tahap terakhir adalah membuktikan bahwa aplikasi benar-benar berhasil menyimpan data pada emulator AWS. Gunakan program `awslocal` untuk memverifikasi data di dalam terminal.

### 5.1 Verifikasi Penyimpanan File (AWS S3)
Jalankan perintah ini untuk melihat isi dalam bucket S3:
```bash
awslocal s3 ls s3://kreativlabs-assets
```
**Ekspektasi Hasil:** Sistem akan menampilkan daftar file yang berisi `dummy_asset.txt` beserta ukuran dan tanggal modifikasinya.

### 5.2 Verifikasi Penyimpanan Database (AWS DynamoDB)
Jalankan perintah ini untuk memindai seluruh isi tabel database:
```bash
awslocal dynamodb scan --table-name UMKM-Profiles
```
**Ekspektasi Hasil:** Sistem akan mencetak keluaran berformat JSON yang berisi data profil *"Toko Sejahtera"* milik *"Budi Santoso"* secara utuh.

---
*Dokumen ini disusun sebagai panduan teknis operasional aplikasi KreativLabs UMKM Data Sync.*
