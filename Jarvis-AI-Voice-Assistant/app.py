import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
import jarvis
import sys
import threading
import os

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis Voice Assistant")
        self.root.geometry("950x600")

        self.header_label = ttk.Label(root, text="Jarvis Voice Assistant", font=("Helvetica", 20, "bold"))
        self.header_label.pack(pady=10)

        # Animated Mic Image (GIF)
        self.gif_label = ttk.Label(root)
        self.gif_label.pack()
        self.load_animation("mic.gif")

        # Available commands display
        commands_frame = ttk.LabelFrame(root, text="Available Commands", padding=10)
        commands_frame.pack(pady=10)

        self.commands_text = tk.Text(commands_frame, height=10, width=100)
        self.commands_text.insert(tk.END, """
        - wikipedia <topic>
        - open youtube / open google / open <site>.com
        - play music
        - what is the time / date
        - open chrome / file explorer / open camera
        - hi / hello / how are you / what is your name
        - thanks / who made you
        - quit / exit / bye
        """)
        self.commands_text.config(state=tk.DISABLED)
        self.commands_text.pack()

        # Output Text Area
        self.output_text = tk.Text(root, height=12, width=100)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.output_text.pack(pady=5)

        # Redirect stdout
        sys.stdout = self

        # Speak Button
        self.speak_button = ttk.Button(root, text="🎤 Speak", command=self.execute_jarvis_main)
        self.speak_button.pack(pady=10)

        self.footer_label = ttk.Label(root, text="Developed by Franklin", font=("Helvetica", 10, "bold"))
        self.footer_label.pack()

    def load_animation(self, path):
        self.gif = Image.open(path)
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        self.animate()

    def animate(self):
        self.gif_label.configure(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(100, self.animate)

    def execute_jarvis_main(self):
        self.output_text.delete('1.0', tk.END)
        threading.Thread(target=jarvis.main).start()

    def write(self, text):
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.update_idletasks()


def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()