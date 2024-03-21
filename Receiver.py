import random

class Receiver():
    def __init__(self):
        self.basis = []
        self.results = []

    def generate_basis(self, length):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be measured
        self.basis = [random.choice(["+", "x"]) for _ in range(length)]
        print(f"Receiver's basis: {self.basis}")

    def measure_signal(self, sender):
        self.results = [sender.bits[_] if sender.basis[_] == self.basis[_] else random.randint(0, 1) for _ in range(len(sender.bits))]
        print(f"Measured signal: {self.results}")