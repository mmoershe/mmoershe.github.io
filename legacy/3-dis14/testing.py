import markdown, os, sys
from markdown.extensions import tables, nl2br

CURRENT_PATH: str = os.path.dirname(__file__)
all_markdown_files: list = [i for i in os.listdir(CURRENT_PATH) if i.endswith('.md')]
assert len(all_markdown_files) == 1, "There isn't the correct amount (1) of Markdown-Files in this directory."
MARKDOWN_PATH: str = os.path.join(CURRENT_PATH, all_markdown_files[0])
HTML_PATH: str = os.path.join(CURRENT_PATH, "index.html")

if __name__ == "__main__":
	with open(MARKDOWN_PATH, "r", encoding="utf-8") as file:
		markdown_content = file.read()
	h1s = [entry[2::].strip() for entry in markdown_content.split("\n") if entry.startswith("# ")]
	for i, h1 in enumerate(h1s):
		markdown_content = markdown_content.replace(f"# {h1}", f"<a name='{i+1}'></a>\n# {h1}")
	md_h1_directory = "\n".join([f"[{i+1}. {h1}](#{i+1})" for i, h1 in enumerate(h1s)])
	html_h1_directory = f"<div>\n{'\n'.join([])}"
	markdown_content = f"{h1_directory}\n\n{markdown_content}"
	# print(markdown_content)
	used_extensions = [tables.TableExtension(), nl2br.Nl2BrExtension()]

	html_content = markdown.markdown(markdown_content, extensions=used_extensions)

	script_tag: str = "<script>var codeElements = document.querySelectorAll('code'); codeElements.forEach(function(codeElement) { var brElement = document.createElement('br'); codeElement.parentNode.insertBefore(brElement, codeElement);});</script>"

	with open(HTML_PATH, 'w') as file:
		file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>DIS13</title>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/styles.css\">\n</head>\n<body>\n{html_content}\n{script_tag}\n</body>")

	print("done.")

	# beginning
	

	

