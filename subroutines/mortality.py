# "Mortality"
# A Subroutine for the CARES Project
# Written by: Jesse Lawson
# Version: 2019.1
# TODO: Version 2: Regenerate one energy at the start of the turn (up to a maximum).

from Functions import *

def mortality(agent):
    """This subroutine will hard-stop the agent if energy <= 0."""
    if agent.energy <= 0:
        # This agent will be cleaned up by the System update function
        if not agent.system.quiet:
            log("has died (energy = %d) and will be removed from the system." % agent.energy)
        agent.alive = False
        return False
