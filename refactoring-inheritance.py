# Base storage class defining the interface for reading and writing data
class Storage:
    def read_data(self):
        pass
        
    def write_data(self, data):
        pass


# Writable storage implementation
class WritableStorage(Storage):
    def __init__(self, name):
        self.name = name
        
    def write_data(self, data):
        print(f"Writing to {self.name}: {data}")


# Readable storage implementation
class ReadableStorage(Storage):
    def __init__(self, name):
        self.name = name 
    
    def read_data(self):
        print(f"Reading data from {self.name}")


# File supports both reading and writing
class File(WritableStorage, ReadableStorage):
    def __init__(self, name):
        super().__init__(name)
        

# Read-only file supports only reading
class ReadOnlyFile(ReadableStorage):
    def __init__(self, name):
        super().__init__(name)


# Process a file by reading and writing to it
def process_file(file):
    file.read_data()
    file.write_data("Some data")


def main():
    regular_file = File("document.txt")
    readonly_file = ReadOnlyFile("readonly.txt")

    print("Processing regular file:")
    process_file(regular_file)

    print("\nProcessing readonly file:")
    process_file(readonly_file)


if __name__ == "__main__":
    main()
