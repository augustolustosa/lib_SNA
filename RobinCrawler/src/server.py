'''
Created on 22/04/2012

@author: Jose Augusto Saraiva Lustosa Filho

'''
import Pyro.core

class Server(Pyro.core.ObjBase):
    global keyword, list_seeds, list_keywords
    
    keyword='vasco'
    
    list_seeds=[] #Lista com os usuarios sementes
    
    list_keywords=[] #lista de palavras chaves para procurar nos perfis dos usuários
    
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
    
    def getKeyword(self):
        return keyword
    
    def getSeeds(self):
        return list_seeds
    
    def getListKeywords(self):
        return list_keywords

class Main():
    def __init__(self):
        Pyro.core.initServer()
        daemon = Pyro.core.Daemon()
        uri = daemon.connect(Server(), 'obj')
        print 'Porta do daemon', daemon.port
        print 'URI do Objeto', uri
        daemon.requestLoop()

if __name__=='__main__':
    Main()
