
from Internet_speed_bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = '/Users/flight/Downloads/chromedriver'
speed_test_url = 'https://www.speedtest.net/'
twitter_url = 'https://www.twitter.com/'

bot = InternetSpeedTwitterBot()
bot.get_internet_speed(speed_test_url)
bot.tweet_at_provider(twitter_url)
