# Final Cryptography Project: Mini Blockchain with RSA Authentication - Documentation

## Table of Contents:
1. **Introduction**
2. **Project Overview**
3. **Key Concepts**
4. **Technologies Used**
5. **How the System Works**
6. **How to Run the Project**
7. **Conclusion**


---

## 1. **Introduction**

For my final cryptography project I choose to implemente a **MiniBlockchain**. It started as a simple as possible, like an educational implementation of a blockchain. It initially consisted of basic blockchain functionality such as creating blocks, adding transactions, and validating the chain. As the project progressed, I thought that it woub be more interesting to add RSA encryption for more security to the system. 

The RSA encryption ensures that only authorized participants can create and verify transactions. The addition of RSA authentication not only enhanced security but also provided more reliability for verifying transaction integrity, which is a critical feature in blockchain technology.

This project now demonstrates a **blockchain** with **transaction signing and verification** through **RSA public-key cryptography**, ensuring that each transaction is authenticated before being included in the blockchain.

## 2. **Project Overview**

Initially, the **MiniBlockchain** was a simple system where:
- **Blocks** contained transaction data.
- **Transactions** were simply added to the blockchain without authentication.

As the project evolved:
- **RSA encryption** was introduced to secure transactions, adding digital signatures for both senders and receivers.
- **Transaction verification** was implemented using RSA public keys to ensure that only authorized parties can initiate valid transactions.

The system now includes:
- **Blockchain**: A chain of blocks where each block contains validated transactions.
- **RSA Authentication**: Transactions are signed with the sender's private RSA key and verified with the sender's public RSA key before being added to the blockchain.
- **Mining**: A proof-of-work process is used to secure and validate new blocks.
- **Transaction Verification**: The addition of RSA ensures that only valid transactions are included in the blockchain.

## 3. **Key Concepts**

- **Blockchain**: A decentralized, immutable ledger where data is stored in blocks. Each block is linked to the previous block via its hash, creating a secure chain.
- **RSA Encryption**: A public-key cryptosystem used for signing transactions with the sender's private key and verifying them with the sender's public key.
- **Proof of Work**: A consensus mechanism where miners solve a computational puzzle to add a new block to the blockchain, ensuring that the process is computationally secure.

## 4. **Technologies Used**

- **Python**: The programming language used to implement the blockchain system.
- **RSA (from the `rsa` library)**: A cryptographic system used for transaction signing and verification.
- **SHA-256**: A secure hashing algorithm used to generate block hashes and validate data integrity.

## 5. **How the System Works**

1. **Genesis Block**: The first block in the blockchain (the Genesis block) is created with hardcoded values.
2. **Transaction Creation**: Initially, transactions were simple entries where the sender and receiver's identities were not authenticated. Later, RSA encryption was added to sign transactions and ensure that only authorized users could create valid transactions.
3. **Transaction Verification**: Transactions are verified using the sender's RSA public key to ensure they haven’t been tampered with and are authentic.
4. **Mining**: Pending transactions are mined by solving a proof-of-work puzzle, ensuring that blocks are securely added to the blockchain.
5. **Block Addition**: Once a valid nonce is found through mining, the block with the verified transactions is added to the blockchain.

## 6. **How to Run the Project**

### **Prerequisites**
- Python 3.x
- `rsa` Python library (install via `pip install rsa`)

### **Steps to Run**
1. Download or clone the repository containing the code.
2. Install the required library:
   ```bash
   pip install rsa
   ```
3. Run the main Python script:
   ```bash
   python miniBlockChain_RSA.py
   ```
4. Follow the on-screen prompts to:
   - Add transactions (with RSA signing)
   - Mine pending transactions
   - Print the blockchain
   - Validate the blockchain



## 7. **Conclusion**

The **MiniBlockchain** project began as a simple blockchain implementation and evolved into a more secure and reliable system by incorporating **RSA encryption** for transaction signing and verification. This added security feature ensures that only authorized participants can submit valid transactions, making the system more robust and trustworthy.




