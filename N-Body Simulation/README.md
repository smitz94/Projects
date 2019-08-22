# N-BODY SIMULATION

### Problem Statement : 
Write a program to simulate the motion of n particles in the plane, mutually affected by gravitational forces, and animate the results.

_Language used_ : **JAVA**

_Algorithm used_ : **BARNES-HUT QUAD TREE STRUCTURE**

_Library used_ : **[StdDraw.java](https://introcs.cs.princeton.edu/java/stdlib/javadoc/StdDraw.html)**



> ### BARNES-HUT ALGORITHM (QUAD TREE STRUCTURE FOR 2D PROBLEM)

In a Two-dimensional n-body simulation, the Barnes–Hut algorithm recursively divides the n bodies into groups by storing them in an quad-tree. 
Each node in this tree represents a region of the two-dimensional space. 
The topmost node represents the whole space, and its four children represent the four octants of the space. 
The space is recursively subdivided into quadrants until each subdivision contains 0 or 1 bodies (some regions do not have bodies in all of their quadrants). 
There are two types of nodes in the quad-tree: internal and external nodes. An external node has no children and is either empty or represents a single body. 
Each internal node represents the group of bodies beneath it, and stores the center of mass and the total mass of all its children bodies.

> Explanation :

![Quad-Tree Structure Representation](https://github.com/smitz94/Projects/blob/master/N-Body%20Simulation/barnes-hut%20quad%20tree%20structure.png)

> **you can further watch the basic division of the tree in detail in the video below:**

#### [Quad-Tree Structure](https://www.youtube.com/watch?v=0eKQXPAcQK8&t=11s)
