'''
Created on 14/04/2012

@author: José Augusto Saraiva Lustosa Filho

'''

class Graph(object):

    def __init__(self, data=None, name=''):
        self.adj={}   #Lista de adjacencia vazia
        self.name=name #nome do grafo.
    
    
    def __str__(self):
        return self.name  #Retorna o nome do grafo.
    
    
    def __iter__(self):
        return self.adj.iterkeys()
    
    
    def get_neighboring(self,no): #retorna uma lista com os vizinhos do no especificado.
        return self.adj[no].iterkeys()
    
    
    def has_neighbor(self, u, v): # verifica se u é vizinho de v.
        return self.adj.has_key(u) and self.adj[u].has_key(v)
    
    
    def get_all_nodes(self): #retorn todos nós do grafo.
        return self.adj.keys()
    
    
    def get_number_nodes(self):  #retorna a quantidade de nós
        return len(self.adj)
    
    
    def has_node(self,no):  #Verifica se o nó está no grafo. Caso sim, retorna True.
        if no in self.adj:
            return True
        
    
    def nodes_coincident(self,graph2=None): #retorna os nós coincidentes nos dois grafos.
        if graph2 is None: #verifica se o graph2 é vazio.
            res = self.__init__() #caso seja vazio, retorna todos nós de graph2.
        elif graph2 in self: #verifica se o nó é unico e coincidente no conjunto.
            res = [graph2] #caso seja unico e coincidente, adiciona no grupo.
        else:  #verifica a coincidencia de nó por nó //pior caso 
            try:
                for no in graph2:
                    if no in self:
                        res+=[no]
            except:
                print 'Error in processing of graph'
        return res
    
    
    def add_node(self,no):  #Adiciona um nó
        if no not in self.adj:
            self.adj[no]={}
    
    
    def add_list_nodes(self, list_nodes): #Adiciona multiplos nós
        for no in list_nodes:
            if no not in self.adj:
                self.adj[no]={}
                
                
    def del_node(self,no): #remover um nó do grafo
        try:
            for i in self.adj:
                del self.adj[i][no]
            del self.adj[no]
        except TypeError:
            print 'Not possible removal all nodes'
    
    
    def del_list_nodes(self,list_nodes): #remover vários nós do grafo
        for i in list_nodes:
            try:
                for n in list_nodes[i]:
                    del self.adj[n][i]
                del self.list_node[i]
            except TypeError:
                print 'Not possible removal all nodes of list'
    
    
    def has_edge(self, u, v=None): #verifica se a aresta está contida no grafo. Caso não retorna False
        if v is None:
            (u,v)=u
        if self.adj.has_key(u) and self.adj.has_key(v):
            return True
        return False

    
    def add_edge(self, u, v=None): #adiciona uma aresta
        if v is None: #verifica se o segundo no nao foi passado como parametro
            (u,v)=u
        if u not in self.adj: #verifica e adiciona o no no grafo
            self.adj[u]={}
        if v not in self.adj:#verifica e adiciona o no no grafo
            self.adj[v]={}
        if v==u: #evita loops
            return
        
        self.adj[u][v]=None #adiciona a aresta.
        self.adj[v][u]=None #lembrando que o grafo é bidirecional.
            

    def add_list_edges(self, list_edges): #adiciona uma lista de arestas.
        for edge in list_edges:
            (u,v)=edge
            if u not in self.adj:
                self.adj[u]={}
            if v not in self.adj:
                self.adj[v]={}
            if u==v:
                return
            self.adj[u][v]=None
            self.adj[v][u]=None
        
        
    def del_edge(self, u, v=None): #Deleta uma aresta no grafo. 
        if v is None:
            (u,v)=u
        if self.adj.has_key(u) and self.adj.has_key(v):
            del self.adj[u][v]
            del self.adj[v][u]
            
            
    def del_list_edges(self, list_edges): #Delete uma lista de arestas do grafo.
        for edge in list_edges:
            (u,v)=edge
            if self.adj.has_key(u) and self.adj.has_key(v):
                del self.adj[u][v]
                del self.adj[v][u]
        
    def edges_coincident(self, graph2=None):
        if graph2 is None:
            res = self.__iter__()
        elif graph2 is self:
            res = [graph2]
        else:
            try:
                for n in graph2:
                    if n in self:
                        res = n                
            except TypeError:
                res=[]
                
        see={}
        for i in res:
            for x in self.adj[i]:
                if x not in graph2:
                    yield (i,x)
            see[i]=1
        del(see)       
    
   
    def degree_node(self, graph2=None): #retorna o grau de um nó.
        if graph2 is None:
            res= self.__iter__()
        elif graph2 in self:
            res=[graph2]
        else:
            try:
                for n in graph2:
                    if n in self:
                        res=[n]
            except TypeError:
                res=[]
        for n in res:
            yield len(self.adj[n])
            
    def clear(self):  #Remove o nome e todos nós e arestas de um grafo.
        self.name=''
        self.adj.clear()
    
    def number_edges(self): #retorna a quantidade de nós no grafo.
        return sum(self.degree_node())/2
    

    
    
    
    
        