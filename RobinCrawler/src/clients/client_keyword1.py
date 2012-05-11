'''
Created on 22/04/2012

@author: Jose Augusto Saraiva Lustosa Filho

'''
# -*- coding: utf-8 -*-
import Pyro.core
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import BasicAuthHandler
from tweepy.api import API
import tweepy
import sys
import os
    


server = Pyro.core.getProxyForURI('PYROLOC://192.168.157.1:7766/obj')

keyword = server.getKeyword()

consumer_key = 'BIEBYwhHBLi9GwMDTIHLhw'
consumer_secret = '7VmjXrQbrtTSlQRqln4Tu0UkhD8xaXUqaeFqIqUkHM'
access_token = '413845046-6ZxeUQFgn1HMkxP3Khzq5IDqJxLvdlhUAZiTyuaU'
access_token_secret = 'tPboV1a5qvZXVPsCjImhlvIFy795InRZqt2HVSUmg'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            tweets = file('C:\Users\kakaroto\Desktop\tweets.txt','w')
            print '%s' %status.text
            tweets.write(status.text, status.author.screen_name, status.created_at, status.source)
            tweets.close()
        except TypeError:
            print 'Erro encontrado'
            pass
            
    
    def on_error(self, status_code):
        print 'Erro encontrado com:', status_code
        return True
    
    
    def on_timeout(self):
        print 'zZzZzZZ...timeout...zZzZzZzZ'
        return True


streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

print 'Capturando tweets...'

streaming_api.filter(track=keyword)