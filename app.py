"""
KreativLabs UMKM Data Sync
Aplikasi sinkronisasi data UMKM menggunakan AWS S3 dan DynamoDB
melalui LocalStack Cloud Emulator.
"""

import boto3


# Konfigurasi endpoint LocalStack
ENDPOINT_URL = "http://localhost:4566"
REGION_NAME = "us-east-1"

# Inisialisasi client DynamoDB
dynamodb_client = boto3.client(
    "dynamodb",
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

# Inisialisasi client S3
s3_client = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
    aws_access_key_id="test",
    aws_secret_access_key="test",
)


def setup_services():
    """Membuat tabel DynamoDB dan S3 bucket yang diperlukan."""
    # Membuat tabel DynamoDB 'UMKM-Profiles'
    print("[SETUP] Membuat tabel DynamoDB 'UMKM-Profiles'...")
    dynamodb_client.create_table(
        TableName="UMKM-Profiles",
        KeySchema=[
            {"AttributeName": "ClientID", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "ClientID", "AttributeType": "S"},
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    print("[SETUP] Tabel 'UMKM-Profiles' berhasil dibuat.")

    # Membuat S3 bucket 'kreativlabs-assets'
    print("[SETUP] Membuat S3 bucket 'kreativlabs-assets'...")
    s3_client.create_bucket(Bucket="kreativlabs-assets")
    print("[SETUP] Bucket 'kreativlabs-assets' berhasil dibuat.")


def execute_app():
    """Menyisipkan data dummy ke DynamoDB dan mengunggah file ke S3."""
    # Menyisipkan 1 item data profil dummy ke tabel DynamoDB
    print("[EXEC] Menyisipkan data profil UMKM ke DynamoDB...")
    dynamodb_client.put_item(
        TableName="UMKM-Profiles",
        Item={
            "ClientID": {"S": "UMKM-001"},
            "NamaUsaha": {"S": "Toko Sejahtera"},
            "Pemilik": {"S": "Budi Santoso"},
            "Kota": {"S": "Surabaya"},
            "Kategori": {"S": "Retail"},
        },
    )
    print("[EXEC] Data profil UMKM berhasil disisipkan.")

    # Membuat file lokal dummy_asset.txt
    print("[EXEC] Membuat file lokal 'dummy_asset.txt'...")
    with open("dummy_asset.txt", "w", encoding="utf-8") as f:
        f.write("File aset dummy untuk KreativLabs UMKM Data Sync.")
    print("[EXEC] File 'dummy_asset.txt' berhasil dibuat.")

    # Mengunggah file ke S3 bucket
    print("[EXEC] Mengunggah 'dummy_asset.txt' ke S3 bucket...")
    s3_client.upload_file("dummy_asset.txt", "kreativlabs-assets", "dummy_asset.txt")
    print("[EXEC] File berhasil diunggah ke 'kreativlabs-assets'.")


if __name__ == "__main__":
    setup_services()
    execute_app()
    print("\n[DONE] Seluruh proses selesai.")
