# An agent is a loop of interactivity that repeats
from __future__ import annotations
from abc import ABC
import actuators
import sensors
import llm


class Agent(ABC):
    def __init__(
        self, 
        name: str, 
        agent_llm: llm.LLM,
        actuators: list[actuators.Actuator],
        sensors: list[sensors.Sensor]
        ):
        self.name = name
        self.agent_llm = agent_llm
        self.actuators = actuators
        self.sensors = sensors
    
    def loop(self):
        raise NotImplementedError()
    
    
class SequentialAgent(Agent):
    def __init__(self, name: str, agent_llm: llm.LLM, actuators: list[actuators.Actuator], sensors: list[sensors.Sensor]):
        super().__init__(name, agent_llm, actuators, sensors)
    
    def loop(self):
        for s in self.sensors:
            self.agent_llm.push(s.input())
        output = self.elicit()
        for a in self.actuators:
            a.act(a.parse_output(output))
            