import os

from dotenv import load_dotenv

from config import get_client
from datetime import datetime
import tweepy

load_dotenv()

client = get_client()


def format_number(number):
    """
    Format a number using Unicode characters to resemble iPhone emojis bar.
    """
    emojis = {
        '0': '0️⃣',
        '1': '1️⃣',
        '2': '2️⃣',
        '3': '3️⃣',
        '4': '4️⃣',
        '5': '5️⃣',
        '6': '6️⃣',
        '7': '7️⃣',
        '8': '8️⃣',
        '9': '9️⃣',
    }

    formatted_number = ''.join(emojis.get(char, char) for char in str(number))
    return formatted_number


if __name__ == "__main__":
    days = str((datetime.today() - datetime(1991, 5, 18)).days)
    # days_since = days[:2] + ',' + days[2:]
    formatted_number = format_number(days)
    tweet = f'Days without recognition \n\n {formatted_number}\n\n #Somaliland'

    # try:
    print(client.get_me())
    client.create_tweet(text=tweet)
    print("Tweet posted successfully:")

    # except Exception as e:
    #     print(e)
