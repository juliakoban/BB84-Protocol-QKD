import Alice, Bob, Channels, Eve

def main():
    alice = Alice.Alice()
    bob = Bob.Bob()
    eve = Eve.Eve()

    bit_string_length = 10

    Channels.quantum_channel(alice, bob, eve, bit_string_length)
    Channels.public_channel(alice, bob, eve)

if __name__ == "__main__":
    main()

# STEPS
# Alice generates a random bit string that she wants to transmit securely to Bob
# For each bit in her string, she randomly chooses a basis (either Rectilinear or Diagonal)
# Bob randomly chooses a basis for signal measurement
# If bases are the same, Bob receives the same bit, other way, there is a 50% chance of getting 0 or 1 bit
# Filtering the same bits to get sifted key