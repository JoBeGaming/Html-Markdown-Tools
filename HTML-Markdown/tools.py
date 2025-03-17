# tools.py
# Gets user input and tries to convert it to the other format

if not __name__ == "__main__": 
    exit("Please don't try to import tools.py")
    
print("Please input your file, with the file extension")
user_input = input()
try:
    file_name = user_input.split(".")[0]
    file_extension = user_input.split(".")[1]
except IndexError: raise Exception("Please Input a file with the file extension following after a \".\", e.g.: \"Example.md\"")

if file_extension ==  "md": 
    from Markdown_to_HTML import *
elif file_extension in ("htm", "html"): 
    from HTML_to_Markdown import *
else: raise Exception("Can only accept .md, .htm and .html files")

main(user_input)