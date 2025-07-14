"""Top level orchestrator agent for fault management."""

try:
    from langgraph import Graph
except Exception:  # pragma: no cover - langgraph may not be installed
    Graph = None  # type: ignore

from .base_agent import Agent
from .alarm_monitoring_supervisor import AlarmMonitoringSupervisor
from .suppression_supervisor import SuppressionSupervisor

class OrchestratorAgent(Agent):
    """Supervises all supervisors and orchestrates the entire workflow."""

    def __init__(self):
        super().__init__("Orchestrator")
        self.alarm_supervisor = AlarmMonitoringSupervisor()
        self.suppression_supervisor = SuppressionSupervisor()
        self.graph = self._build_graph()

    def _build_graph(self):
        """Construct a LangGraph representing agent interactions."""
        if Graph is None:
            return None
        graph = Graph()
        # Placeholder graph construction
        # TODO: define actual graph edges and nodes when details are available
        return graph

    def execute(self, alarm):
        """Run the full fault management pipeline for a single alarm."""
        monitoring = self.alarm_supervisor.execute(alarm)
        suppression = self.suppression_supervisor.execute(alarm)
        return {
            "monitoring": monitoring,
            "suppression": suppression,
        }
