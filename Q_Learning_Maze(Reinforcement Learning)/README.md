# FIND THE TREASURE AT AN ARBITRARY POINT IN A GIVEN MAZE USING Q-LEARNING(REINFORCEMENT LEARNING)


### PROBLEM STATEMENT : 
Use Quality function and Reinforcement Learning to find the treasure as fast as you can in a given maze.

_Language used_ : **Python**

_Library used_ : **[numpy](https://numpy.org/)** and **[matplotlib](https://matplotlib.org/)**

_Models used_ : **[Maze generation Algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)** and **Q-Learning(Epsilon Greedy)**


### CODE EXPLATION [Q_LEARNING_MAZE.IPYNB](https://github.com/smitz94/Projects/blob/master/Q_Learning_Maze(Reinforcement%20Learning)/Q_Learning_Maze.ipynb)
* Generate a maze using sample algorithm given on **wiki** and pick a random target point as **TREASURE**.

* Use Q-learning with Epsilon- Greedy Algorithm to solve the problem.

* Train the neural network to generate optimal strategy.

* PLot the traversal of the network through the maze.

### RESULTS

> **MAZE+TREASURE**

![](https://github.com/smitz94/Projects/blob/master/Q_Learning_Maze(Reinforcement%20Learning)/maze%2Btarget.png)

> **SIMPLE RANDOM WALK**

![](https://github.com/smitz94/Projects/blob/master/Q_Learning_Maze(Reinforcement%20Learning)/random_walk.png)

> **RANDOM WALK WITH Q-LEARNING REWARD**

![](https://github.com/smitz94/Projects/blob/master/Q_Learning_Maze(Reinforcement%20Learning)/random_walk_q-learning.png)

> **FINAL RESULT**

![](https://github.com/smitz94/Projects/blob/master/Q_Learning_Maze(Reinforcement%20Learning)/final_result.png)




### CONCLUSION

* We can tweek the hyperparameters and try to optimize the solution.
