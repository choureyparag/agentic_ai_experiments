from .base_agent import Agent
from .alarm_classification_agent import AlarmClassificationAgent
from .alarm_insight_agent import AlarmInsightAgent

class AlarmMonitoringSupervisor(Agent):
    """Supervisor that distributes alarm monitoring tasks to worker agents."""

    def __init__(self):
        super().__init__("AlarmMonitoringSupervisor")
        self.classifier = AlarmClassificationAgent()
        self.insight = AlarmInsightAgent()

    def execute(self, alarm):
        """Process an alarm using the worker agents."""
        classification = self.classifier.execute(alarm)
        insight = self.insight.execute(alarm)
        return {
            "classification": classification,
            "insight": insight,
        }
