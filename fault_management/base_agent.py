class Agent:
    """Base class for all agents in the fault management system."""

    def __init__(self, name: str):
        self.name = name

    def execute(self, data):
        """Placeholder execution method to be overridden by subclasses."""
        raise NotImplementedError("Agent subclasses must implement execute method")
