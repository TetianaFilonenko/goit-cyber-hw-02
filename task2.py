from typing import List
from utils import load_text_from_file


def generate_key_from_word(word: str) -> List[int]:
    """
    Generate a permutation key from a given word by sorting the characters
    and mapping their original positions to the sorted positions.
    """
    word = word.upper()
    sorted_chars = sorted((char, i) for i, char in enumerate(word))
    key = [None] * len(word)

    for new_index, (char, original_index) in enumerate(sorted_chars):
        key[original_index] = new_index

    return key


def encrypt(message: str, key1: List[int], key2: List[int]) -> str:
    """
    Encrypt a message using two rounds of permutation cipher.
    First with key1 and then with key2.
    """
    message = message.upper()
    message_length = len(message)

    # First round of permutation with key1
    block_size1 = len(key1)
    encrypted_message = ""
    for i in range(0, message_length, block_size1):
        block = message[i : i + block_size1]
        rearranged_block = [block[digit] for digit in key1 if digit < len(block)]
        encrypted_message += "".join(rearranged_block)

    # Second round of permutation with key2
    block_size2 = len(key2)
    doubly_encrypted_message = ""
    for i in range(0, len(encrypted_message), block_size2):
        block = encrypted_message[i : i + block_size2]
        rearranged_block = [block[digit] for digit in key2 if digit < len(block)]
        doubly_encrypted_message += "".join(rearranged_block)

    return doubly_encrypted_message


def decrypt(encrypted_message: str, key1: List[int], key2: List[int]) -> str:
    """
    Decrypt a message that was encrypted using two rounds of permutation cipher.
    First reverse the permutation with key2, then with key1.
    """
    message_length = len(encrypted_message)

    # First reverse the second permutation with key2
    block_size2 = len(key2)
    partially_decrypted_message = ""
    for i in range(0, message_length, block_size2):
        block = encrypted_message[i : i + block_size2]
        original_block = [""] * len(block)
        for j, digit in enumerate(key2[: len(block)]):
            original_block[digit] = block[j]
        partially_decrypted_message += "".join(original_block)

    # Then reverse the first permutation with key1
    block_size1 = len(key1)
    fully_decrypted_message = ""
    for i in range(0, len(partially_decrypted_message), block_size1):
        block = partially_decrypted_message[i : i + block_size1]
        original_block = [""] * len(block)
        for j, digit in enumerate(key1[: len(block)]):
            original_block[digit] = block[j]
        fully_decrypted_message += "".join(original_block)

    return fully_decrypted_message


def main() -> None:
    """
    Driver function to read a message from a file, encrypt it using two permutation keys,
    and then decrypt it.
    """
    # Define the keys based on the words "SECRET" and "CRYPTO"
    key1 = generate_key_from_word("SECRET")
    key2 = generate_key_from_word("CRYPTO")

    plaintext = load_text_from_file("input_text.txt")

    encrypted_message = encrypt(plaintext, key1, key2)

    decrypted_message = decrypt(encrypted_message, key1, key2)

    print(f"Original message: {plaintext}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
