from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding ="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.store(ordet)           # Lägg in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding ="utf-8") as engelskfil:
    for row in engelskfil:
        for word in row.split():
            Word = word.strip('.,!-"')
            if Word not in engelska:
                engelska.store(Word)
                if Word in svenska:
                    print(Word, end = " ")

"""""
def make_tree_from_input():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.store(data)
        data = input().strip()
    return tree

def search_input(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = make_tree_from_input()
    search_input(tree)

main()
"""""




