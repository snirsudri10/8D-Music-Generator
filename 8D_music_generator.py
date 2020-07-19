from pydub import AudioSegment
from pydub.playback import play
import math
import sys
import os.path
import matplotlib.pyplot as plt 

def create8D(fileName,speedOfTransition):
    print("creating a 8D song.\nPlease be patient.")
    song = AudioSegment.from_mp3(fileName)
    parts = []
    parts_after_pan = []
    final_song = AudioSegment.empty()
    sinus=0
    duration = len(song)
    for i in range(1,duration+1): #dividing the song to small pisecs
        parts.append(song[(i-1)*100:i*100])
    for i in range(len(parts)): #the for is for all the small parts of the song
        parts_after_pan.append(parts[i].pan(math.sin(speedOfTransition*sinus)))  #panning the small parts with a sin function times the speed of transition
        sinus+=0.001 # adding the sinus function +0.001 so it will rise and fall
        final_song += parts_after_pan[i] #adding it to the final song file
    print("\nDone.\nSaving the file...")
    return final_song #returning the final song

def checkingArgs():
    try:
        print("File name: "+sys.argv[1])
    except IndexError:
        print("Error missing file name")
        return False

    try:
        print("Speed of transition: "+sys.argv[2]+"\n")
    except IndexError:
        print("Error missing the speed of transition")
        return False

    if(not (os.path.exists(sys.argv[1])) or not sys.argv[1][-4:]==".mp3"):
        print("File not Exists or its unsportted (only mp3 files)")
        return False
    
    try:
        int(sys.argv[2])
    except ValueError:
        print("Speed of transition must be a number")
        return False
    
    try:
        int(sys.argv[2])
    except ValueError:
        print("Sinus multiplication must be a number")
        return False
    
    if(int(sys.argv[2])<1 or int(sys.argv[2])>250):
        print("Speed of transition must be between 1 and 250")
        return False
    
    return True

def printHelp():
    print("Hello and welcome the 8D music creator")
    print("This program takes a song and adding it a 8D effect")
    print("This program using the known sinus function to turn the songs into a 8D effects")
    print("Here are the inputs of this program (by ascending order):")
    print("    1. The name of the file (must be a mp3 file)")
    print()
    print("    2. The speed of transition (how fast it will go from R to L)\n    Values range is from 1 to 250")
    print()
    print("    3. the name of the output file")
    print()
    print("    © All Rights Reserved to Snir Sudri")

def main():
    if(sys.argv[1] == "help"):
        printHelp()
    elif(checkingArgs()):
        final_song = create8D(sys.argv[1],int(sys.argv[2]))
        final_song.export("./"+(str(sys.argv[3])+".mp3"),format="mp3",bitrate="320k")
    print("Bye.")
    
if __name__ == '__main__':
    main()
    