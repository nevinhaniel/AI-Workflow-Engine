class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, fn):
        self.tools[name] = fn

    def get(self, name):
        return self.tools.get(name)


tool_registry = ToolRegistry()

def detect_smells(code):
    return {"issues": 3}

tool_registry.register("detect_smells", detect_smells)
