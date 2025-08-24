class ArithmeticCoding:
    def __init__(self, symbols, probabilities):
        if abs(sum(probabilities) - 1.0) > 1e-6:
            raise ValueError("Probabilities must sum to 1.")
        self.symbols = symbols
        self.probabilities = probabilities
        self.cumulative_probs = self._compute_cumulative_probs()

    def _compute_cumulative_probs(self):
        """Compute cumulative distribution for the symbols."""
        cumulative = {}
        cum_prob = 0.0
        for symbol, prob in zip(self.symbols, self.probabilities):
            cumulative[symbol] = (cum_prob, cum_prob + prob)
            cum_prob += prob
        return cumulative

    def encode(self, message):
        """Encode a message using arithmetic coding."""
        low, high = 0.0, 1.0
        for symbol in message:
            if symbol not in self.cumulative_probs:
                raise ValueError(f"Symbol {symbol} not in alphabet.")
            sym_low, sym_high = self.cumulative_probs[symbol]
            range_width = high - low
            high = low + range_width * sym_high
            low = low + range_width * sym_low
        # Final tag is any number between low and high
        return (low + high) / 2

    def decode(self, encoded_value, message_length):
        """Decode a message of given length using arithmetic coding."""
        decoded_message = []
        low, high = 0.0, 1.0
        for _ in range(message_length):
            value = (encoded_value - low) / (high - low)
            for symbol, (sym_low, sym_high) in self.cumulative_probs.items():
                if sym_low <= value < sym_high:
                    decoded_message.append(symbol)
                    range_width = high - low
                    high = low + range_width * sym_high
                    low = low + range_width * sym_low
                    break
        return decoded_message


# === Example Usage ===
if __name__ == "__main__":
    symbols = ['A', 'B', 'C', 'D']
    probabilities = [0.4, 0.3, 0.2, 0.1]

    ac = ArithmeticCoding(symbols, probabilities)

    message = ['A', 'D', 'B', 'A']
    print("Original Message:", message)

    # Encoding
    encoded_value = ac.encode(message)
    print("Encoded Value:", encoded_value)

    # Decoding
    decoded_message = ac.decode(encoded_value, len(message))
    print("Decoded Message:", decoded_message)
