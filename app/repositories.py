from app.models import Tweet


class TweetRepository:
    def __init__(self):
        self.tweets = []
        self.next_id = 1

    def add(self, tweet):
        if isinstance(tweet, Tweet):
            tweet.id = self.next_id
            self.next_id += 1
            self.tweets.append(tweet)
            return tweet
        return None

    def get(self, id_to_search):
        for tweet in self.tweets:
            if tweet.id == id_to_search:
                return tweet
        return None

    def delete(self, id_to_delete):
        for tweet in self.tweets:
            if tweet.id == id_to_delete:
                self.tweets.remove(tweet)
                return True
        return False

    def update(self, id_to_update, new_message):
        for i, tweet in enumerate(self.tweets):
            if tweet.id == id_to_update:
                self.tweets[i].text = new_message
                return self.tweets[i]
        return None

    def clear(self):
        self.tweets = []
        self.next_id = 1
