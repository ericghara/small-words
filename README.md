# small-words
The number of combinations of 1 and 2 letter words from a repeating string

## Motivation

This answers an interesting problem that was part of a larger (fictional) problem: an SHA hash of unknown length was encrypted into a cyphertext file and a key file.  Only the cyphertext was recovered--the key was lost.  The cypher algorithm is known: letters were converted into strings of numbers (A=1, B=2..Z=26) without delimiters, these delimiters were stored separately in the key file.  Without the key, decryption becomes ambiguous.  An example, BUBBLE is encrypted as 22122125 which could be decoded in many ways: BBLUY (2,2,12,21,25), is one of many possibilities.  While there are many complexities for generating the original plaintext, the greatest is introduced in regions where there are repeats of 1's and/or 2's.  In these 11.. and/or 22.. regions the complexity exponentially increases; 11 can be decoded as AA or K and 22 as BB or V. With a longer repeat block, 2222222 there are 21 possible permutations (BBBBBBB, VBBBBB, BVBBBB...). 

## Method

It quickly became apparent that calculating the number of permutations for these repeat blocks by iterative brute force methods was needlessly resource intensive.  A more finite method was developed by realizing that these repeating character problems can be broken down into discrete permutation with repetition problems--which are comparatively quick to solve. 

```
n!/(n₂!⋅n₂₂!)
```
Using this method the permutations of 222 for example can be broken down into the number of permutations of 2, 2, 2 and the number of permutations of 22, 2.
```
(2,2,2): 3!/(3!⋅0!) = 1

(2,22): 2!/(1!⋅1!) = 2
```
Using this technique the number of permutations of extremely long repeats can be easily calculated despite the logarithmic increase in complexity above repeat lengths of ~5.

## Results
<table>
    <tr>
      <th><a href=https://user-images.githubusercontent.com/87097441/130053642-d183c08f-9a2a-4c6d-9640-919c99cd4c82.png><img src=https://user-images.githubusercontent.com/87097441/130053642-d183c08f-9a2a-4c6d-9640-919c99cd4c82.png alt="Graph" height="auto" width="auto"></a></th>
    </tr>
    <tr>
  <td align="center"><b>The number of potential word permutations of cyphertext block containing <i>n</i> 2's</b><br><i>Note:</i> top figure graphed on a linear and the bottom on a logarithmic scale</td>
    </tr>
</table>
