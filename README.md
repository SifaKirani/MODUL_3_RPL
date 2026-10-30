# Sistem Informasi Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Informasi Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk membantu pengelolaan data perpustakaan. Aplikasi ini menerapkan arsitektur Model-View-Controller (MVC) dan menggunakan database MySQL untuk menyimpan data.
Fitur aplikasi meliputi:
- Login dan autentikasi pengguna.
- Registrasi pengguna.
- Pengelolaan data buku.
- Pengelolaan data anggota.
- Hak akses berdasarkan role pengguna.

## 2. Struktur Direktori MVC

```text
MODUL_3_RPL/
│
├── models/
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── user_model.py
│
├── views/
│   ├── buku_view.py
│   ├── anggota_view.py
│   └── login_view.py
│
├── controllers/
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   └── auth_controller.py
│
├── tests/
│   ├── test_buku.py
│   └── test_auth.py
│
├── config/
│   └── database.py
│
├── main.py
├── main_auth.py
├── requirements.txt
└── README.md
```

## 3. Instalasi dan Konfigurasi Database MySQL

1. Instal Python dan Visual Studio Code.
2. Instal Laragon dan jalankan layanan MySQL.
3. Buat database dengan nama `perpustakaan`.
4. Sesuaikan konfigurasi koneksi database pada `config/database.py`.
5. Pastikan tabel buku, anggota, dan users sudah tersedia.

## 4. Instalasi Dependensi

Aktifkan virtual environment, kemudian jalankan:

```bash
pip install -r requirements.txt
```

## 5. Cara Menjalankan Aplikasi

Pastikan MySQL pada Laragon sudah aktif, kemudian jalankan aplikasi melalui terminal:

```bash
python main.py
```

Untuk menjalankan pengujian:

```bash
pytest -v
```

Untuk menjalankan aplikasi hasil pemaketan, buka file `AplikasiPerpustakaan.exe` di dalam folder `dist/`.
