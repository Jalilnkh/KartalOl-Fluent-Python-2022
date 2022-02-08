#%%
def CreateFirstPopulation(nop,nog):
    population=np.zeros([nop,nog])
    for i in range(nop):
        for j in range(4):
            population[i][j]=np.random.randint(4)+1
    return population


def FitnessFunction(population,Graph):
    rc=population.shape
    fit=np.zeros(1,rc[0])
    for i in range(0,rc[0]):
        pc=1
        for j in range(0,rc[1]):
            for k in range(j+1,rc[1]):
                if population[i][j]==population[i][k]:
                    if graph[j][k]==1:
                        pc=N
                        break
        colure=np.zeros(1,rc[1])
        for j in range(0,rc[1]):
            colure[population[i][j]]=1
        uc=sum(sum(colure))
        N=rc[1]
        fit[0][i]=2*N-uc-pc
    return fit
import numpy as np
Graph=np.ones([4,4])
for i in range(4):
    Graph[i][i]=0
nop=20
nog=4
population=CreateFirstPopulation(nop,nog)
print(population)

# %%
