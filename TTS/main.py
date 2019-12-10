import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Initiating, please wait a few minutes")