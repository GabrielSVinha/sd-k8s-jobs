from hashlib import sha256
from random import choice, randint
from string import ascii_letters
from string import digits
import sys

LETTERS = ascii_letters + digits


def check_string(string, prefix):
    """Checks if the given string's hash starts with the given prefix."""
    h = sha256(string).hexdigest()
    if h.startswith(prefix):
        print("found! string: %s with sha256sum %s" % (string, h))
        return True


def generate_string():
    """Generates a random string with size between 1 and 8."""
    return ''.join(choice(LETTERS) for _ in range(randint(1, 9)))


def run(prefix, m):
    tries = 0
    max_tries = int(m)
    while tries < max_tries:
        a = generate_string()
        tries += 1
        if check_string(a, prefix):
            print("success with %d tries" % tries)
            return True

    # NOTE(clenimar): if we can't find what we're looking for, break.
    # This way we make sure that only an instance that completes the
    # work will finish.
    raise Exception("max tries reached. sorry.")


if __name__ == '__main__':
    run(prefix=sys.argv[1], m=sys.argv[2])
