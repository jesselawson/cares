# Cellular Agent Research Experiment System (CARES)

The Cellular Agent Research Experiment System (CARES) is a modular, programmable
toolset designed to study autonomous agents in a discrete, cellular environment. 

# Quickstart

1. Clone the repository: `git clone https://github.com/jesselawson/cares.git`
2. Install dependencies: `cd cares && pip install -r requirements.txt`
3. Run the example experiment: `python experiments/example1.py`
4. Study the output in the `experiments/example1` folder. You'll have a compiled gif of
all state configurations at each time step, and *.jpg copies of the state configuration 
at each time step. 

# Roadmap

**Current Status: Pre-Alpha**

CARES is almost ready for it's alpha release. Right now it is a solid 
proof-of-concept. Please check the issues for help with roadmap items, or
for bugs identified.

**"avocado"**

The "avocado" release is the first MVP release (post proof-of-concept).

* Move _all_ subroutines to new modular format
* Convert agent update logic into subroutine 

**"burrito"**

The "burrito" release is the first beta release.

* Add matplotlib to state configuration outputs
    * How can it be configured?
* Integrate sqlite (or other db) for sensory_input and association storage
* Add new sensors: 
    * AgentSensorSubroutineListen
    * AgentSubroutineListen

By the time Burrito is released, we should be forming associations between
the different sensory input data. For example, `smell01` might be associated
with `sound44` and `taste32`. 

# Documentation

The full documentation is available [here](https://jesselawson.org/cares).

# Contributing 

This project is intended to be a safe, welcoming space for collaboration, and 
contributors are expected to adhere to the 
[Contributor Covenant](http://contributor-covenant.org/) code of conduct.

1. Fork the repo.
2. Make your changes. 
3. Submit a pull request.

It's that easy!

# License

