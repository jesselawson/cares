# Cellular Automata Research in Emergent Sentience (SCARE)

Theory: 

* Human evolution is based on the sharing of knowledge.
* If knowledge were quantized, each "unit" of knowledge would be an association between 
one or more other "units" of knowledge.
* The more knowledge you share, the more you evolve

"Ethnographically, this diversity ['of social organizations, group sizes, kinship 
structures, and mating patterns'] is at least partially rooted in culturally-acquired and 
widely shared social rules" (Henrich, 2011).

This sharing of experiences has led to the development of social groups and culture, and 
natural selection favored genes that resulted in more pro-social behavior, which in turn 
resulted in generation after generation of offspring with "sociogenetically superior" 
traits.

> Over the last million years or so, people evolved the ability to learn from each other, 
creating the possibility of cumulative, cultural evolution. Rapid cultural adaptation 
also leads to persistent differences between local social groups, and then competition 
between groups leads to the spread of behaviours that enhance their competitive ability. 
Then, in such culturally evolved cooperative social environments, natural selection 
within groups favoured genes that gave rise to new, more pro-social motives. Moral 
systems enforced by systems of sanctions and rewards increased the reproductive 
success of individuals who functioned well in such environments, and this in turn led to 
the evolution of other regarding motives like empathy and social emotions like shame. 
(Boyd & Richerson, 2009)

Knowledge is unique to us and our social environment. 
https://quod.lib.umich.edu/j/jep/3336451.0009.201?view=text;rgn=main

# Describing the Universe

Imagine a discrete grid populated by autonomous agents. This discrete grid is a 
universe that has the following entities in it:

1. Plants. When a plant is consumed, it can give energy (type = edible) or take energy 
(type = poison).
2. One CA per grid; grids can be occupied by both a CA and a plant.
4. It takes one unit of energy to perform any one action.
5. An action is either {move, share_knowledge, learn, reproduce, build_nest}

Thought:
* A thought can be shared by CAs
* A thought has a category {food, shelter, reproduction, 

Computed Individual characteristics:
* Social Value. If this CA has not learned a lot from other CAs, it will be less likely 
to care about other CAs. 

### Scenarios/Research Questions
**Poisoned Plants**. If we have some plants that are poison, how would we communicate to 
other CAs not to eat them? 
* Proximity to poison plant consumption. If $C_1$ "witnesses" $C_2$ eating a poison 
plant and then dying, it will "associate" action:eat, target:plant_type, outcome:death.

**Scarcity.** How does scarcity among different environmental variables affect CAs?
* Scarcity of suitable mates
* Scarcity of food
* Scarcity of shelter materials

### Universal truths
Some universal truths are pre-programmed into each CA at the start of the universe. These 
are biological imperatives--drives that exist on an instinctual level. 
* Every action requires one unit of food.
* There are **learned associations** and **experienced associations** (or just 
"experience"). Universal truths are a sort of "experienced association;" a CA that is 
interacting based on learned association might develop a similar or opposite experience. 
* Both learned and experienced associations are "reinforced" when encountered in a 
similar way--and sometimes you can have an opposite type of reinforcement. This provides 
for situations where, if 1/5 interactions with something yields a negative outcome, a CA 
with no experience with this thing has a 1/5 chance of not trusting someone who shares a 
positive outcome--until more people share it and the learned association's reinforcement 
is > experienced association reinforcement. (Interestingly, this means we need to have 
greater "value" in experienced associations, so that we can quantify the value-difference 
between learned and experienced associations.)
* Sharing knowledge is a founding experienced association--but one can learn not to trust 
others if the value of learned associations are mostly negative.
* Anything with an "unknown" outcome is avoided at all costs. For example, anything where 
the outcome is "death" is avoided at all costs, since the association "action:death, target:any, outcome:unknown" is a universal truth that everyone knows. 



## Comparison to Other Systems

**TerraJS**
* http://rileyjshaw.com/terra/
* TerraJS does not account for social sharing of knowledge; each entity operates in its 
own discrete and unshared set of experiences.


# The Entity

An entity is something that can be alive and can be dead. 

## The Cellular Automaton

A CA is an entity that is comprised of three primary elements:

1. One or more **Genetic Characteristics**, which are combined with mates and passed on 
to offspring (and thus, certain genetic characteristics are passed on--or not);
2. A **Cerebrum**, which is the "brain" of the CA and where all input from
sensors are gathered and decisions are made.
3. 

The Cortex has two components:

1. **Learned Associations**, which are low-priority units of knowledge about the
world;
3. **Experienced Associations**, which are high-priority units of knowledge
about the world.  


# Development 

## Experiment Organization

Each set of environmental conditions (the state variables of the System), combined with
instructions for Agent replication (i.e., which model we will use), is organized in an
experiment folder. 

For example, in Experiment 1 

## Subroutines

The bare essence of a subroutine is a function that takes in the entire Agent object,
performs some logical computations, and then modifies some element(s) of the Agent. 

For example, we know that Agents record all observations as a dynamically columned
database. If we decide to add some environmental feature in the future, we could create
a subroutine that checks whether there are observations of that environmental feature
existing in this particular agent's observations.json file (a tinyDB db file). If 
there does exist records, then we know this agent version is designed to interact with
those environmental features. If there are no results returned, then this agent has not
observed those environmental features--or it is not designed to--and this subroutine
is just skipped.

A Subroutine is a class object that has its own dynamic set of variables, including 
it's own training_data array for whatever this subroutine is designed to do. 

What type of training_data the subroutine stores and trains, including how it trains its


Each Agent can have one of many "subroutines", and new experiments can mix and match
different subroutines together.

Subroutines are stored in the **System Subroutine Library**. 

Groups of subroutines, called a **Subroutine Collection**, are created upon system instantiation. 



Subroutine Collections are added to the agent objects during instantiation:

```
mark_i = SubroutineCollection()

def 
...
system.add_agent(...)
-- Includes the subroutines
```

New subroutines should be registered with the System object, since it is the System that
spawns the Agents. 

**Q: How do we create agents with different subroutine groups?**

The system has to be able to create a **collection of subroutines** and then apply that
collection of subroutines to a particular agent that it is creating. 

If we have `System.`

When each agent is making a decision, it process through its subroutines.

The subroutines can work together OR they can just modify values blindly. 



# References

Boyd, R. & Richerson, P. J. (2009). Culture and the evolution of human cooperation. 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2781880/

Henrich, J. (2011). A cultural species: How culture drove human evolution. 
https://www.apa.org/science/about/psa/2011/11/human-evolution)
