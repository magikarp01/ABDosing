# ABDosing
A script for solving the "100 doses, allocate to populations with marker A and marker B". The script finds the optimal number of doses to give to patients with genetic marker B. The optimal dosing follows the Upper Confidence Bound algorithm from Multi-Armed Bandit Literature. 
See Auer, P., Cesa-Bianchi, N. & Fischer, P. Finite-time Analysis of the Multiarmed Bandit Problem. Machine Learning 47, 235–256 (2002). https://doi.org/10.1023/A:1013689704352

ABDosing.py is the simulation, with implementations of the UCB algorithm and random sampling methods to determine whether or not a patient given the drug would live. The sampling methods are Bernoulli distributions, where marker A has a live chance of 90% while marker B has a live chance of 50%. 

"AB Dosing Results.png" is a graph showing the optimal number of doses to give on the y-axis and the number of initial samples given to each marker population on the x-axis. For example, if 20 doses were given to both marker A and to marker B before the UCB algorithm was started (i.e., we have that data beforehand), the optimal number of doses would be somewhere around 34 according to the graph.

The UCB implementation uses confidence value c=sqrt(2). The simulation averages over 1000 trials for each number of initial samples.
