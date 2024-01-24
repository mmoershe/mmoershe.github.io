import markdown, os, sys
from markdown.extensions import tables, nl2br

CURRENT_PATH: str = os.path.dirname(__file__)
all_markdown_files: list = [i for i in os.listdir(CURRENT_PATH) if i.endswith('.md')]
assert len(all_markdown_files) == 1, "There isn't the correct amount (1) of Markdown-Files in this directory."
MARKDOWN_PATH: str = os.path.join(CURRENT_PATH, all_markdown_files[0])
HTML_PATH: str = os.path.join(CURRENT_PATH, "index.html")


if __name__ == '__main__': 

    with open(MARKDOWN_PATH, "r") as file:
        markdown_text = file.read()

    used_extensions = [tables.TableExtension(), nl2br.Nl2BrExtension()]

    html_content = markdown.markdown(markdown_text, extensions=used_extensions)

    with open(HTML_PATH, 'w') as file:
        file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>DIS13</title>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/styles.css\">\n</head>\n<body>\n{html_content}\n</body>")

    print("done.")

