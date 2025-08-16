#Count how many times each letter appears
def count_letters(text):
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

#Build the Huffman tree
def build_huffman_tree(counts):
    items = [[letter, count] for letter, count in counts.items()]

    while len(items) > 1:
        # Sort by count (ascending)
        items.sort(key=lambda x: x[1])

        # Take two smallest items
        first = items.pop(0)
        second = items.pop(0)

        # Make a new item as parent to first and second
        combined = [[first, second], first[1] + second[1]]
        items.append(combined)

    return items[0]

# Make codes for each letter by traversing the tree
def make_letter_codes(tree, current_code='', code_book=None):
    if code_book is None:
        code_book = {}

    # If current node is a single letter and not a group with children
    if isinstance(tree[0], str):
        code_book[tree[0]] = current_code
    else:
        # Go left (add '0') and right (add '1')
        make_letter_codes(tree[0][0], current_code + '0', code_book)
        make_letter_codes(tree[0][1], current_code + '1', code_book)

    return code_book

#Convert the message
def encode_text(text, code_book):
    result = ''
    for letter in text:
        result += code_book[letter]
    return result

#Main
text = input("Enter your message: ")
letter_counts = count_letters(text)
if len(letter_counts) <= 1:
    print("Input message must contain at least two different letters.")
else:    
    tree = build_huffman_tree(letter_counts)
    codes = make_letter_codes(tree)
    encoded_text = encode_text(text, codes)
    #Print Output
    print("Letter Codes:")
    for letter in codes:
        print(f"{letter}=>{codes[letter]}")

    print("\nOriginal Text=>")
    print(text)

    print("\nEncoded Text=>")
    print(encoded_text)

#Compression Efficiency
original_bits = len(text) * 8
compressed_bits = len(encoded_text)
compression_ratio = original_bits / compressed_bits

print(f"\nOriginal Size: {original_bits} bits")
print(f"Compressed Size: {compressed_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}:1")
