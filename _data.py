from _core import *

Slection=[]

Scenes=[]

Helpers=[]

ModelObjects=[]


BigworldModels=[]

data=[Scenes,ModelObjects,Slection,BigworldModels]

def test():
    for s in data:
        print len(s)
    for s in ModelObjects:
        print s.name
        print len(s.mesh.faces)/3