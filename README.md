# Boids
An implementation of [Craig Reynold's boids] in Python using NumPy and PyQtGraph. 

![](boids.gif)
###### Looks smooth when you run it. Choppiness is because of GIF. 

## Requirements
* Python3
* [NumPy]
* [PyQtGraph]

### Usage
Modify the CONFIG section in main.py or run main.py as is. 

### Tasks
 - [x] Implement in 2D
 - [ ] ~~Find nearest neighbours with k-d tree, reduces runtime of rules from O(n<sup>n</sup>) to O(nlogn)~~ (see explanation below) 
 - [ ] Fix GIF
 - [ ] Vectorize boid rules
 - [ ] Show directions of vectors on plot
 
### Extras 
 - [ ] Implement 'artificial' 2D boids
 - [ ] Implement in 3D with openGl
 - [ ] Add surface plot that 3D boids can interact with
 - [ ] Implement 'artificial' 3D boids


### Why K-D Tree was not implemented. 
- Linear computation of euclidean distances take O(N) time. 
- However, with K-D tree while search is quick O(2<sup>d</sup>LogN), K-D tree generation takes O(NLogN) time, whereas with linear computation there is no 
generation time because we are using an array that has already been filled. For our purposes, we would have to generate a K-D tree on each of our N iterations of 
the array of points. 

- Linear search gives a runtime of O(N<sup>N</sup>). 
- With N iterations of our array of points, K-D tree gives a total runtime of O((2<sup>d</sup>LogN * NLogN)<sup>N</sup>) =~ O(NLogN<sup>N</sup>) =~ O(N<sup>N</sup>). 

If one considers Big O time as it is commonly defined, the implementations are equal, however it is clear that in this case linear search is simply better suited for our purposes. 

[Craig Reynold's boids]: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/modeling-natural-systems/boids.html
[NumPy]: https://numpy.org/
[PyQtGraph]: https://pypi.org/project/pyqtgraph/
