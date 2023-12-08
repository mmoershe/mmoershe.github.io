import os 

import PIL  

import abjad

CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__))


note: str = "c'"
voice_1 = abjad.Voice(note, name="Voice_1")
staff_1 = abjad.Staff([voice_1], name="Staff_1")
abjad.show(staff_1)