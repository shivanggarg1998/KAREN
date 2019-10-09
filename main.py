import speakandrecognize as sar
import functions as F


if __name__ == "__main__":
    print("____KAREN____")
    F.wishme()
    
    while True:
        query = sar.takecommand().lower()

        if 'wikipedia' in query :
            F.wiki(query)

        elif "exit" in query:
            print("Terminating...")
            sar.speak("see you later")
            exit()