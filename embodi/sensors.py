# Sensors are inputs from the world that get translated into prompts for the LLM

from abc import ABC


class Sensor(ABC):
    def __init__(self, name: str):
        self.name = name
    
    def input(self) -> str:
        """
        Implementation of sensory input: this will be called once each agent loop and should
        return a prompt for the LLM
        """
        raise NotImplementedError()
    

class CLIPWebCam(Sensor):
    """
    Grabs a snapshot from the webcam and runs it through CLIP to get a description, which is fed
    as a prompt to the LLM
    """
    def __init__(self, name: str):
        super().__init__(name)
    
    def input(self) -> str:
        pass
        