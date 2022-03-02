from numpy import arange
from math import sqrt, log10

lista = [0, 1, 1.5] + [i for i in range(2, 31, 1)] + [31.5] + [i for i in range(32, 38, 1)] + [
    37.5] + list(map(lambda x: x/10, arange(380, 402, 2))) + [40.5] + [i for i in range(41, 49, 1)]

# Esse programa determina o pH de uma solução, sendo o acido ou a base fracos ( Um tem que ser forte )

for i in lista:

    weak_acid = True
    weak_base = False
    Ka = 1.8*10**-5
    Kb = None
    Kw = 10**-14
    Ca = 0.1
    Va = 0.04
    Cb = 0.1
    Vb = i/1000

    # Acima é input, abaixo é conta

    Ka, Kb = map(lambda x: 1 if x == None else x, [Ka, Kb])
    Kh = Kw/Ka*Kb

    Na = Ca*Va
    Nb = Cb*Vb
    Vt = Va+Vb

    if weak_acid:
        if Na == Nb:
            Csalt = Na/Vt
            Coh = sqrt(Kh*Csalt)
            #print(f"O pH da solução é: {14+log10(Coh)}")
            print(f'{14+log10(Coh)}')
        elif Na > Nb:
            Csalt = Na/Vt if Na < Nb else Nb/Vt
            Na = Na - Nb
            Ca = Na/Vt
            Ch = sqrt(Ka*Kb*Ca) if Csalt == 0 else Ka*Kb*Ca/Csalt
            #print(f"O pH da solução é: {-log10(Ch)}")
            print(f'{-log10(Ch)}')
        else:
            Csalt = Na/Vt if Na < Nb else Nb/Vt
            Nb = Nb - Na
            Coh = Nb/Vt
            #print(f"O pH da solução é: {14+log10(Coh)}")
            print(f'{14+log10(Coh)}')
    elif weak_base:
        if Na == Nb:
            Csalt = Na/Vt
            Ch = sqrt(Kh*Csalt)
            print(f"O pH da solução é: {log10(Ch)}")
        elif Na > Nb:
            Csalt = Na/Vt if Na < Nb else Nb/Vt
            Na = Na - Nb
            Ch = Na/Vt
            print(f"O pH da solução é: {-log10(Ch)}")
        else:
            Csalt = Na/Vt if Na < Nb else Nb/Vt
            Nb = Nb - Na
            Cb = Nb/Vt
            Coh = sqrt(Ka*Kb*Cb) if Csalt == 0 else Ka*Kb*Cb/Csalt
            print(f"O pH da solução é: {14+log10(Coh)}")
