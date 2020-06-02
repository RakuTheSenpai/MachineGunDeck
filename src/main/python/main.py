import sys
sys.coinit_flags = 2
import os
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, 
        QProgressBar, QPushButton, QVBoxLayout, QWidget, QFileDialog, QSpinBox)
# from createPassiveImmersion import *
from prepareFiles import *
from createDeck import *
from ankiInfo import *

class MiaAuto(QDialog):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setFixedWidth(400)

        self.create_Subs2srs_Group()
        self.create_mp3Combiner_Group()

        self.ok_Button = QPushButton("Let's Go!")
        self.ok_Button.setEnabled(False)
        self.ok_Button.clicked.connect(self.execute)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.subs2srs_Group, 1, 0)
        mainLayout.addWidget(self.mp3Combiner_Group,2,0)
        mainLayout.addWidget(self.ok_Button, 3,0)
        self.setLayout(mainLayout)

    def create_Subs2srs_Group(self):
        subs2srs_Path_Lbl = QLabel("Path to Subs2srs:")
        self.subs2srs_Path_Btn = QPushButton("Subs2srs")
        self.subs2srs_Path_Txt = QLineEdit(self)
        self.subs2srs_Path_Txt.setEnabled(False)
        self.subs2srs_Path_Btn.clicked.connect(lambda :self.get_File(self.subs2srs_Path_Txt,"Subs2srs Executable (subs2srs.exe)",False))
        self.subs2srs_Path_Txt.textChanged.connect(self.is_Complete)

        subs2srs_Path_Box = QHBoxLayout()
        subs2srs_Path_Box.addWidget(self.subs2srs_Path_Btn)
        subs2srs_Path_Box.addWidget(self.subs2srs_Path_Txt)

        subtitle_Path_Lbl = QLabel("Subtitle Path:")
        self.subtitle_Path_Btn = QPushButton("Subtitle")
        self.subtitle_Path_Txt = QLineEdit(self)
        self.subtitle_Path_Txt.setEnabled(False)
        self.subtitle_Path_Btn.clicked.connect(lambda :self.get_File(self.subtitle_Path_Txt,"All Subtitle Files (*.ass *.ssa *.lrc *.srt *.trs *.idx)",False))
        self.subtitle_Path_Txt.textChanged.connect(self.is_Complete)

        subtitle_Path_Box = QHBoxLayout()
        subtitle_Path_Box.addWidget(self.subtitle_Path_Btn)
        subtitle_Path_Box.addWidget(self.subtitle_Path_Txt)

        video_Path_Lbl = QLabel("Video Path:")
        self.video_Path_Btn = QPushButton("Video")
        self.video_Path_Txt = QLineEdit(self)
        self.video_Path_Txt.setEnabled(False)
        self.video_Path_Btn.clicked.connect(lambda :self.get_File(self.video_Path_Txt,"All Common Video Files (*.avi *.flv *.mkv *.mp4 *.ogm *.vob)",False))
        self.video_Path_Txt.textChanged.connect(self.is_Complete)

        video_Path_Box = QHBoxLayout()
        video_Path_Box.addWidget(self.video_Path_Btn)
        video_Path_Box.addWidget(self.video_Path_Txt)

        output_Path_Lbl = QLabel("Where the files will be placed:")
        self.output_Path_Btn = QPushButton("Output")
        self.output_Path_Txt = QLineEdit(self)
        self.output_Path_Txt.setEnabled(False)
        self.output_Path_Btn.clicked.connect(lambda :self.get_File(self.output_Path_Txt,"",True))
        self.output_Path_Txt.textChanged.connect(self.is_Complete)

        output_Path_Box = QHBoxLayout()
        output_Path_Box.addWidget(self.output_Path_Btn)
        output_Path_Box.addWidget(self.output_Path_Txt)

        self.subs_Time_Shift = QCheckBox("Subtitle time shift (ms)")
        self.subs_Time_Shift_Txt = QSpinBox(self)
        self.subs_Time_Shift_Txt.setValue(0)
        self.subs_Time_Shift_Txt.setMaximum(99999)
        self.subs_Time_Shift_Txt.setMinimum(-99999)
        self.subs_Time_Shift_Txt.setEnabled(False)
        subs_Time_Shift_Box = QHBoxLayout()
        subs_Time_Shift_Box.addWidget(self.subs_Time_Shift)
        subs_Time_Shift_Box.addWidget(self.subs_Time_Shift_Txt)
        self.subs_Time_Shift.toggled.connect(self.subs_Time_Shift_Txt.setEnabled)

        deck_Name_Lbl = QLabel("Deck Name:")
        self.deck_Name = QLineEdit(self)
        self.deck_Name.textChanged.connect(self.is_Complete)

        self.subs2srs_Group = QGroupBox("Subs2srs")

        layout = QVBoxLayout()
        layout.addWidget(subs2srs_Path_Lbl)
        layout.addLayout(subs2srs_Path_Box)
        layout.addWidget(subtitle_Path_Lbl)
        layout.addLayout(subtitle_Path_Box)
        layout.addWidget(video_Path_Lbl)
        layout.addLayout(video_Path_Box)
        layout.addWidget(output_Path_Lbl)
        layout.addLayout(output_Path_Box)
        layout.addLayout(subs_Time_Shift_Box)
        layout.addWidget(deck_Name_Lbl)
        layout.addWidget(self.deck_Name)
        self.subs2srs_Group.setLayout(layout)   
    
    def create_mp3Combiner_Group(self):
        mp3Combiner_Path_Lbl = QLabel("Path to mp3Combiner:")
        self.mp3Combiner_Path_Btn = QPushButton("mp3Combiner")
        self.mp3Combiner_Path_Txt = QLineEdit(self)
        self.mp3Combiner_Path_Txt.setEnabled(False)
        self.mp3Combiner_Path_Btn.clicked.connect(lambda :self.get_File(self.mp3Combiner_Path_Txt,"Mp3cat Executable (mp3cat.exe)", False))
        self.mp3Combiner_Path_Txt.textChanged.connect(self.is_Complete)

        mp3Combiner_Path_Box = QHBoxLayout()
        mp3Combiner_Path_Box.addWidget(self.mp3Combiner_Path_Btn)
        mp3Combiner_Path_Box.addWidget(self.mp3Combiner_Path_Txt)
        
        passive_Path_Lbl = QLabel("Where the files will be placed:")
        self.passive_Path_Btn = QPushButton("Output")
        self.passive_Path_Txt = QLineEdit(self)
        self.passive_Path_Txt.setEnabled(False)
        self.passive_Path_Btn.clicked.connect(lambda :self.get_File(self.passive_Path_Txt,"", True))
        self.passive_Path_Txt.textChanged.connect(self.is_Complete)

        passive_Path_Box = QHBoxLayout()
        passive_Path_Box.addWidget(self.passive_Path_Btn)
        passive_Path_Box.addWidget(self.passive_Path_Txt)
        
        self.mp3Combiner_Group = QGroupBox("mp3Combiner")

        layout = QVBoxLayout()
        layout.addWidget(mp3Combiner_Path_Lbl)
        layout.addLayout(mp3Combiner_Path_Box)
        layout.addWidget(passive_Path_Lbl)
        layout.addLayout(passive_Path_Box)
        self.mp3Combiner_Group.setLayout(layout)       

    def get_File(self, fieldTxt, restriction, directory):
        if(directory):
            fileName = QFileDialog.getExistingDirectory(self,"Select Directory  ","",QFileDialog.ShowDirsOnly)
        else:
            fileName, _ = QFileDialog.getOpenFileName(self,"Select File", "",restriction)
        if fileName:
            fieldTxt.setText(fileName)

    def is_Complete(self):
        textBoxes = [self.subs2srs_Path_Txt.text(), self.subtitle_Path_Txt.text(), self.video_Path_Txt.text(), 
        self.deck_Name.text(),self.mp3Combiner_Path_Txt.text(),self.output_Path_Txt.text(),self.passive_Path_Txt.text()]
        self.ok_Button.setEnabled(all(textBoxes))
    
    def execute(self):
        video_Path = os.path.dirname(self.video_Path_Txt.text())
        video_Path_Ext = self.video_Path_Txt.text().rsplit('.', 1)[1]
        subtitle_Path = os.path.dirname(self.subtitle_Path_Txt.text())
        subtitle_Path_Ext =  self.subtitle_Path_Txt.text().rsplit('.', 1)[1]
        subs2srs_Path = self.subs2srs_Path_Txt.text()
        directory_Path = self.output_Path_Txt.text()
        deck_Name = self.deck_Name.text()
        subs_Time_Shift = str(self.subs_Time_Shift_Txt.value() if self.subs_Time_Shift.isChecked() else 0)

        sortFilesNumerically(video_Path, video_Path_Ext)
        sortFilesNumerically(subtitle_Path, subtitle_Path_Ext)

        create_Subs2srs_Deck(subs2srs_Path, subtitle_Path, video_Path, directory_Path,deck_Name,subs_Time_Shift)

if __name__ == '__main__':
    appctxt = ApplicationContext()      
    Mia = MiaAuto()
    Mia.show()
    exit_code = appctxt.app.exec_()      
    sys.exit(exit_code)
