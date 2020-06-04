import subprocess
import shutil, os

def create_CombinedMP3(m3pCombiner_Path, passive_Immersion_Path,deck_Name):
    subprocess.call("mp3cat -d . -o combined.mp3", shell=True, cwd=m3pCombiner_Path)
    for file in os.listdir(m3pCombiner_Path):
        filename = os.fsdecode(file)
        if (filename.endswith(".mp3") and filename != "combined.mp3"):
            os.remove(m3pCombiner_Path+"\\"+filename)
            continue
    os.rename(m3pCombiner_Path+"\\combined.mp3", passive_Immersion_Path +"\\"+deck_Name+".mp3")

def move_Files_To_Combined_Path(audio_Path, m3pCombiner_Path):
    for file in os.listdir(audio_Path):
        filename = os.fsdecode(file)
        if filename.endswith(".mp3"):
            shutil.copy(audio_Path + "\\"+ filename, m3pCombiner_Path)
            continue

