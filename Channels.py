def quantum_channel(sender, receiver, length):
    # Preparation, transmission, measurement
    sender.generate_bit_string(length)
    sender.generate_basis(length)
    receiver.generate_basis(length)
    receiver.measure_signal(sender)

def sifted_key(sender, receiver):
    sifted_key = []
    for _ in range(len(sender.bits)):
        if sender.basis[_] == receiver.basis[_]:
            sifted_key.append(sender.bits[_])
        continue
    print(f"Sifted key: {sifted_key}")

def public_channel(sender, receiver):
    # Sender (Alice) and receiver (Bob) publicly communicate the bases they used for qubit preparation and measurement
    # Based on the agreed-upon bases, they filter out the bits where they used different bases
    sifted_key(sender, receiver)