import random

class Sender():
    def __init__(self):
        self.bits = []
        self.basis = []

    def generate_bit_string(self, length):
        # User generates a random bit string that he wants to transmit securely
        self.bits = [random.randint(0, 1) for _ in range(length)]
        print(f"Sender's bits: {self.bits}")

    def generate_basis(self, length):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be polarized
        self.basis = [random.choice(["+", "x"]) for _ in range(length)]
        print(f"Sender's basis: {self.basis}")