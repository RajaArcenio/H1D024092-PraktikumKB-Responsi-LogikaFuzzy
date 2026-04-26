# Penerapa Logika Fuzzy Untuk Menentukan Diskon produk

Aplikasi desktop berbasis Python yang menggunakan **Logika Fuzzy (Fuzzy Logic)** untuk menentukan strategi diskon produk secara dinamis. Sistem ini dirancang untuk membantu pemilik bisnis atau manajer gudang dalam mengoptimalkan perputaran stok dan meminimalisir kerugian akibat barang yang mengendap terlalu lama (*deadstock*).

## 👤 Penulis
- Nama: Raja Arcenio Ravi Hussain
- NIM: H1D024092

## 🚀 Fitur Utama
- **Multipage GUI**: Antarmuka modern dengan 3 halaman (Welcome, Input, dan Output) menggunakan Python Tkinter.
- **Fuzzy Inference System**: Menggunakan metode **Mamdani** melalui library `scikit-fuzzy`.
- **Validasi Input Real-time**: Mencegah kesalahan input (anomali) seperti angka di luar rentang atau karakter non-numerik dengan notifikasi peringatan.
- **Helper Text**: Panduan pengisian input yang selaras dengan prinsip *Human-Computer Interaction* (HCI).
- **27 Basis Aturan (Rules)**: Logika komprehensif yang mencakup seluruh kombinasi kondisi inventaris.

## 🧠 Logika Fuzzy
Sistem ini mengevaluasi 3 variabel input (*Antecedents*) untuk menghasilkan 1 variabel output (*Consequent*):

### Variabel Input (Antecedents)
1. **Stok Saat Ini (0 - 100%)**: Persentase jumlah produk dibandingkan kapasitas gudang.
   - Himpunan: `Sedikit`, `Sedang`, `Banyak`.
2. **Sisa Masa Simpan (0 - 730 Hari)**: Durasi sebelum produk kedaluwarsa atau usang.
   - Himpunan: `Kritis`, `Aman`, `Lama`.
3. **Kecepatan Penjualan (0 - 100%)**: Rata-rata persentase produk terjual per minggu.
   - Himpunan: `Lambat`, `Normal`, `Cepat`.

### Variabel Output (Consequent)
1. **Rekomendasi Diskon (0 - 50%)**
   - Himpunan: `Sedikit`, `Sedang`, `Besar`.

## 🛠️ Prasyarat (Requirements)
Pastikan Anda telah menginstal Python (versi 3.x) dan beberapa library pendukung berikut:

```bash
pip install numpy scikit-fuzzy
```

## 💻 Cara Menjalankan

### 1. Clone repositori ini
```bash
git clone [https://github.com/username/smart-pricing-fuzzy.git](https://github.com/username/smart-pricing-fuzzy.git)
```

### 2. Masuk ke direktori proyek:
```bash
cd smart-pricing-fuzzy
```

### 3. Jalankan aplikasi:
```bash
python main.py
```

## 📖 Cara Menggunakan

### 1. Pada halaman **Welcome**, klik tombol **Mulai Analisis**.
### 2. Masukkan data inventaris pada halaman **Input**. Perhatikan instruksi di atas setiap kolom input agar data yang dimasukkan valid (angka dalam rentang yang ditentukan).
### 3. Klik **Hitung Rekomendasi**. Jika input valid, sistem akan mengarahkan ke halaman Output.
### 4. Lihat hasil persentase diskon yang disarankan berdasarkan analisis logika fuzzy.
### 5. Klik **Ulangi Analisis** untuk mengecek produk lain atau **Keluar Program** untuk selesai.

## 📝 Detail Teknis (Fuzzy Rules)
Sistem ini menggunakan 27 aturan untuk memastikan tidak ada celah logika. Contoh aturan utama:
- **IF** Stok Banyak **AND** Masa Simpan Kritis **AND** Penjualan Lambat **THEN** Diskon Besar.
- **IF** Stok Sedikit **AND** Masa Simpan Lama **AND** Penjualan Cepat **THEN** Diskon Sedikit.

