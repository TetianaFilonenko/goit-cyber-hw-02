from task1 import vigenere_decrypt, vigenere_encrypt
from utils import load_text_from_file


def create_polybius_square(key):
    """
    Create a Polybius square based on a given key.

    Args:
        key (str): The key used to generate the Polybius square.

    Returns:
        list: A 5x5 matrix representing the Polybius square.

    Example:
        >>> create_polybius_square("KEYWORD")
        [['K', 'E', 'Y', 'W', 'O'],
         ['R', 'D', 'A', 'B', 'C'],
         ['F', 'G', 'H', 'I', 'L'],
         ['M', 'N', 'P', 'Q', 'S'],
         ['T', 'U', 'V', 'X', 'Z']]
    """
    key = key.upper().replace("J", "I")  # Treat J and I as the same
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Alphabet without J
    square = []
    used_chars = set()

    # Fill the square with the key, avoiding duplicates
    for char in key:
        if char not in used_chars and char in alphabet:
            square.append(char)
            used_chars.add(char)

    # Fill the rest of the square with remaining letters
    for char in alphabet:
        if char not in used_chars:
            square.append(char)
            used_chars.add(char)

    # Convert the flat list to a 5x5 matrix
    square_matrix = [square[i : i + 5] for i in range(0, 25, 5)]
    return square_matrix


def polybius_encrypt(text, square):
    """
    Encrypts the given text using the Polybius square cipher.

    Parameters:
    - text (str): The text to be encrypted.
    - square (list): The Polybius square used for encryption.

    Returns:
    - encrypted_text (str): The encrypted text.

    Example:
    >>> square = [['A', 'B', 'C', 'D', 'E'],
    ...           ['F', 'G', 'H', 'I', 'K'],
    ...           ['L', 'M', 'N', 'O', 'P'],
    ...           ['Q', 'R', 'S', 'T', 'U'],
    ...           ['V', 'W', 'X', 'Y', 'Z']]
    >>> polybius_encrypt("HELLO", square)
    '3244315133'
    """
    text = text.upper().replace("J", "I")  # Treat J as I
    encrypted_text = ""

    # Build a lookup table for the square
    lookup = {}
    for i, row in enumerate(square):
        for j, char in enumerate(row):
            lookup[char] = f"{i + 1}{j + 1}"

    # Encrypt the message
    for char in text:
        if char in lookup:
            encrypted_text += lookup[char]
        else:
            encrypted_text += char  # Preserve non-alphabetic characters

    return encrypted_text


def polybius_decrypt(encrypted_text, square):
    """
    Decrypts an encrypted text using the Polybius square.

    Parameters:
    - encrypted_text (str): The text to be decrypted.
    - square (list): The Polybius square used for decryption.

    Returns:
    - decrypted_text (str): The decrypted text.
    """
    decrypted_text = ""

    # Create a reverse lookup table
    reverse_lookup = {}
    for i, row in enumerate(square):
        for j, char in enumerate(row):
            reverse_lookup[f"{i + 1}{j + 1}"] = char

    # Decrypt the message
    i = 0
    while i < len(encrypted_text):
        if encrypted_text[i:i+2].isdigit():  # Ensure you are processing two digits
            decrypted_text += reverse_lookup.get(encrypted_text[i:i+2], "")
            i += 2
        else:
            decrypted_text += encrypted_text[i]  # Keep spaces and non-alphabetic characters
            i += 1

    return decrypted_text


def level2_encrypt(plaintext, vigenere_key, table_key):
    """
    Encrypts the plaintext using Vigenere encryption and table encryption.
    # """
    # vigenere_encrypted = vigenere_encrypt(plaintext, vigenere_key)
    table_encrypted = polybius_encrypt(plaintext, table_key)
    return table_encrypted


def level2_decrypt(ciphertext, vigenere_key, table_key):
    """
    Decrypts the given ciphertext using a combination of table cipher and Vigenere cipher.
    """
    table_decrypted = polybius_decrypt(ciphertext, table_key)
    # vigenere_decrypted = vigenere_decrypt(table_decrypted, vigenere_key)
    return table_decrypted


def main() -> None:
    """
    Entry point of the program.
    This function loads the plaintext from a file, encrypts it using the Vigenere cipher and a table key,
    and then decrypts the encrypted text. The encrypted and decrypted texts are printed to the console.
    """
    vigenere_key = "CRYPTO"
    table_key = "MATRIX"
    plaintext = load_text_from_file("input_text.txt")

    encrypted_text = level2_encrypt(plaintext, vigenere_key, table_key)
    print(f"Зашифрований текст: {encrypted_text}")

    decrypted_text = level2_decrypt(encrypted_text, vigenere_key, table_key)
    print(f"Розшифрований текст: {decrypted_text}")


if __name__ == "__main__":
    main()
