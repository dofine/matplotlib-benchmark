# matplotlib-benchmark

## Problem
Problem is that I need to draw many pictures in a for loop, with different data each time. Using `matplotlib.pyplot` interface is far too slow. ~~or I didn't do it the right way.~~ 
Besides, the `matplotlib` tutorials and docs are not very specific about the object-oriented API.
So I did a lot of Googles and Stackoverflows, then I came up with this little benchmark of different plotting interface test. Speed is the very first consideration. 

Code is in [bench.py](bench.py).

## Result
It seems that the right way to do what I need is: Do not redraw everything. Just update data each time, as the function `draw3` does in [bench.py](bench.py). 

Surprisingly the first two methods don't differ too much when using `Agg` backend. While using `Qt5Agg` backend, `draw1` will beat `draw2` by about 15%. Almost for all three methods except `draw1`, `Agg` beats `Qt5Agg`.

Function | `Agg` time| `Qt5Agg` time|
------------ | ------------- | ----------|
`draw1` | 8.235049673209932 | 7.974657052376608
`draw2` | 8.106147522373316 | 9.609950379663687
`draw3` | 5.5861171293730365 | 5.752674005524984

**Note**: time unit in the table is seconds.




## Ref

1. [When to use cla\(\), clf\(\) or close\(\) for clearing a plot in matplotlib? \- Stack Overflow](https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib)
2. [python \- Create a figure that is reference counted \- Stack Overflow](https://stackoverflow.com/questions/16334588/create-a-figure-that-is-reference-counted)
3. [python \- How to update a plot in matplotlib? \- Stack Overflow](https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib/4098938#4098938)