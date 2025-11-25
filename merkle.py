import hashlib #Import library hashlib

# Fungsi hash menggunakan sha256
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Fungsi untuk membangun merkle tree
def build_merkle_tree(transactions): 
    if not transactions: 
        return []

    # Hash transaksi awal
    layer = [sha256(tx) for tx in transactions]
    tree = [layer]

    # Bangun pohon sampai tinggal 1 hash (root)
    while len(layer) > 1:

        # Jika jumlah hash ganjil → duplikasi elemen terakhir
        if len(layer) % 2 == 1:
            layer.append(layer[-1]) # Duplikasi jika ganjil

        next_layer = []
        for i in range(0, len(layer), 2): #Artinya dari range 0 sampai panjang layer setiap iterasi lompat 2
            combined = layer[i] + layer[i+1] # Gabungkan pasangan
            next_layer.append(sha256(combined)) # Hash pasangan

        layer = next_layer #Jadikan layer ke level selanjutnya
        tree.append(layer) #Tambahkan ke variabel tree
    
    # isi dari Tree = ([1,2,3,4,5,6],[12,34,56,56],[1234,5656], [12345656])

    return tree

# Membuat Merkle Proof untuk 1 transaksi
def get_merkle_proof(transactions, target_tx):
    tree = build_merkle_tree(transactions) # Membuat merkle tree dari transaksi
    hashed_tx = sha256(target_tx) # Hash transaksi yang mau divalidasi

    if hashed_tx not in tree[0]: # Cek transaksi validasi di daun layer 0 jika tidak ada maka return none
        return None

    proof = []
    index = tree[0].index(hashed_tx) # Disini index menampung posisi dari transaksi yang mau di validasi

    # Contoh
    # tree[0] = ["h1","h2","h3","h4"]
    # hashed_tx = "h3"
    # index = tree[0].index(hashed_tx)  # index = 2

    for layer in tree[:-1]: #Loop sampai index terakhir - 1
        if len(layer) % 2 == 1:
            layer = layer + [layer[-1]] # Duplikasi jika ganjil
        # Disini pasangan sudah tidak ada yang ganjil

        # pasangan kiri/kanan
        if index % 2 == 0:  # kiri → pasangan di kanan
            sibling = layer[index + 1]
            proof.append(("right", sibling)) # Tambahkan ke proof
        else:              # kanan → pasangan di kiri
            sibling = layer[index - 1]
            proof.append(("left", sibling)) # Tambahkan ke proof

        index //= 2  # Naik 1 level // = Int, / = float

    return proof

# Validasi Transaksi
def verify_merkle_proof(target_tx, proof, merkle_root):
    current_hash = sha256(target_tx) # Hash transaksi yang mau divalidasi

    for direction, sibling in proof: # Direction sebagai elemen pertama yang berisi "right" / "left" dan sibling hash pasangannya
        if direction == "right":
            current_hash = sha256(current_hash + sibling) # Hash current hash + pasangannya
        else:  # left
            current_hash = sha256(sibling + current_hash) # Hash pasangannya + current hash

    return current_hash == merkle_root # Cocok dengan root?

# Main
def main():
    print("~~~ Merkle Tree ~~~")
    print("~~~ Masukan Transaksi (Kosongkan Untuk Selesai) ~~~")

    # Input transaksi
    txs = []
    while True:
        tx = input("> ")
        if tx.strip() == "":
            break
        txs.append(tx)

    tree = build_merkle_tree(txs)

    print("\n~~~ Hasil Merkle Tree ~~~\n")
    for i, layer in enumerate(tree, start=1): # Maksud start=1 disini adalah visualnya dimulai dari 1 meskipun indexnya 0
        print(f"~ Layer {i}:")
        for h in layer:
            print(" ~ ", h)
        print()

    print("Merkle Root:", tree[-1][0]) # Mengakses index terakhir (merkle root)

    # Validasi transaksi
    print("\n~~~ Validasi Transaksi ~~~")
    tx_check = input("Masukkan transaksi yang ingin divalidasi: ")

    proof = get_merkle_proof(txs, tx_check) 

    if proof is None:
        print("Transaksi TIDAK ditemukan di blok!")
    else:
        print("\n Merkle Proof:")
        for p in proof:
            print("  ", p)

        is_valid = verify_merkle_proof(tx_check, proof, tree[-1][0])
        print("\nHasil Validasi:", "~~ Valid ~~" if is_valid else "~~ Tidak Valid ~~")


if __name__ == "__main__":
    main()


# Realisasi di Blockchain Bitcoin

# Untuk verifikasi, seseorang harus tahu:
# Transaksi yang ingin dicek
# Merkle Proof (sibling hash + arah kiri/kanan)
# Merkle Root resmi (dari header blok)

# Dengan ini, kita bisa hitung ulang hash dari transaksi ke root dan pastikan cocok

# Kalau cocok → proof valid → transaksi benar-benar ada di tree asli
# Kalau tidak → proof palsu

# Merkle Proof bisa dibuka publik
# Bisa dipalsukan → harus diverifikasi

# Inti

# 1️⃣ Butuh path (Merkle Proof) untuk verifikasi transaksi

# User tidak perlu seluruh tree, cukup jalur sibling hash dari transaksi ke Merkle Root
# Jalur ini disebut Merkle Proof / path

# 2️⃣ Kalau mau punya full path sendiri

# Harus download seluruh blockchain → jadi full node
# Bisa membangun Merkle Tree sendiri → ambil proof untuk transaksi mana pun
# Kekurangannya: butuh storage besar dan bandwidth tinggi

# 3️⃣ Alternatif ringan: minta ke pihak ketiga

# SPV node / layanan publik:
# Mereka sudah punya full node → membangun tree sendiri
# Kirimkan proof + root resmi ke user
# User cukup verifikasi proof ke Merkle Root

# Kekurangannya:

# Bergantung pihak ketiga untuk proof
# Proof bisa saja dipalsukan jika user tidak verifikasi dengan root resmi
# Tapi selama root resmi digunakan → aman