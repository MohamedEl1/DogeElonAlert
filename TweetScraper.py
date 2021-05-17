import twint
import SendSMS

import pandas
# Configure

# initial_tweet_count = 0
# new_tweet_count = 0

def ScrapeTweets():
    c = twint.Config()

    # Elon Musk's Twitter and prints tweets that includes "Doge"
    c.Username = "elonmusk"
    c.Search = "doge"
    c.Limit = 2
    c.Count = True
    c.Pandas = True

    # c.Output = "./" + 'ElonDogeTweets.csv'

    # if you want to search recent tweets by a specific word
    # c.Search = "GME"
    # c.Limit = 10

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
            break
            # incremet initial count too
        else:
            print("Number of rows ", len(df.index))
            print("Waiting for new tweet from Elon Musk About Doge")
        # df.to_csv('blm_20.csv', index=False)
        # print(df.head(5))

ScrapeTweets()



