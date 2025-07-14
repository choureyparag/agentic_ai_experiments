from .base_agent import Agent
from .topology_suppression_agent import TopologySuppressionAgent
from .flapping_suppression_agent import FlappingSuppressionAgent
from .planned_work_suppression_agent import PlannedWorkSuppressionAgent

class SuppressionSupervisor(Agent):
    """Supervisor that manages suppression-related worker agents."""

    def __init__(self):
        super().__init__("SuppressionSupervisor")
        self.topology = TopologySuppressionAgent()
        self.flapping = FlappingSuppressionAgent()
        self.planned_work = PlannedWorkSuppressionAgent()

    def execute(self, alarm):
        """Run suppression checks using all worker agents."""
        topology = self.topology.execute(alarm)
        flapping = self.flapping.execute(alarm)
        planned_work = self.planned_work.execute(alarm)
        return {
            "topology": topology,
            "flapping": flapping,
            "planned_work": planned_work,
        }
