# apps/backend/core/orchestrator.py

class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run_task(self, task):
        spec = task.to_spec()
        print(f"[Orchestrator] Running task: {task.name}")
        for agent in self.agents:
            agent.execute(spec)

