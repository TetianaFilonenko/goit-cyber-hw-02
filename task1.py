from collections import Counter
import re
from utils import load_text_from_file


def vigenere_encrypt(plaintext, key):
    """
    Encrypts the given plaintext using the Vigenere cipher with the provided key.

    Parameters:
    plaintext (str): The plaintext to be encrypted.
    key (str): The key used for encryption.

    Returns:
    str: The encrypted text.
    """

    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    key = key.upper()
    encrypted_text = ""
    key_index = 0

    for char in plaintext:
        if char.isupper() and char in alphabet_upper:
            shift = alphabet_upper.index(key[key_index % len(key)])
            new_char = alphabet_upper[(alphabet_upper.index(char) + shift) % 26]
            encrypted_text += new_char
            key_index += 1
        elif char.islower() and char in alphabet_lower:
            shift = alphabet_upper.index(key[key_index % len(key)])
            new_char = alphabet_lower[(alphabet_lower.index(char) + shift) % 26]
            encrypted_text += new_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    """
    Decrypts a ciphertext using the Vigenere cipher with a given key.

    Parameters:
    ciphertext (str): The encrypted text to be decrypted.
    key (str): The key used for decryption.

    Returns:
    str: The decrypted text.

    """
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    key = key.upper()
    decrypted_text = ""
    key_index = 0

    for char in ciphertext:
        if char.isupper() and char in alphabet_upper:
            shift = alphabet_upper.index(key[key_index % len(key)])
            new_char = alphabet_upper[(alphabet_upper.index(char) - shift) % 26]
            decrypted_text += new_char
            key_index += 1
        elif char.islower() and char in alphabet_lower:
            shift = alphabet_upper.index(key[key_index % len(key)])
            new_char = alphabet_lower[(alphabet_lower.index(char) - shift) % 26]
            decrypted_text += new_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text


def friedman_test(ciphertext):
    """
    Calculates the index of coincidence (IC) and estimates the key length for a given ciphertext.

    Parameters:
    ciphertext (str): The ciphertext to analyze.

    Returns:
    tuple: A tuple containing the index of coincidence (IC) and the estimated key length.

    """
    ciphertext = "".join(re.findall(r"[A-Z]", ciphertext.upper()))
    letter_counts = Counter(ciphertext)

    N = sum(letter_counts.values())

    numerator = sum(count * (count - 1) for count in letter_counts.values())
    denominator = N * (N - 1)

    ic = numerator / denominator if denominator > 0 else 0

    estimated_key_length = (0.027 * N) / ((0.065 - ic) + (N * (ic - 0.038)))

    return ic, estimated_key_length


def main():
    """
    This function demonstrates the encryption and decryption process using the Vigenere cipher.
    It performs the following steps:
    1. Loads the plaintext from a file specified by the file_path variable.
    2. Encrypts the plaintext using the Vigenere cipher with the given key.
    3. Prints the encrypted ciphertext.
    4. Decrypts the ciphertext using the Vigenere cipher with the same key.
    5. Prints the decrypted plaintext.
    6. Performs the Friedman test on the ciphertext to estimate the key length.
    7. Prints the index of coincidence and the estimated key length.
    """
    file_path = "input_text.txt"
    plaintext = load_text_from_file(file_path)

    key = "CRYPTOGRAPHY"

    ciphertext = vigenere_encrypt(plaintext, key)
    print("Зашифрований текст (Рівень 1):")
    print(ciphertext)

    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("\nРозшифрований текст (Рівень 1):")
    print(decrypted_text)

    ic, estimated_key_length = friedman_test(ciphertext)
    print("\nТест Фрідмана (Рівень 2):")
    print(f"Індекс збігу: {ic}")
    print(f"Приблизна довжина ключа: {estimated_key_length:.2f}")


if __name__ == "__main__":
    main()
