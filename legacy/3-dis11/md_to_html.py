import markdown, os, sys
from markdown.extensions import tables, nl2br
import shutil

MARKDOWN_NAME: str = "dis11_notes.md"

CURRENT_PATH: str = os.path.dirname(__file__)
BASE_PATHS: str = [r"C:\Users\Henri\OneDrive - TH Köln\Slackline\3\DIS11-Informationssysteme-Content-_&_Dokumentenmanagementsysteme", r"C:\Users\User\OneDrive - TH Köln\Slackline\3\DIS11-Informationssysteme-Content-_&_Dokumentenmanagementsysteme"]
assert any([os.path.exists(i) for i in BASE_PATHS]), "I don't have a path saved that exists on this machine."
BASE_PATH: str = [path for path in BASE_PATHS if os.path.exists(path)][0]
MARKDOWN_PATH: str = os.path.join(BASE_PATH, MARKDOWN_NAME)
RAW_FOLDER_PATH: str = os.path.join(BASE_PATH, "raw")
HTML_PATH: str = os.path.join(CURRENT_PATH, "index.html")


def generate_a_tag(headline: str, index: int) -> str:
	return f'<a href="#{index}">{index}. {headline}</a><br />'


def generate_returnButton() -> str: 
	result: list = [f'<button class="returnbutton"><a href="#0">', '&uarr;', '</a></button>']
	return '\n'.join(result)


def copy_raw_folder(src: str, dst: str) -> None: 
	shutil.rmtree(dst)
	shutil.copytree(src, dst)


if __name__ == "__main__":
	with open(MARKDOWN_PATH, "r", encoding="utf-8") as file:
		markdown_content = file.read()
	h1s = [entry[2::].strip() for entry in markdown_content.split("\n") if entry.startswith("# ")]
	for i, h1 in enumerate(h1s):
		markdown_content = markdown_content.replace(f"# {h1}", f"<a name='{i+1}'></a>\n# {h1}")

	html_h1_directory = f"<div class=\"nav\">\n{'\n'.join([generate_a_tag(h1, i+1) for i, h1 in enumerate(h1s)])}\n</div>"


	used_extensions = [tables.TableExtension(), nl2br.Nl2BrExtension()]
	html_content = markdown.markdown(markdown_content, extensions=used_extensions)

	script_tag: str = "<script>var codeElements = document.querySelectorAll('code'); codeElements.forEach(function(codeElement) { var brElement = document.createElement('br'); codeElement.parentNode.insertBefore(brElement, codeElement);});</script>"

	with open(HTML_PATH, 'w', encoding='utf-8') as file:
		file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"UTF-8\">\n<title>DIS13</title>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/styles.css\">\n</head>\n<body>\n<p><a name=\"0\"></a></p>\n{generate_returnButton()}\n{html_h1_directory}\n{html_content}\n{script_tag}\n</body>")

	copy_raw_folder(RAW_FOLDER_PATH, os.path.join(CURRENT_PATH, 'raw')) 

	print("done.")