# Cellular Agent Research Experiment System (CARES)

Theory: 

* Human evolution is based on the sharing of knowledge.
* If knowledge were quantized, each "unit" of knowledge would be an association between one or more other "units" of knowledge.
* The more knowledge you share, the more you evolve



"Ethnographically, this diversity ['of social organizations, group sizes, kinship structures, and mating patterns'] is at least partially rooted in culturally-acquired and widely shared social rules" (Henrich, 2011).

This sharing of experiences has led to the development of social groups and culture, and natural selection favored genes that resulted in more pro-social behavior, which in turn resulted in generation after generation of offspring with "sociogenetically superior" traits.

> Over the last million years or so, people evolved the ability to learn from each other, creating the possibility of cumulative, cultural evolution. Rapid cultural adaptation also leads to persistent differences between local social groups, and then competition between groups leads to the spread of behaviours that enhance their competitive ability. Then, in such culturally evolved cooperative social environments, natural selection within groups favoured genes that gave rise to new, more pro-social motives. Moral systems enforced by systems of sanctions and rewards increased the reproductive success of individuals who functioned well in such environments, and this in turn led to the evolution of other regarding motives like empathy and social emotions like shame. (Boyd & Richerson, 2009)

Knowledge is unique to us and our social environment. https://quod.lib.umich.edu/j/jep/3336451.0009.201?view=text;rgn=main

# Describing the Universe

Imagine a discrete grid populated by autonomous agents. This discrete grid is a 
universe that has the following entities in it:

1. Plants. When a plant is consumed, it can give energy (type = edible) or take energy (type = poison).
2. One CA per grid; grids can be occupied by both a CA and a plant.
4. It takes one unit of energy to perform any one action.
5. An action is either {move, share_knowledge, learn, reproduce, build_nest}

Thought:
* A thought can be shared by CAs
* A thought has a category {food, shelter, reproduction, 

Computed Individual characteristics:
* Social Value. If this CA has not learned a lot from other CAs, it will be less likely to care about other CAs. 

### Scenarios/Research Questions
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



## Comparison to Other Systems

**TerraJS**
* http://rileyjshaw.com/terra/
* TerraJS does not account for social sharing of knowledge; each entity operates in its own discrete and unshared set of experiences.


# The Entity

An entity is something that can be alive and can be dead. 

## The Cellular Automaton

A CA is an entity that is comprised of three primary elements:

1. One or more **Genetic Characteristics**, which are combined with mates and passed on to 
offspring (and thus, certain genetic characteristics are passed on--or not);
2. A **Cerebrum**, which is the "brain" of the CA and where all input from
sensors are gathered and decisions are made.
3. 

The Cortex has two components:

1. **Learned Associations**, which are low-priority units of knowledge about the
world;
3. **Experienced Associations**, which are high-priority units of knowledge
about the world.  


# Development 

Each Agent can have one of many "subroutines", and new experiments can mix and match
different subroutines together. 

Subroutines are added to the agent objects during instantiation:

```
system.subroutines.append(new_subroutine)
...
system.add_agent(...)
-- Includes the subroutines
```

When each agent is making a decision, it process through its subroutines.

The subroutines can work together OR they can just modify values blindly. 



# References

Boyd, R. & Richerson, P. J. (2009). Culture and the evolution of human cooperation. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2781880/

Henrich, J. (2011). A cultural species: How culture drove human evolution. https://www.apa.org/science/about/psa/2011/11/human-evolution)
