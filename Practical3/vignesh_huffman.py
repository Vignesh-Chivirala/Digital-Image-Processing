import heapq

class Node:
    def __init__(self, symbol=None, prob=0, left=None, right=None):
        self.symbol = symbol
        self.prob = prob
        self.left = left
        self.right = right

    # Comparison operator for heapq
    def __lt__(self, other):
        return self.prob < other.prob


def build_huffman_tree(symbols, probabilities):
    heap = [Node(symbol=s, prob=p) for s, p in zip(symbols, probabilities)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(prob=left.prob + right.prob, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]  # root of the tree


def generate_codes(node, prefix='', code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node.symbol is not None:
        code_dict[node.symbol] = prefix
    else:
        generate_codes(node.left, prefix + '0', code_dict)
        generate_codes(node.right, prefix + '1', code_dict)

    return code_dict


def huffman_coding(symbols, probabilities):
    root = build_huffman_tree(symbols, probabilities)
    code_dict = generate_codes(root)

    # Calculate average code length
    avg_length = sum(probabilities[i] * len(code_dict[symbols[i]]) for i in range(len(symbols)))
    return code_dict, avg_length


# === Example Usage ===
if __name__ == "__main__":
    # Example: 5 symbols with probabilities
    symbols = ['A', 'B', 'C', 'D']
    probabilities = [0.4, 0.3, 0.2, 0.1]

    # Ensure probabilities sum to 1
    if abs(sum(probabilities) - 1.0) > 1e-6:
        raise ValueError("Probabilities must sum to 1.")

    # Huffman coding
    codes, avg_length = huffman_coding(symbols, probabilities)

    # Display result
    print("Symbol\tProbability\tCode")
    for s in symbols:
        print(f"{s}\t{probabilities[symbols.index(s)]:.2f}\t\t{codes[s]}")

    print(f"\nAverage Codeword Length: {avg_length:.4f} bits/symbol")
