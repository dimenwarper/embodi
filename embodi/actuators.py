# Actuators convert generated text into actions for the LLM to control
from __future__ import annotations
from abc import ABC


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