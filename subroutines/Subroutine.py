
#  Cellular Agent Research Experiment System (CARES)
#  Copyright (c) 2019 Jesse Lawson
#
#  Web: https://jesselawson.org
#  Email: jesselawson@protonmail.com
#  Telegram: t.me/jesselawson
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod


class Subroutine(ABC):
    """A subroutine is an abstract class designed to give subroutine developers
    as much freedom as possible to configure Agent and System logic."""
    def __init__(self, the_type):
        self.type = the_type # should be either agent or system
        super().__init__()

    @abstractmethod
    def hookup(self, agent_or_system):
        pass

    @abstractmethod
    def process(self, agent_or_system):
        pass


class AgentSubroutine(Subroutine):
    """A subroutine for an Agent."""
    def __init__(self, the_id):
        super().__init__('agent')
        self.agent = None

    def hookup(self, the_agent):
        self.agent = the_agent
        if self.agent:
            return True
        else:
            return False

    @abstractmethod
    def process(self, agent):
        pass


class SystemSubroutine(Subroutine):
    """A subroutine for a System."""
    def __init__(self):
        super().__init__('system')
        self.system = None

    def hookup(self, the_system):
        self.system = the_system
        if self.system:
            return True
        else:
            return False

    @abstractmethod
    def process(self, system):
        pass

