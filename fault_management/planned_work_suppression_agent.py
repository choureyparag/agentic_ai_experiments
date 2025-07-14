from .base_agent import Agent

class PlannedWorkSuppressionAgent(Agent):
    """Agent to suppress alarms during planned maintenance windows."""

    def __init__(self):
        super().__init__("PlannedWorkSuppression")

    def execute(self, alarm):
        """Check if the alarm coincides with planned work periods.

        This placeholder implementation will later query a maintenance
        calendar once the data integration layer is implemented.
        """
        # TODO: Replace with actual maintenance window check
        return {
            "alarm": alarm,
            "suppressed": False,
        }
