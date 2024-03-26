import random

class Alice():
    def __init__(self):
        self.bits = []
        self.basis = []

    def print_bits(self, length):
        print(f"Initial bit sequence: ", end="")
        for _ in range(length):
            print(self.bits[_], end=" ")
        print()

    def print_basis(self, length):
        print(f"Alice encodes: ", end = "       ")
        for _ in range(length):
            print(self.basis[_], end=" ")
        print()

    def generate_bit_string(self, length):
        # User generates a random bit string that he wants to transmit securely
        self.bits = [random.randint(0, 1) for _ in range(length)]

    def generate_basis(self, length):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be polarized
        self.basis = [random.choice(["+", "x"]) for _ in range(length)]