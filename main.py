import speech_recognition as sr
import os
import pyaudio
import webbrowser
import datetime

import datetime
import pyttsx3


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,1)
        audio = r.listen(source) # this audio will be recognized
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured. Sorry from jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites=[['youtube',"https://www.youtube.com/"],['google','https://www.google.com/'],['wikipedia','https://www.wikipedia.com/'],
               ['mehran','https://muet.edu.pk/']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicpath="C:/Users/21CS041/Downloads/Music/go.mp3"
            os.system(f"start {musicpath}")
        if "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir time is {strftime}")
        if "create new folder" in query:
            say("Please enter the name for the new folder:")
            folder_name = input()
            folder_path = "C:/Users/21CS041/Desktop/Jarvis/" + folder_name
            try:
                os.mkdir(folder_path)
                say(f"Folder '{folder_name}' created successfully.")
            except OSError as error:
                say(f"Error creating folder: {error}")

        if "create new file" in query:
            say("creating a new file")
            with open("C:/Users/21CS041/Desktop/Jarvis/hello.txt", 'w') as file:
                pass
        if "delete file" in query:
            say("deleting file")
            os.remove("C:/Users/21CS041/Desktop/Jarvis/hello.txt")
        if "delete folder" in query:
            say("deleting folder")
            os.rmdir("C:/Users/21CS041/Desktop/Jarvis/newfolder")
        if "open visual studio code".lower() in query.lower():
            vscode_path = '"C:\\Users\\21CS041\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.system(vscode_path)



        # print(tex
        # say(query)


# chatStr = ""
# # https://youtu.be/Z3ZAJoi4x6Q
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Harry: {query}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     say(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]
#
#
# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     # print(response["choices"][0]["text"])
#     text += response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#
#     # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
#         f.write(text)
#
# # def say(text):
# #     os.system(f'say "{text}"')
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         # r.pause_threshold =  0.6
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             return "Some Error Occurred. Sorry from Jarvis"
#
# if __name__ == '__main__':
#     print('Welcome to Jarvis A.I')
#     say("Jarvis A.I")
#     while True:
#         print("Listening...")
#         query = takeCommand()
#         # todo: Add more sites
#         sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
#         for site in sites:
#             if f"Open {site[0]}".lower() in query.lower():
#                 say(f"Opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#         # todo: Add a feature to play a specific song
#         if "open music" in query:
#             musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
#             os.system(f"open {musicPath}")
#
#         elif "the time" in query:
#             musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
#             hour = datetime.datetime.now().strftime("%H")
#             min = datetime.datetime.now().strftime("%M")
#             say(f"Sir time is {hour} bajke {min} minutes")
#
#         elif "open facetime".lower() in query.lower():
#             os.system(f"open /System/Applications/FaceTime.app")
#
#         elif "open pass".lower() in query.lower():
#             os.system(f"open /Applications/Passky.app")
#
#         elif "Using artificial intelligence".lower() in query.lower():
#             ai(prompt=query)
#

        # say(query)
#         elif "Jarvis Quit".lower() in query.lower():
#             exit()
#
#         elif "reset chat".lower() in query.lower():
#             chatStr = ""
#
#         else:
#             print("Chatting...")
#             chat(query)



