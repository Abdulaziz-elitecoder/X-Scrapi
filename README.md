# Twitter Scraper

This Python script scrapes tweets mentioning a specific tag (cashtag) from a list of Twitter users within a given time interval.

# Perks

- **Scraping Data for a Specific Tag**: Enter a specific cash tag (e.g., $TSLA) to scrape tweets mentioning that tag.
  
- **Scraping Data for a Given Time Interval**: Specify the number of days, hours, and minutes to define the time interval for scraping.

- **Scrap Data from Multiple Users**: Input a list of Twitter usernames separated by commas to scrape tweets from multiple users simultaneously.

## Installation

1. Clone the repository:
  git clone https://github.com/Abdulaziz-elitecoder/twitterScrapperTask.git

2. Install the required Python packages:
  pip install -r requirements.txt

## Usage

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the script:


4. Follow the prompts to enter the Twitter usernames, cash tag, and time interval.

## Configuration

Before running the script, make sure to set up the following environment variables:

- `TWITTER_USERNAME`: Your Twitter username.
- `TWITTER_EMAIL`: Your Twitter email address.
- `TWITTER_PASSWORD`: Your Twitter password.

**NOTE** You can also change between using prompts as inputs or by using default params. By commenting `xScraper()` and uncommenting `xScraper(twitterUsers, cashTag , timeInterval)`

## Acknowledgments

Special thanks to [d60](https://github.com/d60/twikit) for the [Twikit](https://github.com/d60/twikit) library. Due to Twitter's new policies, scraping has become harder than ever, and Twikit provides a valuable solution for scraping Twitter data.
For more information on the `twikit` package and its utilities, refer to the [Twikit documentation](https://twikit.readthedocs.io/en/latest/twikit.html#twikit.utils.Result).

## Contributing

Please open an issue to report any bugs or suggest improvements.

