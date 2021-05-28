from hashlib import sha256


with open("sample.png", "r") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        sha256.update(chunk)
    hash = hash_md5.hexdigest()

def file_test():
    assert hash 
