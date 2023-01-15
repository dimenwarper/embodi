# Actuators convert generated text into actions for the LLM to control
from __future__ import annotations
from abc import ABC
import gradio as gr


class Actuator(ABC):
    def __init__(self, name: str, init_prompt: str):
        self.init_prompt = init_prompt
        self.name = name
    
    def act(self, text: str):
        """
        Implementation of actuator logic: the name of the actuator will be parsed from
        the LLM output. This method should then do something with that text 
        """
        raise NotImplementedError()
    
    def create_widget(self) -> Any:
        """
        Creates a widget (currently restricted to gradio components) for this actuator 
        This will actually be called during the agent loop.
        """
        raise NotImplementedError()


class TextActuator(Actuator):
    """
    The simplest actuator: a texbox with output
    """    
    def __init__(self, name: str):
        super().__init__(name)
    
    def act(self, text) -> str:
        return text
    
    def create_widget(self) -> Any:
        return gr.TextBox(label=self.name) 

    
class PictureWindow(Actuator):
    def __init__(
        self, 
        name: str,
        picture_dict: dict[str, str],
        description: str
        ):
        init_prompt = f"{' | '.join(picture_dict.keys())}: depending on {description}"
        super().__init__(name, init_prompt)
        # Dictionary of cues and picture paths
        self.picture_dict = picture_dict
        self.description = description
    
    def act(self, text: str):
        """
        This actuator opens up a qtk window and shows a picture depending on a cue outputted by the LLM.
        The cue given bye the LLM might not be perfect so we compute the minimum distance in some sense
        to our limited set of cues
        """
        pass

    def create_widget(self) -> Any:
        pass