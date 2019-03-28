# Social Cellular Automata Research Experiments (SCARE)

Imagine a discrete grid populated by autonomous agents. This discrete grid is a universe that has the following entities in it:
1. Plants. Seeds are harvested from plants 
2. One CA per grid; grids can be occupied by both a CA and a plant.
3. 
4. It takes one unit of "food" to perform an action. 
5. An action is either {move, share_knowledge, learn, reproduce, build_nest}

Thought:
* A thought can be shared by CAs
* A thought has a category {food, shelter, reproduction, 

Computed Individual characteristics:
* Social Value. If this CA has not learned a lot from other CAs, it will be less likely to care about other CAs. 

### Scenarios
**Poisoned Plants**. If we have some plants that are poison, how would we communicate to other CAs not to eat them? 
* Proximity to poison plant consumption. If $C_1$ "witnesses" $C_2$ eating a poison plant and then dying, it will "associate" action:eat, target:plant_type, outcome:death.

**Scarcity.** How does scarcity among different environmental variables affect CAs?
* Scarcity of suitable mates
* Scarcity of food
* Scarcity of shelter materials



### Universal truths
Some universal truths are pre-programmed into each CA at the start of the universe. These are biological imperatives--drives that exist on an instinctual level. 
* Every action requires one unit of food.
* There are **learned associations** and **experienced associations** (or just "experience"). Universal truths are a sort of "experienced association;" a CA that is interacting based on learned association might develop a similar or opposite experience. 
* Both learned and experienced associations are "reinforced" when encountered in a similar way--and sometimes you can have an opposite type of reinforcement. This provides for situations where, if 1/5 interactions with something yields a negative outcome, a CA with no experience with this thing has a 1/5 chance of not trusting someone who shares a positive outcome--until more people share it and the learned association's reinforcement is > experienced association reinforcement. (Interestingly, this means we need to have greater "value" in experienced associations, so that we can quantify the value-difference between learned and experienced associations.)
* Sharing knowledge is a founding experienced association--but one can learn not to trust others if the value of learned associations are mostly negative.
* Anything with an "unknown" outcome is avoided at all costs. For example, anything where the outcome is "death" is avoided at all costs, since the association "action:death, target:any, outcome:unknown" is a universal truth that everyone knows. 
