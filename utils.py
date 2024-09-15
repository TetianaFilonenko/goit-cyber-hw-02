def load_text_from_file(file_path):
    """
    Load text from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
