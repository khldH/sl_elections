from dotenv import load_dotenv
from config import get_client
from datetime import datetime
import tweepy

load_dotenv()


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
    client = get_client()

    days = str((datetime.today() - datetime(1991, 5, 18)).days)
    days_since = days[:2] + ',' + days[2:]

    format_days = format_number(days)
    tweet = f'Days without recognition \n\n {format_days}\n\n #Somaliland'
    try:

        client.create_tweet(text=tweet)
        print("Tweet posted successfully:")

    except tweepy.errors.TweepyException as e:
        print(f"Error: {e.response.text}")
