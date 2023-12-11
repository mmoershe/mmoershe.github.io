import os 

import random 

import PIL  

import abjad

import fitz
CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__))


def convert_pdf_to_png(path=CURRENT_PATH):
    pdf_files: list = [i for i in os.listdir(path) if i.endswith(".pdf")]
    if not os.path.exists(path):
        print(f"{path} doesn't exist.")
        return
    if len(pdf_files) == 0:
        print("There are no PDF-files in the directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF-file(s).")
    for pdf_file in pdf_files:
        pdf_file_path: str = os.path.join(path, pdf_file)
        png_file: str = f"{pdf_file[:-4:]}.png"
        png_file_path: str = os.path.join(path, png_file)
        doc = fitz.open(pdf_file_path)
        first_page = doc[0]
        image = first_page.get_pixmap()
        pil_image = PIL.Image.frombytes("RGB", [image.width, image.height], image.samples)
        pil_image.save(png_file_path)
        os.remove(pdf_file_path)
        print(f"\tConverted {pdf_file} to {png_file}")
        
        
        
def convert_pdf_to_svg(path=CURRENT_PATH):
    pdf_files: list = [i for i in os.listdir(path) if i.endswith(".pdf")]
    if not os.path.exists(path):
        print(f"{path} doesn't exist.")
        return
    if len(pdf_files) == 0:
        print("There are no PDF-files in the directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF-file(s).")
    for pdf_file in pdf_files:
        pdf_file_path: str = os.path.join(path, pdf_file)
        doc = fitz.open(pdf_file_path)
        first_page = doc[0]
        svg_content = first_page.get_svg_image()
        
        with open(os.path.join(path, f"{pdf_file[:-4:]}.svg"), "w", encoding="utf-8") as svg_file:
            svg_file.write(svg_content)
    
    

def crop_svg():
    input_svg_path = os.path.join(CURRENT_PATH, [i for i in os.listdir(CURRENT_PATH) if i.endswith(".svg")][0])
    output_svg_path = os.path.join(CURRENT_PATH, "test.svg")
    # Read the SVG file
    pass



def move_images():
    pass


def delete_leftover(path=CURRENT_PATH):
    # deletes all .ly and .log files that are somehow created with abjad
    all_leftovers: list = [i for i in os.listdir(path) if i.endswith(".ly") or i.endswith(".log")]
    if not all_leftovers:
        print("No leftovers were found.")
        return
    print(f"Found {len(all_leftovers)} leftover-file(s).")
    
    for leftover in all_leftovers: 
        os.remove(os.path.join(path, leftover))
        print(f"\t{leftover} has been deleted.")


def main(note: str="c''", tonart: str="c", minor: bool=False, clef: str="treble"):
    mode: str = "minor" if minor else "major"
    voice = abjad.Voice(note, name="RH_Voice")
    staff = abjad.Staff([voice], name="RH_Staff")
    score = abjad.Score([staff], name="Score")

    time_signatures = [(2, 4), (1, 4), (3, 4), (4, 4), (6, 8), (12, 8)]
    abjad.attach(abjad.TimeSignature(random.choice(time_signatures)), voice[0])

    key_signature = abjad.KeySignature(
        abjad.NamedPitchClass(note), abjad.Mode(mode)
    )
    abjad.attach(key_signature, voice[0])
    
    clef = abjad.Clef(clef)
    abjad.attach(clef, voice[0])
    
    filename: str = f"{int(clef == 'bass')}{'c'}.png"
    print(filename)
    
    abjad.persist.as_png(score, os.path.join(CURRENT_PATH, filename), flags="-dcrop", preview=True, resolution=300)
    # abjad.show(score)



if __name__ == "__main__":
    print(f"{abjad.__version__ = }")
    print(f"{CURRENT_PATH = }")
    main()
    # delete_leftover()