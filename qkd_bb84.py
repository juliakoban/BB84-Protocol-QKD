import Alice, Bob, Eve, Channels, Qrng

def main():
    qrng_generator = Qrng.Qrng()
    alice = Alice.Alice()
    bob = Bob.Bob()
    eve = Eve.Eve()

    bit_string_length = 1000
    printing_length = 20
    error = 5 # in %

    # change eve to None in order to see results without eavesropping
    Channels.quantum_channel(alice, bob, eve, bit_string_length, qrng_generator) 
    Channels.printing_results(alice, bob, eve, printing_length)

if __name__ == "__main__":
    main()