import tweepy


def user_data(username, key):
    """(str, str) -> str
    This function takes username as string and key as a string and returns
    specific data about user as a string."""
    try:
        status = api.user_timeline(screen_name=username, count=1)[0]
        if len(status) != 0:
            json_parse = status
            try:
                return username + ' (' + key + '):' + str(json_parse[key])
            except KeyError:
                return "Incorrect key"
    except tweepy.error.TweepError:
            return "Username not found"


if __name__ == "__main__":
    access_token = "963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC"
    access_token_secret = "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R"
    consumer_key = "0PlKlKMbNYWL9UeVuC6DPxX4B"
    consumer_secret = "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    username = input("Enter username: ")
    key = input("""Enter key(created_at, id, id_str, text, truncated, entities,
    source, in_reply_to_status_id, in_reply_to_status_id_str,
    in_reply_to_user_id, in_reply_to_user_id_str, in_reply_to_screen_name,
    user, geo, oordinates, place, contributors, is_quote_status, retweet_count,
    favorite_count, favorited, retweeted, possibly_sensitive, lang): """)
    print(user_data(username, key))
