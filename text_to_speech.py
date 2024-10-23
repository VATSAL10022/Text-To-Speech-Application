import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os
import playsound

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Application")

        # Text input area
        self.text_input = tk.Text(self.root, height=10, width=50)
        self.text_input.pack(pady=10)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack(pady=5)

        # Clear button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_text)
        self.clear_button.pack(pady=5)

    def convert_to_speech(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            playsound.playsound("output.mp3")
        else:
            messagebox.showwarning("Input Error", "Please enter some text.")

    def clear_text(self):
        self.text_input.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
