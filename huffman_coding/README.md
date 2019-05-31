# Huffman Coding

## Introduction
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

## Approach
- A dictionary will be used to store the each character's frequency from the given data.
- Then, the characters are sorted by frequency by using a priority queue and a tree is built from that priority queue.
- Finally, we will build a dictionary to store the code for each character, by recursively traversing the built Huffman tree, and encode the character from the data by using that code dictionary.

## Analysis
Let N be the total number of characters in the data.
- The time complexity of encoding data operation is O(NlogN), since we use a Priority Queue to help sorting the character's frequency, which takes time complexity of O(NlogN), in order to insert every character of the data into the priority queue. Besides that, we also use hash tables to store the initial frequencies and the encoded character, which takes O(N) time complexity overall.
- The time complexity of decoding data is O(N), in which we will iterate through all of the decoded data.
- The space complexity is O(N) overall.
