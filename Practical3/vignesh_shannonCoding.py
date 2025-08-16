def shannon_fano(probabilities):
    # Normalize probabilities just in case
    total = sum(probabilities)
    if total == 0:
        raise ValueError("Sum of probabilities cannot be zero.")
    probabilities = [p / total for p in probabilities]

    def recursive_sf(p_list):
        if len(p_list) == 1:
            return ['0']
        elif len(p_list) == 2:
            return ['0', '1']

        # Sort in descending order and track original indices
        sorted_p = sorted(enumerate(p_list), key=lambda x: x[1], reverse=True)
        indices, p_sorted = zip(*sorted_p)

        # Find best place to split
        cumulative = [2 * sum(p_sorted[:i + 1]) - 1 for i in range(len(p_sorted))]
        split_index = min(range(len(cumulative)), key=lambda i: abs(cumulative[i]))

        if 0 < split_index < len(p_sorted) - 1:
            left = p_sorted[:split_index + 1]
            right = p_sorted[split_index + 1:]
            left_codes = recursive_sf(left)
            right_codes = recursive_sf(right)
            new_codes = ['0' + code for code in left_codes] + ['1' + code for code in right_codes]
        elif split_index == 0:
            left = [p_sorted[0]]
            right = p_sorted[1:]
            left_codes = recursive_sf(left)
            right_codes = recursive_sf(right)
            new_codes = left_codes + ['1' + code for code in right_codes]
        else:
            left = p_sorted[:-1]
            right = [p_sorted[-1]]
            left_codes = recursive_sf(left)
            right_codes = recursive_sf(right)
            new_codes = ['1' + code for code in left_codes] + right_codes

        # Reconstruct full code list in original order
        full_codes = [''] * len(p_list)
        for idx, code in zip(indices, new_codes):
            full_codes[idx] = code
        return full_codes

    # Generate the codewords
    codewords = recursive_sf(probabilities)

    # Compute the average codeword length
    average_length = sum(len(codewords[i]) * probabilities[i] for i in range(len(probabilities)))
    return codewords, average_length

if __name__ == "__main__":
    # Example: 5 symbols with given probabilities
    symbols = ['A', 'B', 'C', 'D', 'E']
    probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]

    # Ensure probabilities sum to 1
    if abs(sum(probabilities) - 1.0) > 1e-6:
        raise ValueError("Probabilities must sum to 1.")

    # Get codes and average length
    codewords, avg_length = shannon_fano(probabilities)

    # Display result
    print("Symbol\tProbability\tCode")
    for symbol, prob, code in zip(symbols, probabilities, codewords):
        print(f"{symbol}\t{prob:.2f}\t\t{code}")

    print(f"\nAverage Codeword Length: {avg_length:.4f} bits/symbol")
