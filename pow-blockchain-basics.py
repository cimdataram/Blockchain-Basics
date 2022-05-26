from hashlib import sha256
import time
import random

# Predefine / Platzhalter / Genesis
blockchain = []
transactions = []
prev_hash = 0
index = 0
diff = 0
current_hash = ''

def _transactions(transactions):
    transactions = []
    for i in range(10):
        transaction = str(random.randint(1, 10))
        transactions.append(transaction)
    return transactions

def _calc_hash(index, transactions, timestamp, prev_hash):
    nonce = 0
    current_hash = ''
    diff = random.randint(1, 3)
    while not current_hash.startswith('0' * diff):
        nonce += 1
        to_be_hashed = str(index) + str(transactions) + str(timestamp) + str(prev_hash) + str(nonce)
        current_hash = sha256(to_be_hashed.encode('utf-8')).hexdigest()
    return current_hash

# create blockchain loop
while index < 10:
    transactions = _transactions(transactions)
    hash = _calc_hash(index, transactions, time.time(), prev_hash)
    block = [hash, index, transactions, time.time(), prev_hash]
    blockchain.append(block)
    #time.sleep(2)
    index += 1
    print(block)
    print()
    prev_hash = hash
    block = []
print(blockchain)
    
        
# TO DO 
    # hashes prüfen um manipulation vermeiden


