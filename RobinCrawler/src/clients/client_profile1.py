'''
Created on 22/04/2012

@author: Jose Augusto Saraiva Lustosa Filho

'''

import urllib,urllib2
import Pyro.core
import sys
import re
from BeautifulSoup import BeautifulSoup
import tweepy

server = Pyro.core.getProxyForURI('PYROLOC://192.168.157.1:7766/obj')

list_profiles_seeds = server.getSeeds()
list_keywords = server.getListKeywords()

profiles= file('profiles.txt','a')

consumer_key = 'BIEBYwhHBLi9GwMDTIHLhw'
consumer_secret = '7VmjXrQbrtTSlQRqln4Tu0UkhD8xaXUqaeFqIqUkHM'
access_token = '413845046-6ZxeUQFgn1HMkxP3Khzq5IDqJxLvdlhUAZiTyuaU'
access_token_secret = 'tPboV1a5qvZXVPsCjImhlvIFy795InRZqt2HVSUmg'        


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def busca(self, list_profiles_seeds, list_keywords):
    coleta_seeds(list_profiles_seeds)  #coleta os seguidores dos usuários sementes e joga num arquivo, chamado 'profiles_childrens'
    coleta_childrens(list_keywords) #pega os filhos do usuário semente e verifica se a descricao deles contém alguma palavra igual à lista de keyword.

    
    
def coleta_seeds(self, list_profiles_seeds):
    for profile in list_profiles_seeds():
        for friend in tweepy.Cursor(api.friends, id=profile).items(100):
            profiles.write(friend.screen_name)
        
        for follower in tweepy.Cursor(api.followers, id=profile).items(100):
            profiles.write(follower.screen_name)
    
    
def coleta_childrens(self, list_keywords):
    arq = open('profiles.txt','a')
    for keyword in list_keywords:
        pattern = '(.+)'+keyword+'(.+)'
        profiles=arq.realines()
        for profile in profiles:
            user = api.get_user(profile)
            if(re.match(pattern, user.description, re.IGNORECASE)):
                arq.write(user.screen_name)
            else:
                arq_prof = open('profiles.txt','r')
                content = arq_prof.read()
                arq_prof.close()
                result_profile = content.replace(profile,'')
                arq_prof = open('profiles.txt','w')
                arq_prof.write(result_profile)
                arq_prof.close()                
    arq.close()
    
    
    
