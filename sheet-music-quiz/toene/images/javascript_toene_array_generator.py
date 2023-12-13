import os 
import sys 

CURRENT_PATH = os.path.dirname(__file__)

VIOLIN_FOLDER, BASS_FOLDER, VORZEICHEN_VIOLIN_FOLDER, VORZEICHEN_BASS_FOLDER = "violin", "bass", "vorzeichen_violin", "vorzeichen_bass"

# sys.exit()
with open(os.path.join(CURRENT_PATH, "javascript_toene_arrays.js"), "w", encoding = "utf-8") as txt_file:
    violin_list_content = [f"{VIOLIN_FOLDER}/{i}" for i in os.listdir(os.path.join(CURRENT_PATH, VIOLIN_FOLDER))]
    txt_file.write(f"var imagesViolin = {violin_list_content}\n")
    
    bass_list_content = [f"{BASS_FOLDER}/{i}" for i in os.listdir(os.path.join(CURRENT_PATH, BASS_FOLDER))]
    txt_file.write(f"var imagesBass = {bass_list_content}\n")
    
    vorzeichen_violin_list_content = []
    for tonart_folder in os.listdir(os.path.join(CURRENT_PATH, VORZEICHEN_VIOLIN_FOLDER)):
        for image in os.listdir(os.path.join(CURRENT_PATH, VORZEICHEN_VIOLIN_FOLDER,tonart_folder)):
            vorzeichen_violin_list_content.append(f"{VORZEICHEN_VIOLIN_FOLDER}/{tonart_folder}/{image}")
    txt_file.write(f"var imagesViolinVorzeichen = {vorzeichen_violin_list_content}\n")
    
    vorzeichen_bass_list_content = []
    for tonart_folder in os.listdir(os.path.join(CURRENT_PATH, VORZEICHEN_BASS_FOLDER)):
        for image in os.listdir(os.path.join(CURRENT_PATH, VORZEICHEN_BASS_FOLDER,tonart_folder)):
            vorzeichen_bass_list_content.append(f"{VORZEICHEN_BASS_FOLDER}/{tonart_folder}/{image}")
    txt_file.write(f"var imagesBassVorzeichen = {vorzeichen_bass_list_content}\n")

print(len(vorzeichen_bass_list_content))