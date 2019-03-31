# Contextually Limited Maximum System Information

Max entropy for a system of two possible outcomes for each instance of probable outcomes:

$$I = \sum^N_{i=1}{P_i log_2(1/P_i)}$$

Maximum information known is: $log(N)$

Example association given an Association Context $A_C$ and Maximum Information (due to genetic characteristics) $I_{max}$:

Assumptions: 
* Genetic Characteristics (GCs) are mutable[^mutable]
* Maximum Information in any context is determine by a GC
* $I_{max} = \log{N}$ (Shannon)
* $N_{max} = G(N_{max})$, where $G$ is the set of GCs specific to this CA and $G_N$ is the maximum $N$ this CA can account for in any hypothetical association computation $C_H$

A CA's maximum information processable for a hypothetical association under a given context is expressed as:

$$\lim_{N\to{G_{N}}}{I_{max}} = \log{G(N_{max})}$$

There is another factor, though, and that is the maximum number of cells a particular CA can account for when trying to calculate hypothetical outcomes. Since we represent the universe on a 2D grid, we use the Manhattan distance to account for range. Maximum range for calculating hypothetical outcomes can be expressed as:

The number of cells in a 2-dimensional von Neumann neighborhood of range _r_ can be expressed as 

$$ r_{max} = 1 + 2r(r+1)$$

And as a function of a CA's GCs:

$$ r_{max} = 1+2G(r_{max})[G(r_{max})+1]$$

So if a maximum range given by genetic characteristic $G(r_{max})$ is 2, the visible area $V$ (i.e., the cells that can be accounted for in any hypothetical computation) would be:

$$ V_{r=2} = 1+[(2\times{2})(2+1)] = 13$$

Expressed visually:

![Von Neumann Neighborhood](http://www.jcasim.de/main/img14.gif)
This gives us the range of all cells near the CA that will be taken into account for every hypothetical computation.

A tile taken into account this way is expressed with the following data elements:
* Distance to CA

## Deriving an appropriate $G_N$ for testing
To establish appropriate values for $G_N$, we should create a set of CAs with different capacities for information processing.

Let's start with two. $A_1$ will be able to process all of the information no matter what $N$ is. $A_2$ will be able to process 50% of what $A_1$ can. Put another way, $A_2$ will be half as capable of processing information as $A_1$.

Controlling for context, let's say we have the following hypothetical associations:

In the context of "finding food":

Given a von Neumman neighborhood of:
|-|X1|X2|X3|X4|X5|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**Y5**|&nbsp;| | | | |
|**Y4**|&nbsp;| | | | |
|**Y3**|&nbsp;| |X| | |
|**Y2**|&nbsp;| | | | |
|**Y1**|&nbsp;| | | | |

| # | action | location | outcome | 
|----|-----|-------------|-----------|
| 1 | move_up | &tile | 


Which tile near me is most likely to contain food?
Which tile near me is most likely to contain poison?





[^mutable]: During reproduction the GCs are mutable, but for the purpose of this example we will hold them constant.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1NDk2NDgxOSwxNzcxNTkwNDgxXX0=
-->