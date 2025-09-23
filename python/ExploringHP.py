import getpass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import sys
from pynput.keyboard import Key, Listener

ph = PasswordHasher()

print("------Creating a password------")
pw = getpass.getpass("Password: ")
if key.char:
    sys.stdout.write('*')
hp = ph.hash(pw)

print("------Verifying the password------")
pw2 = getpass.getpass("Enter password to verify: ")

try:
    ph.verify(hp, pw2)
    print("Verification successful!")
except VerifyMismatchError:
    print("Wrong password")