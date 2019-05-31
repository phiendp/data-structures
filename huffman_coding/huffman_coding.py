import sys
from queue import PriorityQueue


class Node:
    def __init__(self, frequency, char):
        self.frequency = frequency
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequency(data):
    """
    Calculate the frequency of each character
    """
    freq_dict = {}
    for char in data:
        if freq_dict.get(char) != None:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


def build_priority_queue(freq_dict):
    """
    Use a priority queue to sort chars by frequency from lowest to highest
    """
    pq = PriorityQueue()
    for key in freq_dict:
        node = Node(freq_dict[key], key)
        pq.put(node)
    return pq


def build_huffman_tree(pq):
    while pq.qsize() > 1:
        element_one = pq.get()
        element_two = pq.get()

        sum = element_one.frequency + element_two.frequency
        node = Node(sum, '*')

        node.left = element_one
        node.right = element_two

        pq.put(node)
    return pq.get()


def build_code_dict(node, prefix, codes):
    if not node.left and not node.right:
        codes[node.char] = prefix

    if node.left:
        build_code_dict(node.left, prefix + '0', codes)
    if node.right:
        build_code_dict(node.right, prefix + '1', codes)

    return codes


def huffman_encoding(data):
    if data == None or data == '':
        return data, None

    frequency_dict = calculate_frequency(data)
    pq = build_priority_queue(frequency_dict)

    # Build Huffman tree from the priority queue
    huffman_tree = build_huffman_tree(pq)
    code_dict = build_code_dict(huffman_tree, '', {})

    # Encoding step
    encoded_data = ''
    for char in data:
        encoded_data += code_dict[char]

    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    decoded_data = ''
    node = tree
    for code in data:
        if code == '0':
            node = node.left
        elif code == '1':
            node = node.right

        if node.left is None and node.right is None:
            decoded_data += node.char
            node = tree

    return decoded_data


def test_1():
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


def test_2():
    test_sentence = "Python is awesome!"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(test_sentence)))
    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


def test_3():
    test_sentence = "Algorithm and data structure is fun!"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(test_sentence)))
    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
