# Experiment "exp1"

## Introduction

Agent rules are limited to:

* Energy starts at 10
* Every action {move, eat} costs 1 energy.
* Age starts at 1
* Agent dies if energy < 1
* If energy == 20, produce a new agent (offspring) in an empty surrounding cell

The universe keeps a log of all activity of all entities. Here is an example readout:
```
1. CA44 moved from X24Y08 to X25Y08. (-1 energy).
2. CA45 predicts that the plant at X44Y44 is edible and eats it. Oops! It's poison. CA45 dies.
3. CA46 predicts that the plant at X03Y90 is edible and eats it. Yum! (+10 energy).
 
```

Future logs might have something like:

```
4. CA47 tries to share knowledge with CA10 but she doesn't know anything about the plants yet :<
5. CA48 shares knowledge about edible plants with CA31. (-1 energy).
```

CA Rules:
* Energy starts at 100
* Every action takes 1 energy.
* Every turn, take an action:

CA Actions:
If E < 


Research Questions:
* What are some interesting differences between the decision trees of those who
survived > 100 days and those who did not? 

* Does the # of agents change how long any one agent can survive? In other words,
does the size of the agent population have a linear impact (positive or negative)
on the age of the oldest agent at the end of a certain number of days?

* Scarcity. Does the frequency in which plants regrow affect the survivability of the population?

* Scarcity. What is different in the population when we compare one test with plants that continue
to regrow until every cell has a plant with a test where there are a maximum number
of plants that can be in the system at any one time? 

## Methods

## Results

## Conclusions
