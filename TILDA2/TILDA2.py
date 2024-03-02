import sys
from linkedQFile import LinkedListQ
from IndexListQFile import IndexlistQ


def trolleritrick( siffror ):
    trolleri_ordning = []
    #q = IndexlistQ()
    q = LinkedListQ()
    for x in siffror:
        q.enqueue(x)

    for xx in range(len(siffror)):
        i = q.dequeue()
        q.enqueue(i)
        ii = q.dequeue()
        trolleri_ordning.append(ii)

    return trolleri_ordning

def main():
    #line = input("Vilken ordning ligger korten i?")
    #line = "7 1 12 2 8 3 11 4 9 5 13 6 10"
    line = "3   1   4   2   5"
    #line = sys.stdin.readline()
    siffror = line.strip().split()
    trollning = trolleritrick( siffror )
    for x in trollning:
        print(x, end=" ")
        print()

main()
