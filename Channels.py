from termcolor import colored

def quantum_channel(sender, receiver, eavesdropper, length):
    # Preparation, transmission, measurement
    sender.generate_bit_string(length)
    sender.generate_basis(length)

    if eavesdropper != None:
        eavesdropper.generate_basis(length)
        eavesdropper.measure_signal(sender)
    
    receiver.generate_basis(length)
    receiver.measure_signal(sender)

def bases_comparison(sender, receiver):
    print("Bases comparison: ", end="    ")
    for _ in range(len(sender.basis)):
        if sender.basis[_] == receiver.basis[_]:
            print(colored("\u2714", "green"), end=" ")
        else: print(colored("X", "red"), end=" ") 
    print()

def eve_error(sender, receiver, eavesdropper):
    print("Eve introduces error: ", end="")
    for _ in range(len(sender.basis)):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] != eavesdropper.basis[_]:
            print("Y", end=" ")
        else: print("N", end=" ") 
    print()

def eve_information(sender, receiver, eavesdropper):
    print("Eve's information: ", end="   ")
    for _ in range(len(sender.basis)):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] == eavesdropper.basis[_]:
            print(sender.bits[_], end=" ")
        else: print(" ", end=" ") 
    print()

def shared_key(sender, receiver):
    shared_key = []
    error = 0

    print(f"Shared key: ", end = "          ")
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            if sender.bits[_] != receiver.bits[_]:
                error += 1
            else: 
                shared_key.append(receiver.bits[_])
                print(receiver.bits[_], end=" ")
        else: print(" ", end=" ")
    print()
    print(f"Error rate: {error/len(sender.bits)}")

def public_channel(sender, receiver, eavesdropper):
    # Sender (Alice) and receiver (Bob) publicly communicate the bases they used for qubit preparation and measurement
    bases_comparison(sender, receiver)

    eve_information(sender, receiver, eavesdropper)
    eve_error(sender, receiver, eavesdropper)
    # Based on the agreed-upon bases, they filter out the bits where they used different bases
    # shared_key(sender, receiver)