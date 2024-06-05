import os
from tqdm import tqdm
import click
import hashlib


class Hasher:
    def __init__(self):
        self.hashing_algorithms = hashlib.algorithms_available
        self.wordlist = "wordlists/Top_1m_Passwords.txt"

    @staticmethod
    def validate(algorithm):
        if algorithm not in hashlib.algorithms_guaranteed:
            raise ValueError(f"Algorithm {algorithm} is not available")

    def list_algorithms(self):
        return f"Available algorithms: {', '.join(self.hashing_algorithms)}"

    def hash_pass(self, password, algorithm):
        self.validate(algorithm)
        h = hashlib.new(algorithm)
        h.update(password.encode())
        return f"Hash: {h.hexdigest()}"

    def hash_file(self, file, algorithm, blocksize=8192):
        self.validate(algorithm)
        h = hashlib.new(algorithm)
        with open(file, "rb") as f:
            for block in tqdm(
                iter(lambda: f.read(blocksize), b""), desc="Hashing file", unit="block"
            ):
                h.update(block)
        return f"Hash: {h.hexdigest()}"

    def hash_crack(self, hashed, algorithm):
        self.validate(algorithm)
        with open(self.wordlist, "r") as wordlist:
            total_passwords = sum(1 for _ in wordlist)
            wordlist.seek(0)
            for password in tqdm(
                wordlist, desc="Cracking hash", total=total_passwords, unit="password"
            ):
                password = password.strip()
                h = hashlib.new(algorithm)
                h.update(password.encode())
                if h.hexdigest() == hashed:
                    return f"Password: {password}"
        return "No match found."


@click.group()
def cli():
    pass


@cli.command()
def list_algorithms():
    hasher = Hasher()
    click.echo(hasher.list_algorithms())


@cli.command()
@click.argument("password")
@click.option(
    "--alg", default="sha256", help="Hashing algorithm to use. Default is sha256"
)
def hash_pass(password, alg):
    hasher = Hasher()
    click.echo(hasher.hash_pass(password, alg))


@cli.command()
@click.argument("file")
@click.option(
    "--alg", default="sha256", help="Hashing algorithm to use. Default is sha256"
)
def hash_file(file, alg):
    hasher = Hasher()
    if not os.path.isfile(file):
        raise FileNotFoundError(f"File {file} does not exist")

    click.echo(hasher.hash_file(file, alg))


@cli.command()
@click.argument("hash")
@click.option(
    "--alg", default="sha256", help="Hashing algorithm to use. Default is sha256"
)
def hash_crack(hash, alg):
    hasher = Hasher()
    click.echo(hasher.hash_crack(hash, alg))


if __name__ == "__main__":
    cli()
