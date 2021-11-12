#
# Blockchain
#

import hashlib, time
from datetime import datetime

class Block:
      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash()
            self.next = None

      def calc_hash(self):
            sha = hashlib.sha256()
            hash_str = f"{self.timestamp} {self.data} {self.previous_hash}".encode('utf-8')
            sha.update(hash_str)

            return sha.hexdigest()

      def get_previous_hash(self):
            return self.previous_hash

      def set_next(self, node):
            self.next = node

      def get_next(self):
            return self.next

      def get_hash(self):
            return self.hash

      def get_data(self):
            return self.data

      def __str__(self):
            block_str = f"{self.timestamp}\t{self.data}\t{self.hash}"

            return block_str
      
class Blockchain:
      def __init__(self):
            self.head = None
            self.tail = None
            self.count = 0

      def add_block(self, data):
            if self.tail:
                  node = Block(datetime.utcnow(), data, self.tail.get_hash())
                  self.tail.set_next(node)
                  self.tail = node
            else:
                  node = Block(datetime.utcnow(), data, 0)
                  self.head = node
                  self.tail = node
            self.count += 1

      def verify_blockchain(self):
            curr = self.head

            while curr:
                  calculated_hash = curr.calc_hash()
                  if curr.get_next():
                        stored_hash = curr.get_next().get_previous_hash()
                  else:
                        # last node
                        stored_hash = curr.get_hash()
                  if calculated_hash != stored_hash:
                        print(f"Calculated hash: {calculated_hash}")
                        print(f"Stored hash: {stored_hash}")
                        # raise AssertionError(f"Block Modified: {curr}")
                        print(f"WARNING!! Block modified > {curr}")

                  curr = curr.get_next()

      def find(self, data):
            curr = self.head
            node = None

            while curr:
                  if curr.get_data() == data:
                        node = curr
                        break
                  curr = curr.get_next()

            return node

      def __str__(self):
            blockchain_str = str()
            curr = self.head

            while curr:
                  blockchain_str += f"{curr}\n"
                  curr = curr.get_next()

            return blockchain_str

#
# Main
#
if __name__ == '__main__':
      blockchain = Blockchain()
      for i in range(10):
            blockchain.add_block(f"data {i}")

      # print(blockchain)
      blockchain.verify_blockchain()

      # Test 0: 
      node = blockchain.find('data 0')
      if node:
            node.data = 'data 99'
      blockchain.verify_blockchain()

      # Test 1: 
      node = blockchain.find('data 4')
      if node:
            node.data = 'data 99'
      blockchain.verify_blockchain()

      # Test 2: 
      node = blockchain.find('data 9')
      if node:
            node.data = 'data 99'
      blockchain.verify_blockchain()