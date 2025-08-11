import customtkinter as ctk
import os
import threading
from app import App

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

TOKEN_FILE = "token.txt"

class BotApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TimeLeaper Bot Runner")
        self.geometry("400x170")

        token = ""
        if os.path.isfile(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                token = f.read().strip()

        self.label = ctk.CTkLabel(self, text="Enter Bot Token:")
        self.label.pack(pady=(20, 5))

        self.token_var = ctk.StringVar(value=token)

        self.token_entry = ctk.CTkEntry(self, textvariable=self.token_var, width=350)
        self.token_entry.pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.pack(pady=(5, 10))

        self.run_button = ctk.CTkButton(self, text="Run Bot", command=self.start_bot_thread)
        self.run_button.pack()

        self.bot_thread = None

    def start_bot_thread(self):
        token = self.token_var.get().strip()
        if not token:
            self.status_label.configure(text="Error: Please enter a bot token.", text_color="red")
            return

        self.token_entry.configure(state="disabled")
        self.run_button.configure(state="disabled")
        self.status_label.configure(text="Starting bot...", text_color="green")
        self.update()

        with open(TOKEN_FILE, "w") as f:
            f.write(token)

        self.bot_thread = threading.Thread(target=self.run_bot, args=(token,), daemon=True)
        self.bot_thread.start()

        self.after(100, self.check_thread)

    def run_bot(self, token):
        try:
            bot = App(token)
            bot.run()
            self.status = "Bot stopped."
            self.status_color = "green"
        except Exception as e:
            self.status = f"Error: {e}"
            self.status_color = "red"

    def check_thread(self):
        if self.bot_thread.is_alive():
            self.after(100, self.check_thread)
        else:
            self.token_entry.configure(state="normal")
            self.run_button.configure(state="normal")
            self.status_label.configure(text=self.status, text_color=self.status_color)


if __name__ == "__main__":
    BotApp().mainloop()
