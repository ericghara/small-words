from math import factorial
%matplotlib widget # note delete if running code outside of Jupyter notebook
import matplotlib.pyplot as plt

def combo2(lnth):
    twtytwo = 0 # num of 22s
    perms = 0
    # iterate quantities of 2's and 22's to permutate
    while 2*twtytwo <= lnth:
        twos = lnth-twtytwo*2
        n = twos+twtytwo
        # formula n!/(n₂!*n₂₂!) ; ie permutation with repititions formula for 2 types of objects  
        perms +=int( factorial(n)/( factorial(twos)*factorial(twtytwo) ) )
        twtytwo +=1
    return perms

# iterate 1-6   
x0 = [*range(1,7)]
y0 = [combo2(i) for i in x0]
 
# plot 1-6
ylabel = 'Permutations'
xlabel = 'Number of 2\'s'
f, (ax1, ax2) = plt.subplots(2, 1, sharey=False, figsize=(8,10))
ax1.plot(x0,y0)
ax1.set_yscale("linear")
ax1.set_ylabel(ylabel)
ax1.set_xlabel(xlabel)
ax1.set_xticks((1,2,3,4,5,6))
plt.figure(figsize=(2, 2), dpi=80)

# iterate 1-100    
x1 = [*range(1,101)]
y1 = [combo2(i) for i in x1]   
  
# plot 1-100
ax2.plot(x1,y1)
ax2.set_yscale("log")
ax2.set_ylabel(ylabel)
ax2.set_xlabel(xlabel)
