import struct

class DES:
    def __init__(self, key):
        if len(key) != 8:
            raise ValueError("Key must be exactly 8 bytes long")
        self.key = key

    def _process_block(self, block, encrypt=True):
        # Placeholder for a simple DES block processing (for educational purposes)
        # In real-world scenarios, you must use well-tested libraries like pycryptodome
        return block[::-1]  # Reverse block as a simple operation (not real DES)

    def encrypt(self, data):
        if len(data) % 8 != 0:
            raise ValueError("Data must be a multiple of 8 bytes")
        return b"".join(self._process_block(data[i:i+8]) for i in range(0, len(data), 8))

    def decrypt(self, data):
        if len(data) % 8 != 0:
            raise ValueError("Data must be a multiple of 8 bytes")
        return b"".join(self._process_block(data[i:i+8], encrypt=False) for i in range(0, len(data), 8))
