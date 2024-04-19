
class Alice():
    def __init__(self):
        self.bits = []
        self.basis = []
        self.basis_with_error = []
        
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

    def generate_bit_string(self, length, generator):
        # User generates a random bit string that he wants to transmit securely
        self.bits = [generator.generate_bit() for _ in range(length)]
    
    def generate_basis(self, length, generator):
        # User randomly choose a basis (either Rectilinear or Diagonal)
        # The choice of basis determines how the qubit will be polarized
        self.basis = [generator.generate_base() for _ in range(length)]