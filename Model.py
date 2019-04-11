
from subroutines.move_randomly import *
from subroutines.evaluate_goals import *
from subroutines.mortality import *
from subroutines.process_sensor_eyesight import *

class Model:
    """A model is a collection of subroutines."""
    def __init__(self, name):
        self.name = name
        self.subroutines = []

    def add_subroutine(self, subroutine):
        """Add an array of subroutines to this model."""
        self.subroutines.append(subroutine)

    def get_subroutines(self):
        return self.subroutines


# The order in which subroutines are added matters. These are FIFO!
MODEL_ALPHA1 = Model('alpha1')
MODEL_ALPHA1.add_subroutine(mortality)
MODEL_ALPHA1.add_subroutine(process_sensor_eyesight)
MODEL_ALPHA1.add_subroutine(evaluate_goals)
MODEL_ALPHA1.add_subroutine(move_randomly)


NEWEST_MODEL = MODEL_ALPHA1