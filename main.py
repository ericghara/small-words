from math import factorial, prod
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
#%matplotlib widget 
# note delete if running code outside of Jupyter notebook

def combo2(lnth):
    # Depreciated.  opt_combo2 offers ~ equivilent perofmrance for small lnth 
    # and significantly improved performance for large lnth
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

def opt_combo2(lnth):
    # Optimized combo2
    # Optimization of this formula a!/(b₂!*c₂₂!)
    # Where a is always > b or c
    b = 0 # number of two character letters
    perms = 0 # number of permutations
    while 2*b <= lnth:
        c = lnth-2*b
        a = b+c
        # factors a!/(b!*c!) to reduce number of factorial operations
        if b >= c:
            #factor out b
            factor = b
            denom = factorial(c)
        else:
            #facor out c
            factor = c
            denom = factorial(b)
        perms +=prod(range(a,factor,-1))/denom
        b +=1
    return perms

## Make Plots ##
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
ax1.set_xlim((1,6))

# iterate 1-100    
x1 = [*range(1,101)]
y1 = [combo2(i) for i in x1]   
  
# plot
ax2.plot(x1,y1)
ax2.set_yscale("log")
ax2.set_ylabel(ylabel)
ax2.set_xlabel(xlabel)
ax2.set_xlim((1,100))
f.show()

## Fit
def exponential(x,A,B, C):
    # A⋅e^(B*x)-C
    return A*np.exp(B*x)-C
    
x  = np.array([*range(1,31,1)])
y = np.array([combo2(i) for i in x])

#Fit exponential
popt, pcov = optimize.curve_fit(exponential, x,y, bounds=(-np.inf, np.inf), maxfev = 800)
#print(popt)
yEXP = exponential(x, *popt)
plt.figure()
ylabel = 'Permutations'
xlabel = 'Number of 2\'s'
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.plot(x, y, label='Actual Data', marker='o')
plt.plot(x, yEXP, 'r-',ls='--', label="Exponential Fit")
plt.yscale("Log")
plt.xlim((1,30))
plt.legend()
#plt.show()

#Optimized Values
print("Values",popt)

# Plot Fit
xOut = np.array([*range(31,101)])
yOut = np.array([combo2(i) for i in xOut])
yOut_EXP = np.array([exponential(i, *popt) for i in xOut])
plt.figure()
plt.plot(np.hstack((x,xOut)), np.hstack((y,yOut)), 'grey', label='Actual Data')
plt.plot(x, yEXP, 'g-',ls=':', label="Exponential Fit")
plt.plot(xOut, yOut_EXP, 'r-',ls=':', label="Fit Outside Training Set")
plt.yscale("Log")
plt.legend()
plt.xlim((1,100))
plt.ylabel(ylabel)
plt.xlabel(xlabel)
#plt.show()


# Residuals
residuals = np.hstack((y,yOut))-np.hstack((yEXP, yOut_EXP)) #data-fit
plt.figure()
plt.plot(np.hstack((x,xOut)),residuals)
plt.yscale("Log")
ylabel = 'Residual (deviation from predicted)'
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.xlim((1,100))
#plt.show()

# Residuals - weighted
#wResiduals = residuals/np.hstack((y,yOut))*100
#plt.figure()
#plt.plot(np.hstack((x,xOut)),wResiduals)
#plt.yscale("Linear")
#ylabel = 'Percent Residual'
#plt.ylabel(ylabel)
#plt.xlabel(xlabel)
#plt.ylim((-20,100))
#plt.xlim((0,100))

#R²
allY = np.hstack((y,yOut))
meanY = sum(allY)/len(allY) 
#print(" String Length     R²  ")
R2Lst = []
for i in range(1,101,1):
    rss = 0 # sum of squares of residuals
    tss = 0 # total sum of squares
    for val, res in zip(allY[0:i],residuals[0:i]):
        tss += (val-meanY)**2
        rss += (val-res)**2
    R2 = 1-rss/tss
    R2Lst.append(R2)
    #print("0 -%3d repeats: % 2.3f "%(i,R2))

    
# R² Plot
plt.figure()
plt.plot(np.hstack((x,xOut)),R2Lst)
plt.yscale("Linear")
ylabel = 'R²'
plt.ylabel(ylabel)
plt.xlabel("Data Range (0 to n)")
plt.xlim((1,100))
plt.show()

