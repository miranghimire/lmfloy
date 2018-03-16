#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
import os
import sys

playcommand="mpv '{}.mp3' *.mp3"
def display_menu():
    print("=============================================")
    print("         p/SPACE to pause                    ")
    print("         L to loop                           ")
    print("         < and > for next and previous       ")
    print("         / and * decrease/increase volume    ")
    print("         m to mute sound                     ")
    print("         q to quit                           ")
    print("=============================================")
    print("\n")

def main():
    if len(sys.argv) == 1:
        display_menu()
        os.system("mpv *.mp3")
        exit(1)
    elif len(sys.argv) != 2:
        print("Usage: youtube.py 'search string' ")
        exit(1)
    filename = sys.argv[1]
    query_string = urllib.parse.urlencode({"search_query" : filename})
    if os.path.exists(filename+".mp3"):
        display_menu()
        os.system(playcommand.format(filename))
    else:
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("=============================================")
        print("     Downloading " + filename +"             ")
        print("=============================================")
        url = "http://www.youtube.com/watch?v=" + search_results[0]
        download_command = "youtube-dl --extract-audio --audio-format mp3 -o '{}' {} > /dev/null"
        os.system(download_command.format(filename+".%(ext)s",url))
        print("             Download succeeded               ")
        display_menu()
        os.system(playcommand.format(filename))
if __name__=="__main__":
    main()
