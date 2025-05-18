# tools.py
# Gets user input and tries to convert it to the other format
# NOTE: Comments will be deleted, and the new file will not be commented!
# NOTE: For Valid HTML-Files, check /examples/example.html
# NOTE: Generated Markdown will not follow markdownlint rules!

#DEBUG
from pathlib import Path
for file in Path(".").rglob("main.md"):
    file.unlink()


if not __name__ == "__main__": 
    raise ImportError("Please don't try to import tools.py")

print("Please input your file, with the file extension")
user_input = input()
try:
    file_name = user_input.split(".")[0]
    file_extension = user_input.split(".")[1]
except IndexError: 
    raise Exception("Please Input a file with the file extension following after a \".\", e.g.: \"Example.md\"")

if file_extension ==  "md": 
    from Markdown_to_HTML import *
    main(user_input)
    print(rf"Generated file at output\{file_name}.html")

elif file_extension in ("htm", "html"): 
    from HTML_to_Markdown import *
    main(user_input)
    print(rf"Generated file at output\{file_name}.md")

else: 
    raise Exception("Can only accept .md, .htm and .html files")