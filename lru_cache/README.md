# LRU Cache

## Introduction
Design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

## Basic usecase
- In case of a cache hit, your get() operation should return the appropriate value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

## Approach
In order to have each operation taking O(1) time, we will use a doubly linked nodes, which will be stored in 2 different data structures:
- A queue: reference on the node's usage. Whenever the queue hits its maximum capacity, we will remove the least recently use node from both the queue and the dictionary below.
- A hash table (dictionary): to store the given key and a node as that key's value.

## Analysis
- The get operation will retrieve the node by its key from the hash table, with lookup time is O(1), or constant time.
- In case of cache hit, the node will be moved to the tail of the queue, which also takes O(1) complexity.
- The set operation will take O(1) time compelxity for both the hash table lookup, and inserting the node into queue in case of the node is not available in the hash table.
- Overall, the time compelxity is O(1), and the space complexity is O(N).
