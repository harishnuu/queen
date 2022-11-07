from itertools import permutations
N=8
sol=0
cols = range(N)
for combo in permutations(cols):
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol+= 1
        print('solution'+str(combo)+'\n')
        print("\n".join('.'*i+'Q'+'.'*(N+1)for i in combo)+"\n\n\n\n")
