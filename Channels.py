from termcolor import colored
import math, random

def quantum_channel(sender, receiver, eavesdropper, length, generator, error):
    # Preparation, transmission, measurement
    sender.generate_bit_string(length, generator, error)
    sender.generate_basis(length, generator)

    receiver.generate_basis(length, generator)

    if eavesdropper != None:
        eavesdropper.generate_basis(length, generator)
        eavesdropper.measure_signal(sender)
        receiver.measure_signal(eavesdropper, length, error)
        return
    
    receiver.measure_signal(sender, length, error)

def bases_comparison(sender, receiver, length):
    print("Bases comparison: ", end="    ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
            print(colored("\u2714", "green"), end=" ")
        else: print(colored("X", "red"), end=" ") 
    print()

def public_channel(sender, receiver, length):
    # Sender (Alice) and receiver (Bob) publicly communicate the bases they used for qubit preparation and measurement
    bases_comparison(sender, receiver, length)

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
    information = 0
    print("Eve's information: ", end="   ")
    for _ in range(len(sender.basis)):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] == eavesdropper.basis[_]:
            information += 1
            
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_] and sender.basis[_] == eavesdropper.basis[_]:
            print(sender.bits[_], end=" ")
        else: print(" ", end=" ") 
    print()
    return information

def alice_shared_key(sender, receiver, length):
    key_length = 0
    print(f"Alice's shared key: ", end = "  ")
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            key_length += 1
  
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
                print(sender.bits[_], end=" ")
        else: print(" ", end=" ")
    print()
    return key_length

def bob_shared_key(sender, receiver, length): 
    print(f"Bob's shared key: ", end = "    ")
    for _ in range(length):
        if sender.basis[_] == receiver.basis[_]:
                print(receiver.bits_with_error[_], end=" ")
        else: print(" ", end=" ")
    print()

def eve_detection(sender, receiver):
    sus_bits_indexes = []
    detection = 0
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            sus_bits_indexes.append(_)

    for _ in range(0, len(sus_bits_indexes), 3):
        if sender.bits[sus_bits_indexes[_]] != receiver.bits_with_error[sus_bits_indexes[_]]:
            detection += 1

    print(f"With {math.floor((len(sus_bits_indexes)) / 3)} (out of {len(sus_bits_indexes)} filtered bits) sacrificed bits, Eve is detected {detection} times.")
    print(f"QBER (quantum bit error rate): {round(detection * 100 / len(sus_bits_indexes), 1)}%")

def printing_results(sender, receiver, eavesdropper, length):
    print()
    sender.print_bits(length)
    sender.print_basis(length)

    if eavesdropper != None:
        eavesdropper.print_measurement(sender, length)

    receiver.print_measurement(sender, length)  

    public_channel(sender, receiver, length)

    # Based on the agreed-upon bases, Alice filters out the bits where they used different bases
    key_length = alice_shared_key(sender, receiver, length)
    
    if eavesdropper != None:
        # Information that Eve gets and gets undetected
        information = eve_information(sender, receiver, eavesdropper, length)
        # Information that Eve gets and can get detected
        error = eve_error(sender, receiver, eavesdropper, length)

    # Based on the agreed-upon bases, Bob filters out the bits where they used different bases
    bob_shared_key(sender, receiver, length)

    print()
    if eavesdropper == None:
        print(f"Final shared key length: {key_length}")

    if eavesdropper != None:
        print(f"Eve introduces an error, with a 50% probability of being detected, {error * 100 / len(sender.bits)}% of the time.")
        print(f"Eve gets to know {round(information * 100 / key_length, 1)}% of the key.")
        eve_detection(sender, receiver)
    
    print()
