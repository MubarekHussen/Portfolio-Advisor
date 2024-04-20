import os
from openai import OpenAI
from dotenv import load_dotenv
from scraper import main as scrape_website
from historical_data import main as get_historical_data
import logging
import tkinter as tk
from tkinter import messagebox

logging.basicConfig(level=logging.INFO)
load_dotenv()


def get_openai_client():
    """Get OpenAI client with API key."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Missing OpenAI API key")
    return OpenAI(api_key=api_key)


def ask_gpt(content, price_changes, portfolio_change):
    """Ask GPT for portfolio advice based on the given content and price changes."""
    client = get_openai_client()

    message = f"I read this news article: {content} and focus on this article mainly when you give me the suggestions. Here are the price changes for my stocks in March 2024:\n"
    for symbol, change in price_changes.items():
        message += f"{symbol}: {change:.2f}%\n"
    message += f"\nWeighted average change for the portfolio: {portfolio_change:.2f}%\n"
    message += "My current portfolio is 20% TSLA, 20% NVDA, 20% AAPL, 20% GOOG, and 20% US government bonds. What suggestions do you give me based on this informations?"

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="gpt-3.5-turbo",
        )
    except Exception as e:
        logging.error(f"Failed to get chat completion: {e}")
        return None

    return chat_completion.choices[0].message.content.strip()


def show_message(advice):
    """Display portfolio advice using Tkinter messagebox."""
    root = tk.Tk()
    root.withdraw()
    root.option_add('*Font', 'Helvetica 12')
    root.geometry('1600x600')
    messagebox.showinfo("Portfolio Advice", advice)
    root.destroy()


def main():
    results = get_historical_data()
    content = scrape_website()
    advice = ask_gpt(content, results['price_changes'], results['portfolio_change'])
    if advice:
        logging.info(advice)
        show_message(advice)
    else:
        logging.error("Failed to get advice from GPT")


if __name__ == "__main__":
    main()