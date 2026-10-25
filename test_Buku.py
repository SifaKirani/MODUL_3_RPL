from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku():
    model = BukuModel()

    # Mock koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Data buku tiruan
    mock_cursor.fetchall.return_value = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    # Menjalankan fungsi get_all_buku()
    hasil = model.get_all_buku()

    # Memastikan hasil berupa list
    assert isinstance(hasil, list)

    # Memastikan data buku berhasil dikembalikan
    assert len(hasil) == 1
    assert hasil[0]["judul"] == "Buku Testing"

    # Memastikan query dijalankan
    mock_cursor.execute.assert_called_once()