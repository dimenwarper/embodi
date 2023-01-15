# Sensors are inputs from the world that get translated into prompts for the LLM

from abc import ABC
from typing import Any
import gradio as gr


class Sensor(ABC):
    def __init__(self, name: str):
        self.name = name
    
    def input(self, widget_input: Any) -> str:
        """
        Implementation of sensory input: this will be called once each agent loop and should
        return a prompt for the LLM
        """
        raise NotImplementedError()
    
    def create_widget(self) -> Any:
        """
        Creates a widget (currently restricted to gradio components) for this sensor
        This will actually be called during the agent loop.
        """
        raise NotImplementedError()
    

class TextSensor(Sensor):
    """
    The simplest sensor: a texbox
    """    
    def __init__(self, name: str):
        super().__init__(name)
    
    def input(self, widget_input: Any) -> str:
        return widget_input
    
    def create_widget(self) -> Any:
        return gr.TextBox(label=self.name)
        

class CLIPWebCam(Sensor):
    """
    Grabs a snapshot from the webcam and runs it through CLIP to get a description, which is fed
    as a prompt to the LLM
    """
    def __init__(self, name: str):
        super().__init__(name)
    
    def input(self, widget_input: Any) -> str:
        pass
    
    def create_widget(self) -> Any:
        pass
        