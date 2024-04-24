import random

class Alice():
    def __init__(self):
        self.bits = []
        self.bits_with_error = []
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

    def generate_bit_string(self, length, generator, error):
        # User generates a random bit string that he wants to transmit securely
        self.bits = [generator.generate_bit() for _ in range(length)]

        self.bits_with_error = [self.bits[_] for _ in range(length)]
       
        if (error > 0):
            for bit in self.bits_with_error:
                number = random.randint(1, 101)
                if (number <= error and bit == 0):
                    bit = 1
                elif (number <= error and bit == 1):
                    bit = 0
    
    def generate_basis(self, length, generator):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be polarized
        self.basis = [generator.generate_base() for _ in range(length)]
