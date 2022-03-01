from math import log10

# QUANDO TEMOS ACIDOS OU BASES QUE LIBERAM MAIS DE 1 ION, MULTIPLICAMOS A CONCENTRAÇÃO PELO
# NUMERO DE IONS QUE ELA LIBERA. (LEMBRANDO, TEM QUE SER ACIDO E BASE FORTES)

V_acido = 0.025
C_acido = 0.1
V_base = 0.026
C_base = 0.1

N_acido = V_acido*C_acido
N_base = V_base*C_base

Vt = V_acido + V_base


print(f'Numero de mols de HCl é {N_acido}')
print(f'Numero de mols de NaOH é {N_base}')
print('\n')


if N_acido == N_base:
    print(f'A reação neutralizou')
elif N_acido > N_base:
    print(f'O numero de mols final é de HCl {N_acido-N_base}')
    print(f'A concentração é {(N_acido-N_base)/Vt}')
    print(f'O pH é {-log10((N_acido-N_base)/Vt)}')
else:
    print(f'O numero de mols final é de NaOH {N_base-N_acido}')
    print(f'A concentração é {(N_base-N_acido)/Vt}')
    print(f'O pH é {log10((N_base-N_acido)/Vt)+14}')
