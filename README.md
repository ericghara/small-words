# small-words
The number of combinations of 1 and 2 letter words from a repeating character string

## Motivation

This answers an interesting problem that was part of a larger (fictional) problem: an SHA hash of unknown length was encrypted into a cyphertext file and a key file.  Only the cyphertext was recovered--the key was lost.  The cypher algorithm is known: letters were converted into strings of numbers (A=1, B=2..Z=26) without delimiters, these delimiters were stored separately in the key file.  Without the key, decryption becomes ambiguous.  An example, BUBBLE is encrypted as 22122125 which could be decoded in many ways: BBLUY (2,2,12,21,25), is one of many possibilities.  While there are many complexities for generating the original plaintext, the greatest is introduced in regions where there are repeats of 1's and/or 2's.  In these 11.. and/or 22.. regions the complexity exponentially increases; 11 can be decoded as AA or K and 22 as BB or V. With a longer repeat block, 2222222 there are 21 possible permutations (BBBBBBB, VBBBBB, BVBBBB...). 

## Method

It quickly became apparent that calculating the number of permutations for these repeat blocks by iterative brute force methods was needlessly resource intensive.  A more finite method was developed by realizing that these repeating character problems can be broken down into discrete permutation with repetition problems--which are comparatively quick to solve. 

<p align="center"><code>n!/(n₂!⋅n₂₂!)</code></p align="center">

Using this method the permutations of 2222 for example can be broken down into the number of permutations of (2, 2, 2, 2), (22, 2, 2) and (22,22).

<p align="center"><code>(2,2,2,2): 4!/(4!⋅0!) = 1</code></p align="center">
<p align="center"><code>(22,2,2): 3!/(2!⋅1!) = 3</code></p align="center">
<p align="center"><code>(22,22): 1!/(1!⋅0!) = 1</code></p align="center">
<p align="center"><code>Sum = 5</code></p align="center">

Using this technique the increase in time for calculating the number of permutations increases linearly as the length of the repeat block increases, despite the logrithmic increase in number of permutations.

## Results
<table align="center">
    <tr>
      <th><a href=https://user-images.githubusercontent.com/87097441/130302256-19869ee4-446b-4c28-b0f4-17e99ed519b8.png><img src=https://user-images.githubusercontent.com/87097441/130302256-19869ee4-446b-4c28-b0f4-17e99ed519b8.png alt="Graph" height="auto" width="auto"></a></th>
    </tr>
    <tr>
  <td align="center"><b>The number of potential word permutations of cyphertext block containing <i>n</i> 2's</b><br><i>Note:</i> top figure graphed on a linear and the bottom on a logarithmic scale</td>
    </tr>
</table>

## Approximation
The solution above is a summation, which has a time complexity that is linearly correlated to the magnitude of its input.  I do not believe it is possible to further simplify this solution (although please contact me if you can!) but it should be possible to develop a reasonable approximation.  To this end a nonlinear least squares fit was calculated (scipy) using a model exponential function.  The training set was 1-30 repeats.  A wider training set could not be used due to the inability of scipy's backend to support >64 bit float precision.  Despite this, the fit proved quite acceptable even far outside the training set.

<table align="center">
    <tr>
        <td><a href=ttps://user-images.githubusercontent.com/87097441/130301665-4b1cee9a-087c-4dd7-88e9-5c612d1b21cd.png><img src=https://user-images.githubusercontent.com/87097441/130301665-4b1cee9a-087c-4dd7-88e9-5c612d1b21cd.png alt="Training Set" height="auto" width="475" /></a></td>
        <td><a href=https://user-images.githubusercontent.com/87097441/130301691-18f2f98b-325b-4ac9-b03b-488dad145608.png> <img src=https://user-images.githubusercontent.com/87097441/130301691-18f2f98b-325b-4ac9-b03b-488dad145608.png alt="Outside Training set" height="auto" width="475"/></a></td>
    </tr>
    <tr>
        <td align="center">Comparison of actual values to those calculated from exponential fit</td>
        <td align="center">Comparison of actual to fit beyond confines of training set</td>
    </tr>
    <tr>
        <td><a href=https://user-images.githubusercontent.com/87097441/130301767-722e135f-f647-4dc5-b99b-3c848c55898c.png> <img src=https://user-images.githubusercontent.com/87097441/130301767-722e135f-f647-4dc5-b99b-3c848c55898c.png alt="Residuals" height="auto" width="475"/></a></td>
     <td align="center"><a href=https://user-images.githubusercontent.com/87097441/130301784-c9ecfe31-9c3d-41e2-b34f-1834ccbea7d5.png> <img src=https://user-images.githubusercontent.com/87097441/130301784-c9ecfe31-9c3d-41e2-b34f-1834ccbea7d5.png alt="R²" height="auto" width="475"/></a>
 </tr>
    <tr>
        <td align="center">Residuals--deviation from predicted</td>
        <td align="center">R² Across increasing prediction ranges</td>
    </tr>
</table>

Visually the quality of the fit is difficult to assess due to the shear range of the y values (top 2 graphs).  Looking at the residuals shows us that within the training set, the fit is very good, displaying apparently random deviation from the actual value.  Outside of the training set the fit of the calculated function can only be called acceptable, with a nonrandom deviation from expected.  Despite this R² analysis shows an accurate approximation in the range of 1-100 character lengths.  With fitting methods that support larger numbers certainly better fits can be used, but I will leave this pursuit to someone else :).

## Conclusion
If you want to rigorously calculate the number of permutations of 2 and 22 in a repeating string, breaking down the problem into discrete permutation with repetition problems provides a very quick solution with O(x) time complexity.  If you seek an O(1) solution and can accept an approximation and the limitation to strings <90 characters this approximation is a good option:

<p align="center"><code>A⋅eᴮⁿ-C</code></p align="center">
<p align="center"><code>A = 0.72360693 B = 0.48121182 C = 0.00476934</code></p align="center">
