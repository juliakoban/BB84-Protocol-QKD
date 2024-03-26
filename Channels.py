from termcolor import colored
import math

def quantum_channel(sender, receiver, eavesdropper, length):
    # Preparation, transmission, measurement
    sender.generate_bit_string(length)
    sender.generate_basis(length)

    receiver.generate_basis(length)
    if eavesdropper != None:
        eavesdropper.generate_basis(length)
        eavesdropper.measure_signal(sender)
        receiver.measure_signal(eavesdropper)
        return
    receiver.measure_signal(sender)

def bases_comparison(sender, receiver, length):
    print("Bases comparison: ", end="    ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
            print(colored("\u2714", "green"), end=" ")
        else: print(colored("X", "red"), end=" ") 
    print()

def eve_error(sender, receiver, eavesdropper, length):
    error = 0
    print("Eve introduces error: ", end="")
    for _ in range(len(sender.basis)):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] != eavesdropper.basis[_]:
            error += 1

    for _ in range(length):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] != eavesdropper.basis[_]:
            print("Y", end=" ")
        else: print("N", end=" ") 
    print()
    return error

def eve_information(sender, receiver, eavesdropper, length):
    print("Eve's information: ", end="   ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] == eavesdropper.basis[_]:
            print(sender.bits[_], end=" ")
        else: print(" ", end=" ") 
    print()

def alice_shared_key(sender, receiver, length):
    print(f"Alice's shared key: ", end = "  ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
                print(sender.bits[_], end=" ")
        else: print(" ", end=" ")
    print()

def bob_shared_key(sender, receiver, length): 
    print(f"Bob's shared key: ", end = "    ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
                print(receiver.bits[_], end=" ")
        else: print(" ", end=" ")
    print()

def eve_detection(sender, receiver):
    sus_bits_indexes = []
    detection = 0
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            sus_bits_indexes.append(_)

    for _ in range(0, len(sus_bits_indexes), 3):
        if sender.bits[sus_bits_indexes[_]] != receiver.bits[sus_bits_indexes[_]]:
            detection += 1

    print(f"With {math.floor((len(sus_bits_indexes)) / 3)} (out of {len(sus_bits_indexes)} filtered bits) sacrificed bits, Eve is detected {detection} times.")

def printing_results(sender, receiver, eavesdropper):
    # Printing a part of results 
    length = math.floor(len(sender.bits) / 4)

    sender.print_bits(length)
    sender.print_basis(length)

    eavesdropper.print_measurement(sender, length)
    receiver.print_measurement(sender, length)

    # Sender (Alice) and receiver (Bob) publicly communicate the bases they used for qubit preparation and measurement
    bases_comparison(sender, receiver, length)
    # Based on the agreed-upon bases, Alice filters out the bits where they used different bases
    alice_shared_key(sender, receiver, length)
    # Information that Eve gets and gets undetected
    eve_information(sender, receiver, eavesdropper, length)
    # Information that Eve gets and can get detected
    error = eve_error(sender, receiver, eavesdropper, length)
    # Based on the agreed-upon bases, Bob filters out the bits where they used different bases
    bob_shared_key(sender, receiver, length)

    print(f"Eve introduces an error, with a 50% probability of being detected, {error * 100 / len(sender.bits)}% of the time.")
    eve_detection(sender, receiver)

def public_channel(sender, receiver, eavesdropper):
    printing_results(sender, receiver, eavesdropper)