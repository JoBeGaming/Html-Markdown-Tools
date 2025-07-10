# Convert HTML to Markdown


def main(file_name): 
    try:
        with open(file_name, "r", errors="strict") as file:
            lines = file.readlines()
            lines = [line for line in lines if not line.startswith("<!")]
    except FileNotFoundError: 
        raise FileNotFoundError(f"""File {file_name} not found. Please make sure you have saved your file in the current directory and you have given the correct input.""")
    try:
        with open(rf"output\{file_name.split('.')[0]}.md", "x") as new_file:
            new_file.write("<!--Generated Markdown File-->\n")
            with open(rf"src\inline_style.html", "r") as style:
                style_list = style.readlines()
            new_file.write(style_list)
            previous_line = ""
            for line in lines: 
                convert(new_file, line, previous_line)
                previous_line = line
    except FileExistsError:
        raise FileExistsError(rf"""File {file_name.split(".")[0]}.md already exists at output\.""")

def convert(new_file, line, previous_line):
    line = line.removesuffix("\n")
    line = line.lstrip(" ")
    if line.startswith("<a href="): 
        line = line.removeprefix('<a href="')
        link = line.split('"')[0]
        text = line.split('"')[1].removeprefix(">").removesuffix("</a>")
        new_file.write(f"[{text}]({link})\n")
        new_file.write("\n")
    elif line.startswith("<h") and not (line.startswith("<head>") or line.startswith("<hr")): 
        heading_lvl = line.removeprefix("<h").split(">")[0]
        text = line.removeprefix(f"<h{heading_lvl}>").removesuffix(f"</h{heading_lvl}>")
        if int(heading_lvl) > 6: heading_lvl = 6
        prefixes = "#" * int(heading_lvl)
        new_file.write(f"{prefixes} {text}\n")
        new_file.write("\n")
    elif line.startswith("<hr>") and not (previous_line.startswith("<h") and not (previous_line.startswith("<head>") or previous_line.startswith("<hr"))):
        new_file.write("---\n")
    #elif line.startswith(): ...