# -*- coding: utf-8 -*-
import sys
from bintreeFile import Bintree
from QueueFunc import LinkedListQ

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
def writechain(nod):

    if nod.parent is not None:
        writechain(nod.parent)
    print(nod.word)

def makechildren(ordnod):
    lista = []
    ord = ordnod.word
    bokstaver = [*alfabet]

    for i in range(len(ord)):
        ordreset = [*ord]

        for bokstav in bokstaver:
            ordreset[i] = bokstav
            lista.append("".join(ordreset))

    lista.remove(ord)
    lista2 = []
    for pp in lista:
        if pp in svenska and pp not in oldkids:
            lista2.append(ParentNode(pp,ordnod))
            oldkids.store(pp)

    return lista2

def isthereaway(start, slut):
    startnod = ParentNode(start)
    q = LinkedListQ()
    q.enqueue(startnod)

    while not q.isEmpty():

        nextWord = q.dequeue()

        if nextWord.word == slut:
            writechain(nextWord)
            return nextWord

        else:
            newwords = makechildren(nextWord)
            for pp in newwords:
                q.enqueue(pp)

    return False



if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()


alfabet =  "abcdefghijklmnopqrstuvwxyzåäö"
svenska = Bintree()
with open("word3.txt", "r", encoding ="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet not in svenska:
            svenska.store(ordet)           # Lägg in i sökträdet

oldkids = Bintree()



startord = sys.argv[1]
slutord = sys.argv[2]

poop = isthereaway(startord,slutord)










