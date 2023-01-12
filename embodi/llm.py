# API for connecting to an LLM and some prompting utilities utilities

class LLM:
    def __init__(self, name: str, init_prompt: str):
        self.name = name
        self.init_prompt = ""
    
    def boot_llm(self, init_prompt: str):
        pass
    
    def generate(self, prompt: str) -> str:
        return "ph"