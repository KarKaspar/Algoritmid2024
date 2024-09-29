alglist=input("anna mingi järjekord ")
alglist=alglist.split(",")

def eemalda():
    alglist.remove(alglist[-1])
def lisa(lisada):
    alglist.insert(0,lisada)
def piilu():
    return alglist[0]
def kontrolli():
    if len(alglist)==0:
        return "tühi"
    else:
        return "olemas"
def suurus():
    return len(alglist)