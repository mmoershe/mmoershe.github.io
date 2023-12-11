import os 

import sys

import random 

import PIL  

import abjad

import fitz
CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__)) 
VIOLIN_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "violin")
BASS_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "bass")
VORZEICHEN_VIOLIN_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "vorzeichen_violin")
VORZEICHEN_BASS_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "vorzeichen_bass")


def clean_all_names(path=CURRENT_PATH) -> None: 
    for file in os.listdir(path): 
        # print(file)
        if file.endswith(".preview.png"):
            new_file_name = file.replace(".preview.png", ".png")
            os.replace(os.path.join(path, file), os.path.join(path, new_file_name))


def move_image(from_path: str, to_path: str) -> None:
    os.rename(from_path, to_path)
    print(f"\tMoved {from_path} to {to_path}")


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


def generate_sheetmusic(path=CURRENT_PATH, note: str="c''", tonart: str="c", minor: bool=False, clef: str="treble") -> None:
    global VIOLIN_OUTPUT_PATH, BASS_OUTPUT_PATH, VORZEICHEN_VIOLIN_OUTPUT_PATH, VORZEICHEN_BASS_OUTPUT_PATH
    mode: str = "minor" if minor else "major"
    voice = abjad.Voice(note, name="RH_Voice")
    staff = abjad.Staff([voice], name="RH_Staff")
    score = abjad.Score([staff], name="Score")
    # time_signatures = [(2, 4), (1, 4), (3, 4), (4, 4), (6, 8), (12, 8)]
    # abjad.attach(abjad.TimeSignature(random.choice(time_signatures)), voice[0])
    key_signature = abjad.KeySignature(
        abjad.NamedPitchClass(tonart), abjad.Mode(mode)
    )
    abjad.attach(key_signature, voice[0])
    clef = abjad.Clef(clef)
    abjad.attach(clef, voice[0])
    
    
    obstructed_note: str = note.replace("'", "+")
    filename: str = f"{int(clef=='bass')}{obstructed_note}.png"
    temporary_output_path: str = os.path.join(path, filename)
    
    abjad.persist.as_png(score, temporary_output_path, flags="-dcrop", preview=True, resolution=300)

    clean_all_names(path)
    output_path = ""    
    if clef.name == "treble" and tonart == "c":
        output_path = VIOLIN_OUTPUT_PATH
    if clef.name == "bass" and tonart == "c":
        output_path = BASS_OUTPUT_PATH
    if clef.name == "treble" and tonart != "c":
        output_path = VORZEICHEN_VIOLIN_OUTPUT_PATH
    if clef.name == "bass" and tonart != "c":
        output_path = VORZEICHEN_BASS_OUTPUT_PATH
    output_path = os.path.join(output_path, filename.replace("+", "'"))
    move_image(temporary_output_path, output_path)


if __name__ == "__main__":
    VIOLIN_NOTEN = ["a","b", "c'", "d'", "e'", "f'","g'", "a'","b'", "c''", "d''", "e''", "f''","g''", "a''","b''","c'''"]
    BASS_NOTEN = ["c,", "d,", "e,", "f,","g,", "a,","b,", "c", "d", "e", "f","g", "a","b", "c'", "d'", "e'", "f'","g'"]
    ALLE_TONARTEN = [""]
    # for violin_note in VIOLIN_NOTEN:
    #     generate_sheetmusic(note=violin_note, clef="treble", tonart="c", minor=False)   
    # for bass_note in BASS_NOTEN:
    #     generate_sheetmusic(note=bass_note, clef="bass", tonart="c", minor=False)
    
    generate_sheetmusic(tonart="c", note="cs''")
    
    delete_leftover()