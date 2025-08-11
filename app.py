from client import Client

class App:
    def __init__(self, token: str):
        self.token = token
        self.client = Client()

    def run(self):
        """Start the application."""
        self.client.run(self.token)


if __name__ == "__main__":
    app = App("YOUR_BOT_TOKEN")
    app.run()
