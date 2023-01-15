# An agent is a loop of interactivity that repeats
from __future__ import annotations
from abc import ABC
import actuators
import sensors
import llm
import gradio as gr


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
    
    def loop_fn(self, *widget_inputs):
        for i, wi in enumerate(widget_inputs):
            s = self.sensors[i]
            self.agent_llm.push(s.input(wi))
        output = self.agent_llm.call()
        return (a.act(a.parse_output(output)) for a in self.actuators)
    
    def run(self):
        with gr.Blocks() as app:
            sensor_widgets = [s.create_widget() for s in self.sensors]
            actuator_widgets = [a.create_widget() for a in self.actuators]
            done_button = gr.Button("Go")
            done_button.click(fn=self.loop_fn, inputs=sensor_widgets, outputs=actuator_widgets)

        app.launch()            