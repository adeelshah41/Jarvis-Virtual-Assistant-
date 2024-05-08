import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
import requests
import datetime
from customtkinter import *
import webbrowser
import threading
import pyttsx3
import time
API_KEY = open('apikey').read()
SEARCH_ENGINE_ID = open('searchengineID').read()

class VirtualAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S")
        self.root.geometry("400x300")
        set_appearance_mode('dark')
        self.label = CTkLabel(root, text="Virtual Assistant")
        self.label.pack()

        self.entry = CTkEntry(root,width=300)
        # self.entry = CTkTextbox(root, height=5,width=10)
        self.entry.pack(padx=10,pady=12)

        self.btn_text_input = CTkButton(root,text="Submit Text", command=self.process_text_input)
        self.btn_text_input.pack(padx=10)

        self.btn_audio_input = CTkButton(root, text="Submit Audio", command=self.process_audio_input)
        self.btn_audio_input.pack(padx=10,pady=12)

        self.output_text =tk.Text(root, height=10, width=50)
        self.output_text.pack()

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
    # def process_text_input(self):
    #     user_input = self.entry.get()
    #     self.handle_input(user_input)

    def process_text_input(self):
        user_input = self.entry.get()
        threading.Thread(target=self.handle_input, args=(user_input,)).start()

    def process_audio_input(self):
        threading.Thread(target=self.listen_and_handle_audio).start()
    #
    def listen_and_handle_audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            self.handle_input(user_input)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def handle_input(self, input_text):
        if "weather" in input_text.lower():
            city = input_text.split()[-1]
            self.get_weather(city)
        elif "time" in input_text.lower():
            self.get_current_time()
        elif 'play music' in input_text.lower():
            self.play_music()
        elif "set reminder" in input_text.lower():
            self.display_message("Enter the reminder time (YYYY-MM-DD HH:MM): ")
            reminder=input_text.split("set reminder ")[-1]
            message="Don't forget to attend the class !!"
            self.set_reminder(reminder,message)
        elif "open" in input_text.lower():
            self.open_website(input_text)
        elif "create folder" in input_text.lower():
            folder_name = input_text.lower().split("create folder ")[-1]
            response = self.create_folder(folder_name)
        elif "create file" in input_text.lower():
            file_name = input_text.lower().split("create file ")[-1]
            response = self.create_file(file_name)
        elif "rename file" in input_text.lower():
            old_name, new_name = input_text.lower().split("rename file ")[-1].split(" to ")
            response = self.rename_file(old_name, new_name)
        elif "rename folder" in input_text.lower():
            old_name, new_name = input_text.lower().split("rename folder ")[-1].split(" to ")
            response = self.rename_folder(old_name, new_name)
        elif "delete file" in input_text.lower():
            file_name = input_text.lower().split("delete file ")[-1]
            response = self.delete_file(file_name)
        elif "delete folder" in input_text.lower():
            folder_name = input_text.lower().split("delete folder ")[-1]
            response = self.delete_folder(folder_name)
        elif "send email" in input_text.lower():
            response = self.send_email()
        elif "google search" in input_text.lower():
            query = input_text.lower().split("google search ")[-1]
            response = self.googlesearch(query)
        elif "translate" in input_text.lower():
            text_to_translate = input_text.lower().split("translate ")[-1]
            response = self.translate_text(text_to_translate)
        elif any(op in input_text.lower() for op in ['+', '-', '*', '/']):
            response = self.calculate(input_text)
        elif "hello" in input_text.lower() and len(input_text)==5:
            self.display_message("Hello! How can I help you?")
        elif "goodbye" in input_text.lower() or "bye" in input_text.lower() or "good bye" in input_text.lower():
            self.display_message("Goodbye!")
            self.root.destroy()
        elif "scrape website" in input_text.lower():
            website_url = input_text.lower().split("scrape website ")[-1]
            response = self.scrape_website(website_url)
        elif "run python file" in input_text.lower():
            file_name = input_text.lower().split("run python file ")[-1]
            response = self.run_python_file(file_name)
        else:
            self.display_message("I'm sorry, I didn't understand that.")
            self.display_message("you said: "+input_text)

    def create_folder(self, folder_name):
        if folder_name == "create folder":
            self.display_message('Try again')
        else:
            try:
                os.mkdir(folder_name)
                self.display_message(f"Folder '{folder_name}' created successfully.")
            except Exception as e:
                self.display_message(f"Failed to create folder '{folder_name}': {str(e)}")

    def rename_folder(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            self.display_message(f"Folder '{old_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            self.display_message(f"Failed to rename folder '{old_name}' to '{new_name}': {str(e)}")

    def delete_folder(self, folder_name):
        if folder_name == "delete folder":
            self.display_message('Try again')
        else:
            try:
                os.rmdir(folder_name)
                self.display_message(f"Folder '{folder_name}' deleted successfully.")
            except Exception as e:
                self.display_message( f"Failed to delete folder '{folder_name}': {str(e)}")

    def create_file(self, file_name):
        if file_name == "create file":
            self.display_message('Try again')
        else:
            try:
                with open(file_name, 'w') as f:
                    pass
                self.display_message(f"Folder '{file_name}' created successfully.")
            except Exception as e:
                self.display_message(f"Failed to create folder '{file_name}': {str(e)}")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            self.display_message(f"File '{old_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            self.display_message( f"Failed to rename file '{old_name}' to '{new_name}': {str(e)}")

    def delete_file(self, file_name):
        if file_name == "delete file":
            self.display_message('Try again')
        else:
            try:
                os.remove(file_name)
                self.display_message(f"File '{file_name}' deleted successfully.")
            except Exception as e:
                self.display_message(f"Failed to delete file '{file_name}': {str(e)}")

    def play_music(self):
            musicpath = "C:/Users/21CS041/Downloads/Music/"
            music_files=os.listdir(musicpath)
            music_files = [file for file in music_files if file.endswith(('.mp3', '.wav'))]
            # Play each music file using the default system player
            for music_file in music_files:
                os.system(f'start {os.path.join(musicpath, music_file)}')

    def get_current_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.display_message(f"The current time is {current_time}.")

    def get_weather(self,city):
        api_key = open('apikey2').read()
        # city = 'Hyderabad'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            self.display_message(f"The current temperature in {city} is {temperature}°C. Weather: {weather_description}.")
        else:
            self.display_message("Failed to fetch weather information.")

    # def run_python_file(self, file_name):
    #     try:
    #         subprocess.run(['python', file_name], capture_output=True, text=True)
    #         return f"Python file '{file_name}' executed successfully."
    #     except Exception as e:
    #         return f"Failed to execute Python file '{file_name}': {str(e)}"
    def open_website(self, input_text):
        # Extract the website URL from user input
        website = input_text.lower().split("open ")[-1]
        # Check if the URL starts with 'http://' or 'https://', if not, prepend it
        if not website.startswith('http://') and not website.startswith('https://'):
            website = 'http://' + website
        try:
            webbrowser.open(website+'.com')
            self.display_message(f"Opened {website}.com successfully.")
        except Exception as e:
            self.display_message(f"Failed to open {website}: {str(e)}")

    # def scrape_website(self, website_url):
    #     try:
    #         response = requests.get(website_url)
    #         if response.status_code == 200:
    #             soup = BeautifulSoup(response.content, 'html.parser')
    #             # Example: Scraping title of the webpage
    #             title = soup.title.string
    #             return f"Title of the webpage: {title}"
    #         else:
    #             return f"Failed to scrape website: {response.status_code}"
    #     except Exception as e:
    #         return f"Failed to scrape website: {str(e)}"

    def set_reminder(self,reminder_time_str, message):
        reminder_time = datetime.datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")
        while True:
            current_time = datetime.datetime.now()
            if current_time >= reminder_time:
                self.display_message(message)
                musicpath = "C:/Users/21CS041/Downloads/Music/bell.wav"
                os.system(f'start {musicpath}')
                break
            else:
                time.sleep(10)  # Check every 10 seconds for the reminde

    def translate_text(self, text_to_translate):
        try:
            translator = Translator()
            translated_text = translator.translate(text_to_translate, dest='en').text
            self.display(f"Translated text: {translated_text}")
        except Exception as e:
            self.display_message(f"Failed to translate text: {str(e)}")

    def googlesearch(self,query):

        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'q': query,
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID
        }
        response = requests.get(url, params=params)
        results = response.json()
        if 'items' in results:
            search_link = results['items'][0]['link']
            webbrowser.open(search_link)

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.display_message(f"Result: {result}")
        except Exception as e:
            self.display_message(f"Failed to perform calculation: {str(e)}")

    def display_message(self, message):
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

if __name__ == "__main__":
    root = CTk()
    app = VirtualAssistant(root)
    root.mainloop()
