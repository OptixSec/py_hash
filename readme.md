# Python Hashing

A simple CLI tool for generating hashes from strings or files and cracking hashes using a wordlist.

## Dependencies

* click
* tqdm

## Usage

> **NOTE**: Default hashing algorithm is sha256. Use the ```-alg``` argument to specify a different algorithm.

> **NOTE** View a list of the available algorithms at the bottom of this readme.

### Generate a hash from a string

```bash
python app.py hash-pass mypassword
python app.py hash-pass -alg sha512 mypassword
```

### Generate a hash from a file

```bash
python app.py hash-file /file/myfile.zip
python app.py hash-file -alg sha512 /file/myfile.zip mypassword
```

### Hash cracking with a wordlist

> **IMPORTANT**: Set the ```self.wordlist = ""``` variable inside the init of the ```Hasher()``` to the path of the wordlist you want to use.

```bash
python app.py hash-crack b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32
python app.py hash-crack -alg sha512 b822f1cd2dcfc685b47e83e3980289fd5d8e3ff3a82def24d7d1d68bb272eb32d
```

### Available Hashing Algorithms

* ripemd160
* blake2s
* shake_128
* sha3_384
* blake2b
* sha256
* sha3_224
* sm3
* sha1
* md5-sha1
* sha3_512
* sha512_224
* md5
* sha224
* sha512
* sha384
* sha3_256
* shake_256
* sha512_256