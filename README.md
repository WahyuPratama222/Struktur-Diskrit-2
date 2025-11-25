# 🌳 Implementasi Merkle Tree Sederhana (Python)

Proyek ini adalah implementasi sederhana dari struktur data **Merkle Tree** (juga dikenal sebagai *Hash Tree*) menggunakan Python. Merkle Tree adalah struktur penting yang digunakan dalam teknologi *blockchain*, seperti Bitcoin, untuk memverifikasi integritas data secara efisien.



---

## 📋 Fitur Utama

Kode ini mengimplementasikan fungsi-fungsi inti dari Merkle Tree:

1.  `sha256(data)`: Fungsi hashing standar yang digunakan untuk semua data.
2.  `build_merkle_tree(transactions)`: Membangun Merkle Tree dari daftar transaksi dan menghasilkan Merkle Root. Menangani kasus ganjil dengan menduplikasi hash terakhir.
3.  `get_merkle_proof(transactions, target_tx)`: Menghasilkan **Merkle Proof** (jalur *sibling hash* dan arahnya) yang diperlukan untuk memverifikasi transaksi tertentu.
4.  `verify_merkle_proof(target_tx, proof, merkle_root)`: Fungsi validasi yang menghitung ulang hash dari transaksi hingga Merkle Root menggunakan *proof* yang diberikan.

---

## 🚀 Cara Menjalankan

### Persyaratan

Pastikan Anda memiliki Python 3 terinstal. Tidak ada *library* eksternal yang perlu diinstal selain `hashlib` yang sudah tersedia di Python standar.

```bash
# Anda hanya memerlukan Python
python --version
