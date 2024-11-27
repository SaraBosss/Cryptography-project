# Final Cryptography Project: Mini Blockchain with RSA Authentication - Documentation

## Table of Contents:
1. **Introduction**
2. **Project Overview**
3. **Key Concepts**
4. **Technologies Used**
5. **How the System Works**
6. **Code Structure**
7. **How to Run the Project**
8. **Transaction Verification with RSA**
9. **Security Features**
10. **Conclusion**
11. **Evolution of the Project**
12. **Future Work**

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

## 6. **Code Structure**

The code is organized into two main classes:
- **Block**: Represents a block in the blockchain with attributes such as `index`, `prev_hash`, `timestamp`, `data`, `hash`, and `nonce`.
- **Blockchain**: Manages the blockchain, adds transactions, verifies transaction signatures, and mines blocks using proof of work.

The methods in the **Blockchain** class have evolved over time:
- **Initial Methods**: Initially, methods for creating blocks, adding transactions, and printing the blockchain were implemented without any security measures.
- **RSA Integration**: Later methods like `add_transaction` and `verify_transaction` were updated to incorporate RSA encryption. Transactions are now signed with the sender's private key and verified using the sender's public key.

## 7. **How to Run the Project**

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
   python miniblockchain.py
   ```
4. Follow the on-screen prompts to:
   - Add transactions (with RSA signing)
   - Mine pending transactions
   - Print the blockchain
   - Validate the blockchain

## 8. **Transaction Verification with RSA**

The key improvement to the project was the addition of **RSA authentication** for verifying transactions.

1. **Transaction Creation**: When a transaction is created (e.g., "Alice sends 10 coins to Bob"), the sender signs the transaction using their **private RSA key**.
2. **Transaction Verification**: The recipient (or any node in the network) can verify the transaction by using the sender's **public RSA key**. This ensures that the transaction was signed by the correct party and hasn’t been tampered with.
3. **Authenticating Senders and Receivers**: By using RSA, the system guarantees that the senders and receivers of transactions are authenticated, ensuring that no unauthorized user can manipulate the blockchain.

## 9. **Security Features**

- **RSA Digital Signatures**: Transactions are signed with the sender's private RSA key, and only the sender's public key can verify it, preventing unauthorized changes.
- **Blockchain Integrity**: Blocks are linked together via hashes using SHA-256, ensuring data integrity and preventing tampering.
- **Proof of Work**: Mining ensures that adding a new block requires computational effort, making it difficult to alter the blockchain.

The introduction of RSA encryption significantly increased the **security** and **reliability** of the system by preventing unauthorized transactions and ensuring the authenticity of all transactions.

## 10. **Conclusion**

The **MiniBlockchain** project began as a simple blockchain implementation and evolved into a more secure and reliable system by incorporating **RSA encryption** for transaction signing and verification. This added security feature ensures that only authorized participants can submit valid transactions, making the system more robust and trustworthy.

By combining blockchain with RSA authentication, the project demonstrates how encryption can be used to enhance the security and integrity of distributed ledger systems.

## 11. **Evolution of the Project**

The project evolved as follows:
1. **Initial Phase (Basic Blockchain)**: The project started with basic blockchain functionality, where transactions were added to blocks without any authentication or encryption.
2. **Security Phase (Adding RSA Authentication)**: As the need for security became apparent, **RSA encryption** was integrated to allow for the signing and verification of transactions. This ensured that only authorized users could initiate transactions and that each transaction was verifiable by others.
3. **Current State (Fully Secured Blockchain)**: The system now includes fully verified transactions, where the sender’s private key signs the transaction and the receiver’s public key (or any participant’s public key) can verify it, ensuring a high level of security.

## 12. **Future Work**

- **Add More Participants**: The system could be extended to support more users, not just Alice and Bob, to simulate a more realistic blockchain network.
- **Enhanced Proof of Work**: The mining process could be made more challenging to simulate real-world blockchain mining difficulty.
- **GUI Implementation**: A graphical user interface could be developed to simplify interaction with the blockchain for non-technical users.

---

This documentation now clearly explains how the project started as a basic blockchain and how the **addition of RSA encryption** gradually improved security and transaction authenticity, ultimately creating a more reliable and secure **MiniBlockchain** system.# Cryptography-project
