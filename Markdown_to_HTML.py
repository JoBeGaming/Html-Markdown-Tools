# Convert Markdown to HTML


def main(file_name): 
    try:
        with open(file_name, "r", errors="strict") as file:
            lines = file.readlines()
        with open(rf"src\inline_style.html", "r") as style:
            style_list = style.readlines()
            style.write(style_list)
    except FileNotFoundError: 
        raise FileNotFoundError(f"""File {file_name} not found. Please make sure you have saved your file in the current directory and you have given the correct input.""")
    try:
        with open(rf"output\{file_name.split('.')[0]}.html", "x") as file:
            ...
    except FileExistsError:
        raise FileExistsError(rf"""File {file_name.split(".")[0]}.html already exists at outputs\.""")