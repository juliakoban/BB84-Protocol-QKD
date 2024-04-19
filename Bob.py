import random
from termcolor import colored

class Bob:
    def __init__(self):
        self.basis = []
        self.bits = []
        self.basis_with_error = []
        
    def print_measurement(self, sender, length):
        print("Bob measures: ", end="        ")
        for _ in range(length):
            if sender.basis[_] == self.basis[_]:
                print(colored(self.basis[_], "green"), end=" ")
            else:
                print(colored(self.basis[_], "blue"), end=" ")  # blue color means that it is probabilistic
        print()

    def generate_basis(self, length):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be measured
        self.basis = [random.choice(["+", "x"]) for _ in range(length)]

    def measure_signal(self, sender):
        self.bits = [sender.bits[_] if sender.basis[_] == self.basis[_] else random.randint(0, 1) for _ in range(len(sender.bits))]

