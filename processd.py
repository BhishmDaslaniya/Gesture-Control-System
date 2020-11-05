# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:16:20 2020

@author: Bhishm
"""

import psutil


VLC = "vlc.exe"
CHROME = "chrome.exe"
MUSIC= "Music.UI.exe"
GAME = "Highway Racer.exe"
PPT = "POWERPNT.EXE"



def current_process():
    count=0
    for proc in psutil.process_iter():

        if proc.name()==VLC:
            return "vlc"

        if proc.name()==MUSIC:
            return "music"
            
        if proc.name()==CHROME:
            return "chrome"
        
        if proc.name()==GAME:
            return "game"
        
        if proc.name()== PPT:
            return "PPT" 
                

current_process()            
            
            
    
            
   
    
        
       
