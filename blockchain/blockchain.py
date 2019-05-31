import datetime
import hashlib


class Node:
    def __init__(self, block, previous=None):
        self.block = block
        self.previous = previous


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        previous_hash = None
        if self.tail:
            previous_hash = self.tail.block.hash

        block = Block(data, previous_hash)
        node = Node(block,  self.tail)

        if self.head == None:
            self.head = node
        else:
            block.previous = self.tail
            block.previous_hash = self.tail.block.hash

        self.tail = node


def test_blockchain():
    chain = BlockChain()

    chain.add_block("Sample test data")
    assert chain.tail == chain.head
    assert chain.tail.block.previous_hash == None
    first_block_hash = chain.tail.block.hash

    chain.add_block("Add new data")
    assert chain.tail != chain.head
    assert chain.tail.block.previous_hash != None

    second_block_hash = chain.tail.block.hash
    second_block_prev_hash = chain.tail.block.previous_hash
    assert first_block_hash == second_block_prev_hash
    assert second_block_hash != second_block_prev_hash

    print("Tests passed!")


if __name__ == "__main__":
    test_blockchain()
