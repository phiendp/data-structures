# Blockchain

## Introduction
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Approach
There are 3 data structures that are used to build the blockchain solution:
- Node: each node contains a block data, with the link to the previous node.
- Block: a block contains the data (already hashed), its creation timestamp, and a hash to its previous block.
- Blockchain: a singly linked list with pointers to head and tail.

## Analysis
- The hash calculation will take O(N) time complexity, in which N is the total characters (size) of the block data, which will be processed during hashing.
- Adding a block to the block chain will take O(1) time complexity, in which the block will be appended to the linked list.
- Space complexity will take O(N), in which N is the size of the block data.
