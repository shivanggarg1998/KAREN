import speakandrecognize as sar
import functions as F
import webbrowser


if __name__ == "__main__":
    print("____KAREN____")
    F.wishme()
    
    while True:
        query = sar.takecommand().lower()

        if 'wikipedia' in query :       #to search stuff on wikipedia
            F.wiki(query)

        elif 'open youtube' in query:
            sar.speak ('opening youtube...')
            webbrowser.open('http://youtube.com')

        elif 'open gmail' in query:
            sar.speak ('opening gmail...')
            webbrowser.open('http://gmail.com')

        elif 'open github' in query:
            sar.speak ('opening github....')
            webbrowser.open('http://github.com')

        elif "google search" in query:
            query = query.replace("google search","")
            sar.speak ('searching on google.....')
            url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open(url)

        elif "exit" in query:           #to exit the program 
            print("Terminating...")
            sar.speak("see you later")
            exit()