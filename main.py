from blockchain import Blockchain

## Initialising Blockchain object
blockchain = Blockchain()

blockchain.add_new_block("First Block")
blockchain.add_new_block("Second Block")
blockchain.add_new_block("Third  Block")

for block in blockchain.get_blocks():
	print()
	print(block.to_string())
