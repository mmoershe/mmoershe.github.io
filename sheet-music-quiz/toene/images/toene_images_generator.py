import os 

import sys

import random 

import PIL  

import abjad

import json 

from tqdm import tqdm 

CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__)) 
VIOLIN_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "violin")
BASS_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "bass")
VORZEICHEN_VIOLIN_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "vorzeichen_violin")
VORZEICHEN_BASS_OUTPUT_PATH: str = os.path.join(CURRENT_PATH, "vorzeichen_bass")


def create_directories(path=CURRENT_PATH) -> None: 
    global VIOLIN_OUTPUT_PATH, BASS_OUTPUT_PATH, VORZEICHEN_VIOLIN_OUTPUT_PATH, VORZEICHEN_BASS_OUTPUT_PATH
    for directory in [VIOLIN_OUTPUT_PATH, BASS_OUTPUT_PATH, VORZEICHEN_VIOLIN_OUTPUT_PATH, VORZEICHEN_BASS_OUTPUT_PATH]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            tqdm.write(f"Created {directory}")


def clean_all_names(path=CURRENT_PATH) -> None: 
    for file in os.listdir(path): 
        # tqdm.write(file)
        if file.endswith(".preview.png"):
            new_file_name = file.replace(".preview.png", ".png")
            os.replace(os.path.join(path, file), os.path.join(path, new_file_name))


def move_image(from_path: str, to_path: str, filename: str) -> None:
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    os.rename(from_path, os.path.join(to_path, filename))
    tqdm.write(f"Moved {filename} to {to_path}")


def delete_leftover(path=CURRENT_PATH):
    # deletes all .ly and .log files that are somehow created with abjad
    all_leftovers: list = [i for i in os.listdir(path) if i.endswith(".ly") or i.endswith(".log")]
    if not all_leftovers:
        tqdm.write("No leftovers were found.")
        return
    tqdm.write(f"Found {len(all_leftovers)} leftover-file(s).")
    
    for leftover in all_leftovers: 
        os.remove(os.path.join(path, leftover))
        tqdm.write(f"\t{leftover} has been deleted.")


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
    if clef.name == "treble" and tonart == "c" and note in toene_data["toene"][clef.name]["clean"]:
        output_path = VIOLIN_OUTPUT_PATH
    elif clef.name == "bass" and tonart == "c" and note in toene_data["toene"][clef.name]["clean"]:
        output_path = BASS_OUTPUT_PATH
    elif clef.name == "treble":
        output_path = VORZEICHEN_VIOLIN_OUTPUT_PATH
        output_path: str = os.path.join(output_path, f"tonart_{tonart}")
    elif clef.name == "bass":
        output_path = VORZEICHEN_BASS_OUTPUT_PATH
        output_path: str = os.path.join(output_path, f"tonart_{tonart}")
        
    filename = filename.replace("+", "'")
    move_image(temporary_output_path, output_path, filename)


if __name__ == "__main__":   
    with open(os.path.join(CURRENT_PATH, "toene_data.json"), "r") as f:
        toene_data = json.load(f)
    create_directories()
    
    for tonart in tqdm(toene_data["tonarten"], leave=False):
        tqdm.write("")
        for clef in tqdm(toene_data["toene"], leave=False):
            tqdm.write("")
            for note in tqdm(toene_data["toene"][clef]["all"], leave=False):
                generate_sheetmusic(note=note, tonart=tonart, clef=clef, minor=False)
            delete_leftover()
    
    delete_leftover()

    # VIOLIN_NOTEN = ["a","b", "c'", "d'", "e'", "f'","g'", "a'","b'", "c''", "d''", "e''", "f''","g''", "a''","b''","c'''"]
    # BASS_NOTEN = ["c,", "d,", "e,", "f,","g,", "a,","b,", "c", "d", "e", "f","g", "a","b", "c'", "d'", "e'", "f'","g'"]
    # ALLE_TONARTEN = ["g", "d", "a", "e", "b", "fs", "gf", "df", "af", "ef", "bf", "f"]
    # for violin_note in VIOLIN_NOTEN:
    #     generate_sheetmusic(note=violin_note, clef="treble", tonart="c", minor=False)   
    # for bass_note in BASS_NOTEN:
    #     generate_sheetmusic(note=bass_note, clef="bass", tonart="c", minor=False)
    # for i in ALLE_TONARTEN:
    #     generate_sheetmusic(tonart=i, note="fs'")