import hashlib

text = "Hello, world"
hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()
print("SHA Hash of ", text, "is", hash_digest)


def hash_file(file_path):
    h = hashlib.new('sha256')
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print(f"\nChecking integrity between {file1} and {file2}")
    if hash1 == hash2:
        return "File is intact no modification have been made"
    return "File have been modified. Possibly unsafe"
    

if __name__ == "__main__":
    file_path = "/home/codesignature/Desktop/cryptography_with_python/sample files/sample.txt"
    print(f"SHA Hash of file {file_path} is {hash_file(file_path)}")
    print(verify_integrity(r"/home/codesignature/Desktop/cryptography_with_python/sample files/shapes.svg", r"/home/codesignature/Desktop/cryptography_with_python/sample files/shapes copy.svg"))
    print(verify_integrity(r"/home/codesignature/Desktop/cryptography_with_python/sample files/shapes.svg", r"/home/codesignature/Desktop/cryptography_with_python/sample files/circle.svg"))