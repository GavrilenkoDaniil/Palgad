from funktsioonid import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]






#3
def suurim_palk(i:list,p:list):
    """
    :rtype float,str:
    """
    suurim=max(p)
    b=p.index(suurim)
    kellel=i[b]
    return suurim,kellel

#10
def keskmine(i,p):
    """
    :rtype var:
    """
    summa=0
    for palk in p:
        summa+=palk
    kesk=summa/len(p)
    print(kesk)
    vahe=0
    if 0<=p.index(kesk)<len(p)-1:
        kes=i[p.index(kesk)]
        return kesk
    else:
        kesk="Puudub"
        return kesk