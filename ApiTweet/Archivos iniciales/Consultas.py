import tweepy
import json

consumer_key ="Fh6LmUXiwKFbiBVWwaDnrF5ol"    
consumer_secret ="Hr7stctYdMu5VrnCy345J6cERIatB6tGHFXAgqefjL63BR7iSE"
access_token ="1328079922670219266-kLmrUhtK0h8nCRPUG16CDezEJQZySz"
access_token_secret ="MfFJhcY6cBRwBp8Fmbtj74bJnMz345WgjtKlRXxZ7bUwX"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api= tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Obtener informacion de uno mismo
def unoMismo():
    data=api.me()
    print(json.dumps(data._json,indent=2))
#Obtener informacion de alguna cuenta
def Tercero(nombre):
    data=api.get_user(nombre)
    print(json.dumps(data._json,indent=2))
#Obtener seguidores
def Seguidores(nombre,cantidad):
    for usuario in tweepy.Cursor(api.followers,screen_name=nombre).items(cantidad):
        print(json.dumps(usuario._json,indent=2))
#Obtener personas que sigue una cuenta
def Seguidos(nombre,cantidad):
    for usuario in tweepy.Cursor(api.friends,screen_name=nombre).items(cantidad):
        print(json.dumps(usuario._json,indent=2))
#Obter un timeline de tweets
def TimeLine(nombre,cantidad):
    for tweet in tweepy.Cursor(api.user_timeline,screen_name=nombre,tweet_mode="extended").items(cantidad):
        print(json.dumps(tweet._json,indent=2))
        print("============================================================")
#Obtener informacion sobre un tweet en especifico
def Tweets(consulta,cantidad):
    for tweet in tweepy.Cursor(api.search,q=consulta,tweet_mode="extended").items(cantidad):
        print(json.dumps(tweet._json,indent=2))
        print("============================================================")

#Obtener informacion sobre las tendencias
def TopTrends(woeid):
    trends = api.trends_place(id = woeid)
    for value in trends:
        for trend in value['trends']:
            print(trend['name'])

trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a
# dict which we"ll put in data.
data = trends1[0]
# grab the trends
trends = data["trends"]
# grab the name from each trend
names = [trend["name"] for trend in trends]
# put all the names together with a " " separating them
trendsName = " ".join(names)
print(trendsName)
#print (trends1)



#TopTrends(264) #woeid peru
#TopTrends(418440) #woeid peru
#TimeLine("Lui5Melgar",4)
#Tweets("#DenunciaLaTrampa",4)