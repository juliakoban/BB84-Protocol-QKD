import Alice, Bob, Eve, Channels

def main():
    alice = Alice.Alice()
    bob = Bob.Bob()
    eve = Eve.Eve()

    bit_string_length = 1000
    printing_length = 20
    error = 5

    Channels.quantum_channel(alice, bob, None, bit_string_length)
    Channels.printing_results(alice, bob, None, printing_length)

if __name__ == "__main__":
    main()