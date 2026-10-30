
# Sistem Informasi Perpustakaan

## Deskripsi Proyek
Sistem Informasi Perpustakaan merupakan aplikasi berbasis Python yang digunakan untuk mengelola data buku dan anggota perpustakaan. Aplikasi ini memiliki fitur tambah, tampil, ubah, dan hapus data (CRUD), serta sistem autentikasi pengguna dengan hak akses berdasarkan role.

Aplikasi dikembangkan menggunakan konsep **Model-View-Controller (MVC)** agar kode program lebih terstruktur dan mudah dikembangkan.

## Fitur Aplikasi
- Login dan autentikasi pengguna.
- Registrasi pengguna.
- Pengelolaan data buku.
- Pengelolaan data anggota.
- Tambah, tampil, ubah, dan hapus data.
- Pembagian hak akses admin dan anggota.
- Password disimpan menggunakan hash SHA-256.
- Logout untuk keluar dari aplikasi.

## Teknologi yang Digunakan
- Python
- MySQL
- CustomTkinter
- Tkinter dan ttk
- Pytest
- Flake8
- GitHub Actions

## Struktur Folder Proyek

```text
Modul3_RPL/
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   └── auth_controller.py
│
├── models/
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── user_model.py
│
├── Views/
│   └── buku_View.py
│
├── tests/
│   ├── test_buku.py
│   └── test_auth.py
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── main.py
├── main_auth.py
├── requirements.txt
└── README.md
```

## Arsitektur MVC

1. **Model**: Mengelola data dan berhubungan langsung dengan database MySQL.
2. **View**: Menampilkan antarmuka aplikasi kepada pengguna.
3. **Controller**: Menghubungkan Model dan View serta mengatur alur proses aplikasi.

## Persiapan Database

1. Instal dan jalankan MySQL.
2. Buat database dengan nama `perpustakaan`.
3. Sesuaikan konfigurasi koneksi database pada file `config/database.py`.
4. Pastikan tabel yang dibutuhkan aplikasi sudah tersedia, yaitu tabel `buku`, `anggota`, dan `users`.

## Instalasi dan Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/SifaKirani/MODUL_3_RPL.git
```

### 2. Masuk ke Folder Proyek

```bash
cd MODUL_3_RPL
```

### 3. Buat Virtual Environment

```bash
python -m venv env
```

### 4. Aktifkan Virtual Environment

Windows PowerShell:

```powershell
.\env\Scripts\Activate
```

### 5. Instal Dependensi

```bash
pip install -r requirements.txt
```

### 6. Jalankan Aplikasi

```bash
python main.py
```

Untuk menjalankan aplikasi melalui sistem login:

```bash
python main_auth.py
```

## Pengujian Aplikasi

Pengujian dilakukan menggunakan Pytest untuk memastikan fungsi aplikasi berjalan sesuai dengan yang diharapkan.

Jalankan perintah:

```bash
python -m pytest -v
```

Pemeriksaan kualitas kode dilakukan menggunakan Flake8:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Continuous Integration (CI)

Proyek ini menggunakan GitHub Actions untuk menjalankan proses pengujian secara otomatis setiap kali terdapat push atau pull request ke branch `main`.

Tahapan CI meliputi:
1. Checkout repository.
2. Menyiapkan lingkungan Python.
3. Menginstal dependensi.
4. Memeriksa kualitas kode menggunakan Flake8.
5. Menjalankan pengujian otomatis menggunakan Pytest.

## Versi Aplikasi

**Release:** v1.0.0

Aplikasi juga tersedia dalam bentuk executable Windows (`.exe`) melalui GitHub Releases pada repository proyek.
