class Qrng:
    def __init__(self):
        self.input_file = open("./qrng_files/QNGFile.dat", "rb") # read binary

    def update_file(self):
        self.input_file.close()
        self.input_version += 1
        file_name = "./qrng_files/QNGFile{}.dat".format(self.input_version)
        self.input_file = open(file_name, "rb")
    
    def get_byte_from_file(self):
        byte = self.input_file.read(1)
        if not byte:
            self.update_file()
            byte = self.input_file.read(1)
        return int.from_bytes(byte, byteorder='big') 
    
    def generate_bit(self):
        byte = self.get_byte_from_file()
        if byte / 255.0 < 0.5: # only generating numbers from 0 to 1
            return 0
        return 1
    
    def generate_base(self):
        byte = self.get_byte_from_file()
        if byte % 2 == 0: 
            return "+"
        return "x"

