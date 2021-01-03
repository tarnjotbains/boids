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
 - [ ] Find nearest neighbours with k-d tree, reduces runtime of rules from O(n<sup>n</sup>) to O(nlogn)
 - [ ] Fix GIF
 - [ ] Vectorize boid rules
 - [ ] Show directions of vectors on plot
 - [ ] Implement 'artificial' 2D boids
 - [ ] Implement in 3D with openGl
 - [ ] Add surface plot that 3D boids can interact with
 - [ ] Implement 'artificial' 3D boids





[Craig Reynold's boids]: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/modeling-natural-systems/boids.html
[NumPy]: https://numpy.org/
[PyQtGraph]: https://pypi.org/project/pyqtgraph/
