from hashlib import sha256
from datetime import datetime

class Block():
## A block stores 3 components : the data written to it, the hash of the previous block
## and it's own hash

## Initialising the data structure of a block

	def __init__(self, data, previous_block_hash):
		self.data = data
		self.prev_block_hash = previous_block_hash
		self.hash = sha256(self.to_string().encode()).hexdigest()

	def is_hash_valid(self, hash):
		return (hash.startswith('0' * 3))

	def calculate_valid_hash(self):
		hash = ''
		nonce = 0

		while (not self.is_hash_valid(hash)):
			temp = self.to_string() + str(nonce)
			hash = sha356(temp.encode()).hexdigest()
			nonce += 1
		
		self.hash = hash

	def to_string(self):
		return "{0}\t{1}".format(self.data, self.prev_block_hash)
