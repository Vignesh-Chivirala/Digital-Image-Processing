#Count each character appearance
def count_frequencies(message):
    frequency = {}
    for char in message:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

#Create codes
def create_codes(frequency):
    #Sort characters by frequency (descending)
    sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    #Dictionary to store codes, initializing no code for every character
    codes = {char: '' for char, x in sorted_chars}

    def assign_codes(char_list):
        if len(char_list) <= 1:
            return

        # Split the list into two halves
        mid = len(char_list) // 2
        left = char_list[:mid]
        right = char_list[mid:]

        # Add '0' to left group codes
        for char, x in left:
            codes[char] += '0'
        # Add '1' to right group codes
        for char, x in right:
            codes[char] += '1'

        # Repeat
        assign_codes(left)
        assign_codes(right)

    assign_codes(sorted_chars)
    return codes

#Convert the message in codes
def encode_message(message, codes):
    encoded = ''
    for char in message:
        encoded += codes[char]
    return encoded

#Main
message = input("Enter your message: ")
frequencies = count_frequencies(message)
codes = create_codes(frequencies)
encoded_message = encode_message(message, codes)

#Show coded message
print("Character Codes:")
for char in codes:
    print(f"'{char}': {codes[char]}")

print(f"\nOriginal Message=>{message}")
print(f"\nEncoded Message=>{encoded_message}")


#Compression Efficiency
original_bits = len(message) * 8
compressed_bits = len(encoded_message)
compression_ratio = original_bits / compressed_bits

print(f"\nOriginal Size: {original_bits} bits")
print(f"Compressed Size: {compressed_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}:1")
