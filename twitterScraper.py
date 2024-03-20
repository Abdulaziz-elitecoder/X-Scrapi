from dotenv import load_dotenv
from twikit import Client
from twikit.utils import build_query
from datetime import datetime, timezone, timedelta
import os
import time
import json

# loading env variables
load_dotenv()

# getting X credentials from .env for scraping due to new X policies.
USERNAME = os.environ.get('TWITTER_USERNAME')
EMAIL = os.environ.get('TWITTER_EMAIL')
PASSWORD = os.environ.get('TWITTER_PASSWORD')

# Initialize client
client = Client('en-US')
# Login to the service with provided user credentials
client._user_agent = client._user_agent.strip()
client.login(
    auth_info_1=USERNAME,
    auth_info_2=EMAIL,
    password=PASSWORD
)

def get_twitter_users():
    users_input = input("Enter Twitter usernames separated by commas (e.g., user1,user2): ")
    return users_input.split(',')

def get_cash_tag():
    return input("Enter the cashTag (e.g., $TSLA): ")

def get_time_interval():
    days = input("Enter the number of days: ")
    hours = input("Enter the number of hours: ")
    minutes = input("Enter the number of minutes: ")
    return [int(days), int(hours), int(minutes)]

def scrapeTweets(twitterUsersList, Tag, timeInterval):
    """
    Scrape tweets mentioning a specific tag from a list of Twitter users within a given time interval.

    Args:
        twitterUsersList (list): List of Twitter usernames to scrape tweets from.
        Tag (str): The tag to search for in tweets (e.g., "$TSLA").
        timeInterval (list): List containing [days, hours, minutes] specifying the time interval to search within.

    Returns:
        None
    """
    # empty array
    tweets_data = []
    # Calculate the datetime to start searching from
    timeSubtract = timedelta(days=timeInterval[0], hours=timeInterval[1], minutes=timeInterval[2])
    targetedDateTime = datetime.now(timezone.utc) - timeSubtract
    formattedDate = targetedDateTime.strftime("%Y-%m-%d")
    
    # Counter for the number of tweets mentioning the tag
    counterOfQualifiedTweets = 0
    

    # Loop through each Twitter user in the list
    for twitterUser in twitterUsersList:
        options = {
            # Search options for the Twitter user
            "from_user": twitterUser,
            "since": formattedDate,
        }
        
        # Build search query from both (text, options) which in this case text = Tag 
        query = build_query(Tag, options)
        
        # Search latest tweets using the query
        tweets = client.search_tweet(query, 'latest')
        
        # Loop through each tweet
        for tweet in tweets:
            # Convert tweet datetime to a compatible datetime object
            tweetDateTime = datetime.strptime(
                tweet.created_at, "%a %b %d %H:%M:%S %z %Y")
            
            # Check if the tweet is within the targeted datetime range
            if targetedDateTime <= tweetDateTime:
                counterOfQualifiedTweets += 1
                print(f"tweetID: {tweet.id} username: {tweet.user.screen_name} createdAt: {tweet.created_at}")
                # Append tweet data to tweets_data list
                tweets_data.append({
                    "tweetID": tweet.id,
                    "username": tweet.user.screen_name,
                    "createdAt": tweet.created_at,
                    "viewCount": tweet.view_count
                })

    # Print summary of search results
    print(f"""--------------------------------------------------------------
{Tag} was mentioned {str(counterOfQualifiedTweets)} times in the last {str(timeInterval[0])} days, {str(timeInterval[1])} hours, and {str(timeInterval[2])} minutes.
--------------------------------------------------------------""")
        
    # save the tweets list as JSON file
    tweets_json = json.dumps(tweets_data, indent=4)
    with open("./tweets.json", 'w') as f:
        f.write(tweets_json)
        
    # Calculate the time interval in seconds
    timeIntervalInSeconds = (
        timeInterval[0] * 24 * 60 * 60) + (timeInterval[1] * 60 * 60) + (timeInterval[2] * 60)
    # Sleep for the time interval
    time.sleep(timeIntervalInSeconds)
    
def xScraper(twitterUsersList = None, Tag= None, timeInterval=None):
    # get twitter users list
    if twitterUsersList is None:
        twitterUsersList = get_twitter_users()
    # get targeted tag
    if Tag is None:
        Tag = get_cash_tag()
    # get timeInterval
    if timeInterval is None:
        timeInterval = get_time_interval()

    while True:
        scrapeTweets(twitterUsersList, Tag, timeInterval)


if __name__ == '__main__':
    # Default values for the params to search with
    twitterUsers = ["Mr_Derivatives", "warrior_0719","ChartingProdigy", "allstarcharts", "yuriymatso", "TriggerTrades", "AdamMancini4", "CordovaTrades", "Barchart", "RoyLMattox"]
    cashTag = "$CMG"
    timeInterval = [0, 12, 0]

    
    # using the function with default values
    xScraper(twitterUsers, cashTag , timeInterval)
    
    # without default params
    # xScraper()

