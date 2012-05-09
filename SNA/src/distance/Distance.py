'''
Created on 14/04/2012

@author: José Augusto Saraiva Lustosa Filho

'''

    
def eccentricity(G, v=None):
    nodes=[]
    if v is None:
        nodes.G.get_all_nodes()
    elif isinstance(v, list):
        nodes=v
    else:
        nodes=[v]
    
    e={}
    for i in nodes:
        tam = list_shortest_path_length(G,i)
        try:
            assert len(tam)==G.get_number_nodes()
        except TypeError:
            print "Graph is not connected"
        e[i]=max(tam.values)
    
    if len(e)==1: 
        return e.values()[0]
    
    return e.values()
    
def list_shortest_path_length(G,v):  
    seen={}                  # level (number of hops) when seen in BFS
    level=0                  # the current level
    nextlevel={v:1}  # dict of nodes to check at next level
    while nextlevel:
        thislevel=nextlevel  # advance to next level
        nextlevel={}         # and start a new list (fringe)
        for i in thislevel:
            if not seen.has_key(i): 
                seen[i]=level # set the level of vertex v
                nbrs=dict.fromkeys(G.get_neighboring(i),1)
                nextlevel.update(nbrs) # add neighbors of v
        level=level+1
    return seen  # return all path lengths as dictionary
        
        
def diameter(G): #retorna o diametro do grafo G.
    return max(eccentricity(G))


def radius(G): #retorna o raio do grafo G
    return min(eccentricity(G))


def center(G,e=None): #retorna o centro de um grafo G
    if e is None:
        e=eccentricity(G)
    radius=min(e)
    res=[i for i in e if e[i]==radius]
    return res
    


