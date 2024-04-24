import random
from termcolor import colored

class Eve():
    def __init__(self):
        self.bits = []
        self.basis = []
    
    def print_measurement(self, sender, length):
        print("Eve measures: ", end="        ")
        for _ in range(length):
            if sender.basis[_] == self.basis[_]:
                print(colored(self.basis[_], "green"), end=" ")
            else: print(colored(self.basis[_], "blue"), end=" ") # blue color means that it is probabilistic
        print()

    def generate_basis(self, length, generator):
        self.basis = [generator.generate_base() for _ in range(length)]
        
    
    def measure_signal(self, sender):
        # When Eavesdropper is measuring the signal, she is destroying the photons, so she needs to generate a new bit string to send to bob
        self.bits = [sender.bits_with_error[_] if sender.basis[_] == self.basis[_] else random.randint(0, 1) for _ in range(len(sender.bits))]