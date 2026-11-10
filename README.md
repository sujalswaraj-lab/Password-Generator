# Random Password Generator

A beginner-friendly command-line password generator written in Python.

## Features

- Choose any password length (minimum 6 characters)
- Optionally include numbers and symbols
- Uses Python's `secrets` module, which is designed for security-sensitive randomness
- Validates input and asks again if something is wrong

## Requirements

- Python 3.6 or newer
- No extra libraries needed (`secrets` and `string` are built in)

## How to Run

```bash
python password_generator.py
```

On some systems you may need to use `python3` instead of `python`.

## Usage

The program asks for a length, then whether to include numbers and symbols (answer `y` or `n`).

```
=== Random Password Generator ===

Password length (at least 6): 12
Include numbers? (y/n): y
Include symbols? (y/n): y

Your password: X@pPBA^Eq-Gv
```

Your password will be different every time.

## How It Works

The `generate_password()` function builds a pool of characters: always letters, plus digits and symbols if you chose them. It then picks one character at random from that pool, repeating until the password reaches the requested length.

## Why `secrets` and not `random`?

The `random` module is predictable if someone knows how it was seeded, so it isn't safe for passwords. The `secrets` module uses the operating system's secure random source, which is the right choice for anything security-related.

## Ideas for Improvement

- Generate several passwords at once and let the user pick one
- Guarantee at least one letter, number and symbol in every password
- Add a "copy to clipboard" option
- Let the user choose which symbols are allowed
