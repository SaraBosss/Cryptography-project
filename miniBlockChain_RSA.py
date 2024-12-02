import hashlib
import time
import rsa  # Adding the rsa library for cryptography

class Block:
    """
    Represents a block in the blockchain. A block contains information like 
    its index, previous hash, timestamp, data, hash, and a nonce.
    """

    def __init__(self, index, prev_hash, timestamp, data, hash, nonce):
        self.index = index  # Index of the block in the chain
        self.prev_hash = prev_hash  # Hash of the previous block
        self.timestamp = timestamp  # Creation time of the block
        self.data = data  # Data contained in the block
        self.hash = hash  # Hash of the block
        self.nonce = nonce  # Nonce used for proof-of-work

    def to_string(self):
        """
        Converts the block to a readable string representation.
        """
        return f"Block {self.index} [Hash: {self.hash}]\nData: {self.data}\nPrevious Hash: {self.prev_hash}\nTimestamp: {self.timestamp}\nNonce: {self.nonce}\n"

class Blockchain:
    """
    Represents a blockchain with a list of blocks and a list of pending transactions.
    Each transaction can be signed and verified using RSA keys.
    """

    def __init__(self):
        """
        Initializes the blockchain with a genesis block and sets default parameters.
        """
        self.chain = [self.create_genesis_block()]  # Creates the genesis block
        self.pending_transactions = []  # List of pending transactions
        self.transaction_limit = 2  # Limit of transactions per block
        self.difficulty = 3  # Difficulty of the proof-of-work (number of leading zeros in the hash)

    def create_genesis_block(self):
        """
        Creates the Genesis Block (the first block in the blockchain).
        """
        timestamp = int(time.time())  # Current timestamp
        genesis_hash = self.calculate_hash(0, "0", timestamp, "Genesis Block", 0)
        return Block(0, "0", timestamp, "Genesis Block", genesis_hash, 0)

    def calculate_hash(self, index, prev_hash, timestamp, data, nonce):
        """
        Calculates the SHA-256 hash of a block based on its contents.
        """
        value = str(index) + prev_hash + str(timestamp) + data + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def get_latest_block(self):
        """
        Retrieves the most recent block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data, nonce):
        """
        Adds a block to the blockchain after validating the transactions.
        """
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())
        new_hash = self.calculate_hash(new_index, latest_block.hash, new_timestamp, data, nonce)
        new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash, nonce)
        self.chain.append(new_block)
        print(f"Block {new_index} added to the blockchain.")

    def add_transaction(self, sender, receiver, amount, sender_priv_key):
        """
        Adds a pending transaction after signing it.
        """
        # Check if the amount is a valid number
        if not amount.isdigit():
            print("Invalid amount. Please enter a valid number.")
            return

        # Create and sign the transaction with the sender's private key
        transaction = f"{sender} sends {amount} to {receiver}"
        signature = rsa.sign(transaction.encode(), sender_priv_key, 'SHA-256')

        # Add the signed transaction to the pending transactions list
        self.pending_transactions.append((transaction, signature))
        print(f"Transaction added: {transaction} | Signature: {signature.hex()}")

        # If the number of transactions exceeds the limit, the oldest one is removed
        if len(self.pending_transactions) > self.transaction_limit:
            self.pending_transactions.pop(0)
            print("Oldest transaction pruned.")

    def verify_transaction(self, transaction, signature, sender_pub_key):
        """
        Verifies the validity of a transaction using the sender's public key.
        """
        try:
            rsa.verify(transaction.encode(), signature, sender_pub_key)
            print(f"Transaction verified: {transaction}")
            return True
        except rsa.VerificationError:
            print(f"Transaction verification failed: {transaction}")
            return False

    def mine(self, alice_pub_key, bob_pub_key):
        """
        Mines the pending transactions into a new block.

        Args:
        alice_pub_key (rsa.PublicKey): Alice's public key for verifying transactions.
        bob_pub_key (rsa.PublicKey): Bob's public key for verifying transactions.
        """
        if not self.pending_transactions:
            print("No pending transactions to mine.")
            return

        # Verify transactions before adding them to the block
        valid_transactions = []
        for transaction, signature in self.pending_transactions:
            sender = transaction.split(' ')[0]  # Extract the sender's name
            if sender == "Alice":
                sender_pub_key = alice_pub_key
            else:
                sender_pub_key = bob_pub_key

            # Verify the validity of the transaction's signature
            if self.verify_transaction(transaction, signature, sender_pub_key):
                valid_transactions.append(transaction)
            else:
                print(f"Invalid transaction skipped: {transaction}")

        if not valid_transactions:
            print("No valid transactions to mine.")
            return

        nonce = 0
        while True:
            # Join all valid transactions into a single string
            transactions_data = " | ".join(valid_transactions)
            hash_attempt = self.calculate_hash(len(self.chain), self.get_latest_block().hash, int(time.time()), transactions_data, nonce)
            if hash_attempt.startswith('0' * self.difficulty):
                print(f"Nonce found: {nonce}")
                self.add_block(transactions_data, nonce)
                self.pending_transactions = []  # Clear transactions after mining
                print("Pending transactions mined into a new block.")
                break
            nonce += 1

    def is_chain_valid(self):
        """
        Verifies the integrity of the blockchain.

        Returns:
        bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]
            recalculated_hash = self.calculate_hash(
                current_block.index, current_block.prev_hash, current_block.timestamp, current_block.data, current_block.nonce
            )
            if current_block.hash != recalculated_hash:
                print(f"Block {i} has been tampered with.")
                return False
            if current_block.prev_hash != prev_block.hash:
                print(f"Block {i} has an invalid previous hash.")
                return False
        print("Blockchain is valid.")
        return True

    def print_chain(self):
        """
        Prints the entire blockchain.
        """
        for block in self.chain:
            print(block.to_string())

def main():
    """
    Main function to run the blockchain application.
    """
    # Generate public and private keys for Alice and Bob
    alice_pub_key, alice_priv_key = rsa.newkeys(512)
    bob_pub_key, bob_priv_key = rsa.newkeys(512)

    print("Mini Blockchain")
    print("1. Add Transaction")
    print("2. Mine Pending Transactions")
    print("3. Print Blockchain")
    print("4. Validate Blockchain")
    print("5. Exit")

    blockchain = Blockchain()
    alice_balance = 100
    bob_balance = 50

    while True:
        choice = input("Enter your choice: ")
        print()  # Add a newline after user input
        if choice == '1':
            sender = input("Enter sender (Alice/Bob): ")
            receiver = input("Enter receiver (Alice/Bob): ")
            amount = input("Enter amount: ")

            # Verify that the amount is a number
            try:
                amount = int(amount)  # Attempt to convert the amount to an integer
                if sender == "Alice" and alice_balance >= amount:
                    alice_balance -= amount
                    blockchain.add_transaction(sender, receiver, str(amount), alice_priv_key)
                elif sender == "Bob" and bob_balance >= amount:
                    bob_balance -= amount
                    blockchain.add_transaction(sender, receiver, str(amount), bob_priv_key)
                else:
                    print("Insufficient balance or invalid sender/receiver.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

            print(f"Alice's balance: {alice_balance}")
            print(f"Bob's balance: {bob_balance}")

        elif choice == '2':
            blockchain.mine(alice_pub_key, bob_pub_key)

        elif choice == '3':
            blockchain.print_chain()

        elif choice == '4':
            blockchain.is_chain_valid()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
        print()  # Add a newline between loop iterations

if __name__ == "__main__":
    main()

