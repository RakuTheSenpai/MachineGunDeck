from pywinauto.application import Application
import shutil, os
import time

def create_Subs2srs_Deck(subs2srs_Path, subtitle_Path, video_Path, directory_Path,deck_Name,subs_Time_Shift):
    subs2srs_App = Application().start(subs2srs_Path)
    subs2srs = subs2srs_App.subs2srs
    subs2srs.set_focus()
    subs2srs['&Subs1...Edit'].set_text(subtitle_Path+"\\*.srt")
    subs2srs['&Video...Edit'].set_text(video_Path+"\\*.mp4")    
    subs2srs['&Output...Edit'].set_text(directory_Path)
    subs2srs['Name of deck:Edit'].set_text(deck_Name)
    subs2srs['Time Shift:Button'].click_input()
    subs2srs['Subs1:Edit'].set_text(subs_Time_Shift)
    subs2srs_App.subs2srs.Button0.click()  
    while(True):
        if(subs2srs_App.subs2srs.is_active()==True):
            subs2srs_App.kill_()
            break

