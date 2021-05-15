import twint

# Configure
c = twint.Config()

# Elon Musk's Twitter and prints tweets that includes "Doge" 
c.Username = "elonmusk"
c.Search = "doge"

# Run
print(twint.run.Search(c))