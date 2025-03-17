# Convert HTML to Markdown


def main(file_name): 
    try:
        with open(file_name, "r", errors="strict") as file:
            lines = file.readlines()
            print(lines)
        with open(f"{file_name.split(".")[0]}.md", "x") as file:
            ...
    except FileNotFoundError: 
        raise FileNotFoundError(f"""File {file_name} not found. Please make sure you have saved your file in the current directory and you have given the correct input.""")
    except FileExistsError:
        raise FileExistsError(f"""File {file_name} already exists.""")