# MANUAL PENGGUNAAN: KREATIVLABS UMKM DATA SYNC

## Identitas

- **Nama Lengkap: Andika Arif Sofyan
- NIM: 32602200027

## Deskripsi Aplikasi

Aplikasi ini mengautomasi interaksi ke layanan AWS S3 dan AWS DynamoDB di lingkungan lokal menggunakan LocalStack sebagai cloud emulator. Dengan aplikasi ini, pengguna dapat membuat tabel DynamoDB untuk menyimpan profil UMKM, serta membuat dan mengunggah file aset ke S3 bucket, seluruhnya berjalan di mesin lokal tanpa memerlukan akun AWS.

## Persyaratan Sistem

- Docker Engine
- Python 3.10+
- LocalStack CLI

## Langkah Instalasi

1. Jalankan LocalStack dalam mode daemon:

```bash
localstack start -d
```

2. Instal dependensi Python yang diperlukan:

```bash
pip install boto3 awscli-local
```

## Cara Penggunaan

Jalankan aplikasi dengan perintah berikut:

```bash
python app.py
```

## Verifikasi

Gunakan perintah berikut untuk memverifikasi bahwa data telah berhasil dibuat:

1. Verifikasi file di S3 bucket:

```bash
awslocal s3 ls s3://kreativlabs-assets
```

2. Verifikasi data di tabel DynamoDB:

```bash
awslocal dynamodb scan --table-name UMKM-Profiles
```

---

**Batas waktu pengumpulan: 30 menit dari jam pelaksanaan.**
