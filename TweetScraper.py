import twint
import SendSMS
import nest_asyncio
import time

def ScrapeTweets():

    starttime = time.time()
    nest_asyncio.apply()
    c = twint.Config()

    # Elon Musk's Twitter and prints tweets that includes "Doge"
    c.Username = "Mohamed79113197"
    c.Search = "doge"
    c.Limit = 2
    c.Count = True
    c.Pandas = True


    # Run the scraping of Elon's tweet
    twint.run.Search(c)

    # Save the tweets in a dataframe and count the number of tweets
    df1 = twint.storage.panda.Tweets_df
    initial_tweet_count = len(df1.index)

    # This will keep looping to check / listen for new tweets from Elon Musk
    while True:
        twint.run.Search(c)
        # Save the tweets in a dataframe and count the number of tweets
        df = twint.storage.panda.Tweets_df
        new_tweet_count = len(df.index)

        if new_tweet_count > initial_tweet_count:
            # Calling SMS function to send text message to phone number
            SendSMS.sendsms()
            print("Elon musk Just tweeted about DogeCoin")

            # Increment initial tweet count
            initial_tweet_count +=1

        else:
            print("Waiting for new tweet from Elon Musk About Doge coin")
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))


ScrapeTweets()



