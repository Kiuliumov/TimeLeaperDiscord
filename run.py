import argparse
from dotenv import load_dotenv
import os
from app import App

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run the bot client.")
    parser.add_argument(
        "-t", "--token", help="Your bot token (overrides .env)"
    )
    args = parser.parse_args()

    token = args.token or os.getenv("BOT_TOKEN")

    if not token:
        print("Error: Bot token not provided. Use --token or set BOT_TOKEN in .env")
        exit(1)

    app = App(token)
    app.run()

if __name__ == "__main__":
    main()
