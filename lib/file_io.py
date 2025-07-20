# lib/file_io.py

def write_file(file_name, file_content):
    """Writes content to a .txt file, overwriting if it exists."""
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """Appends content to a .txt file."""
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "a") as file:
        file.write(append_content)  # <-- removed the '\n'


def read_file(file_name):
    """Reads content from a .txt file and returns it."""
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "r") as file:
        return file.read()
