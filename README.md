# 🌳 Simple Merkle Tree Implementation

A straightforward implementation of a **Merkle Tree** (also known as a *Hash Tree*) data structure using Python. Merkle Trees are fundamental components in blockchain technology, such as Bitcoin, used to efficiently verify data integrity.

## 📚 Table of Contents

- [What is a Merkle Tree?](#what-is-a-merkle-tree)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Real-World Application: Bitcoin Blockchain](#real-world-application-bitcoin-blockchain)
- [Example Output](#example-output)

---

## 🔍 What is a Merkle Tree?

A Merkle Tree is a binary tree structure where:
- **Leaf nodes** contain hashes of individual data blocks (transactions)
- **Non-leaf nodes** contain hashes of their child nodes concatenated together
- The **root node** (Merkle Root) represents a cryptographic fingerprint of all the data

This structure allows for efficient and secure verification of data integrity without needing to store or transmit the entire dataset.

---

## ✨ Features

This implementation provides core Merkle Tree functionality:

1. **`sha256(data)`** - Standard hashing function using SHA-256 for all data
2. **`build_merkle_tree(transactions)`** - Constructs a complete Merkle Tree from a list of transactions and generates the Merkle Root. Handles odd-numbered nodes by duplicating the last hash
3. **`get_merkle_proof(transactions, target_tx)`** - Generates a **Merkle Proof** (path of sibling hashes and their positions) required to verify a specific transaction
4. **`verify_merkle_proof(target_tx, proof, merkle_root)`** - Validation function that recalculates the hash path from a transaction to the Merkle Root using the provided proof

---

## 📋 Requirements

- Python 3.x
- No external libraries required (uses built-in `hashlib`)

---

## 🚀 Installation

1. Clone or download this repository
2. Verify Python installation:

```bash
python --version
# or
python3 --version
```

3. Run the program:

```bash
python merkle.py
# or
python3 merkle.py
```

---

## 💻 Usage

### Interactive Mode

Run the script and follow the prompts:

```bash
python merkle.py
```

1. Enter transactions one by one (press Enter on empty line to finish)
2. View the generated Merkle Tree structure
3. Enter a transaction to verify its inclusion in the tree

### Example Session

```
~~~ Merkle Tree ~~~
~~~ Enter Transactions (Empty to Finish) ~~~
> Alice pays Bob 10 BTC
> Bob pays Charlie 5 BTC
> Charlie pays Dave 3 BTC
> 

~~~ Merkle Tree Result ~~~

~ Layer 1:
  ~  a1b2c3d4... (hash of "Alice pays Bob 10 BTC")
  ~  e5f6g7h8... (hash of "Bob pays Charlie 5 BTC")
  ~  i9j0k1l2... (hash of "Charlie pays Dave 3 BTC")
  ~  i9j0k1l2... (duplicate of last hash - odd number handling)

~ Layer 2:
  ~  m3n4o5p6... (combined hash)
  ~  q7r8s9t0... (combined hash)

~ Layer 3:
  ~  u1v2w3x4... (Merkle Root)

Merkle Root: u1v2w3x4...

~~~ Verify Transaction ~~~
Enter transaction to verify: Bob pays Charlie 5 BTC

Merkle Proof:
   ('left', 'a1b2c3d4...')
   ('right', 'q7r8s9t0...')

Validation Result: ~~ Valid ~~
```

---

## 🔧 How It Works

### Building the Tree

1. Hash each transaction (leaf nodes)
2. Pair hashes and combine them: `hash(hash1 + hash2)`
3. If odd number of hashes, duplicate the last one
4. Repeat until only one hash remains (the Merkle Root)

### Generating a Proof

To prove a transaction exists without sharing all transactions:
1. Find the target transaction's position
2. Collect sibling hashes at each level
3. Record whether each sibling is on the left or right

### Verifying a Proof

1. Start with the transaction hash
2. Combine with each sibling hash in the proof (respecting left/right order)
3. Hash the combination at each step
4. Compare final result with the Merkle Root

If they match ✅ → Transaction is valid
If they don't match ❌ → Transaction is invalid or tampered with

---

## 🪙 Real-World Application: Bitcoin Blockchain

### How Bitcoin Uses Merkle Trees

In Bitcoin, each block header contains a Merkle Root representing all transactions in that block. This enables:

- **Efficient Verification**: Verify a transaction without downloading the entire blockchain
- **Lightweight Clients (SPV)**: Mobile wallets can verify payments with minimal data
- **Tamper Detection**: Any change to a transaction changes the Merkle Root

### Verification Methods

#### 1️⃣ **Full Node** (Complete Independence)
- Downloads entire blockchain
- Builds complete Merkle Trees
- Generates proofs for any transaction
- **Trade-off**: Requires significant storage (hundreds of GB) and bandwidth

#### 2️⃣ **SPV Node** (Simplified Payment Verification)
- Downloads only block headers (with Merkle Roots)
- Requests Merkle Proofs from full nodes
- Verifies proofs against official Merkle Root
- **Trade-off**: Depends on third parties for proofs, but still cryptographically secure

### Security Considerations

- Merkle Proofs can be publicly shared without security risk
- Proofs can only be validated against the official Merkle Root
- Attempting to fake a proof will fail verification
- As long as the Merkle Root is authentic, the verification is trustworthy

---

## 📊 Example Output

```
~~~ Merkle Tree ~~~
~~~ Enter Transactions (Empty to Finish) ~~~
> tx1
> tx2
> tx3
> 

~~~ Merkle Tree Result ~~~

~ Layer 1:
  ~  b3a8f... (tx1 hash)
  ~  4d5e2... (tx2 hash)
  ~  7c6f9... (tx3 hash)
  ~  7c6f9... (duplicate)

~ Layer 2:
  ~  a1d7e...
  ~  8f3b2...

~ Layer 3:
  ~  f4e8d9c2a... (Merkle Root)

Merkle Root: f4e8d9c2a...
```

---

## 📝 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests to improve this implementation!

---

**Built with 💙 for learning blockchain fundamentals**
