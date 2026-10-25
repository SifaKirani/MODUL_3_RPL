
import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Konfigurasi Jendela
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("800x480")
        self.minsize(700, 450)

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Input Nama Anggota
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota",
            state="normal"
        )
        self.entry_nama.pack(
            pady=8, padx=15, fill="x"
        )

        # Input Alamat Anggota
        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat Anggota",
            state="normal"
        )
        self.entry_alamat.pack(
            pady=8, padx=15, fill="x"
        )

        # Tombol Simpan Data
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            hover_color="darkgreen"
        )
        self.btn_simpan.pack(
            pady=5, padx=15, fill="x"
        )

        # Tombol Update Data
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            hover_color="darkblue"
        )
        self.btn_update.pack(
            pady=5, padx=15, fill="x"
        )

        # Tombol Hapus Data
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            hover_color="darkred"
        )
        self.btn_delete.pack(
            pady=5, padx=15, fill="x"
        )

        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Frame untuk Tabel dan Scrollbar
        self.frame_tabel = ctk.CTkFrame(
            self.frame_kanan,
            fg_color="transparent"
        )
        self.frame_tabel.pack(
            fill="both", expand=True, padx=15, pady=10
        )

        # Kolom Tabel
        kolom = ("id_anggota", "nama_anggota", "alamat")

        self.tabel = ttk.Treeview(
            self.frame_tabel,
            columns=kolom,
            show="headings",
            height=15
        )

        # Header Tabel
        self.tabel.heading(
            "id_anggota", text="ID Anggota"
        )
        self.tabel.heading(
            "nama_anggota", text="Nama Anggota"
        )
        self.tabel.heading(
            "alamat", text="Alamat"
        )

        # Lebar Kolom
        self.tabel.column(
            "id_anggota", width=80, anchor="center"
        )
        self.tabel.column(
            "nama_anggota", width=160, anchor="w"
        )
        self.tabel.column(
            "alamat", width=200, anchor="w"
        )

        # Scrollbar Vertikal
        self.scrollbar = ttk.Scrollbar(
            self.frame_tabel,
            orient="vertical",
            command=self.tabel.yview
        )
        self.tabel.configure(
            yscrollcommand=self.scrollbar.set
        )

        # Menampilkan Tabel dan Scrollbar
        self.tabel.pack(
            side="left", fill="both", expand=True
        )
        self.scrollbar.pack(
            side="right", fill="y"
        )


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()
