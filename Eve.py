import random
from termcolor import colored

class Eve():
    def __init__(self):
        self.bits = []
        self.basis = []
    
    def print_measurement(self, sender):
        print("Eve measures: ", end="        ")
        for _ in range(len(sender.bits)):
            if sender.basis[_] == self.basis[_]:
                print(colored(self.basis[_], "green"), end=" ")
            else: print(colored(self.basis[_], "blue"), end=" ") # blue color means that it is probabilistic
        print()

    def print_basis(self, length):
        print(f"Eve's basis: ", end="         ")
        for _ in range(length):
            print(self.basis[_], end=" ")
        print()

    def generate_basis(self, length):
        self.basis = [random.choice(["+", "x"]) for _ in range(length)]
        # self.print_basis(length)
    
    def measure_signal(self, sender):
        # When Eavesdropper is measuring the signal, she is destroying the photons, so she needs to generate a new bit string to send to bob
        self.bits = [sender.bits[_] if sender.basis[_] == self.basis[_] else random.randint(0, 1) for _ in range(len(sender.bits))]
        self.print_measurement(sender)