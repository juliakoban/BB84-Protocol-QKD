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


def sifted_key(sender, receiver):
    sifted_key = []
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            sifted_key.append(sender.bits[_])
        continue
    print(f"Sifted key: {sifted_key}")

def quantum_channel(sender, receiver, length):
    # Preparation, transmission, measurement
    sender.generate_bit_string(length)
    sender.generate_basis(length)
    receiver.generate_basis(length)
    receiver.measure_signal(sender)

def public_channel(sender, receiver):
    # Sender (Alice) and receiver (Bob) publicly communicate the bases they used for qubit preparation and measurement
    # Based on the agreed-upon bases, they filter out the bits where they used different bases
    sifted_key(sender, receiver)

def main():
    alice = Sender()
    bob = Receiver()
    bit_string_length = 10

    quantum_channel(alice, bob, bit_string_length)
    public_channel(alice, bob)

if __name__ == "__main__":
    main()

# STEPS
# Alice generates a random bit string that she wants to transmit securely to Bob
# For each bit in her string, she randomly chooses a basis (either Rectilinear or Diagonal)
# Bob randomly chooses a basis for signal measurement
# If bases are the same, Bob receives the same bit, other way, there is a 50% chance of getting 0 or 1 bit
# Filtering the same bits to get sifted key