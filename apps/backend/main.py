# apps/backend/main.py

from core.task import Task
from core.orchestrator import Orchestrator
from agents.planner import PlannerAgent
from agents.builder import BuilderAgent
from agents.validator import ValidatorAgent

def main():
    # Example task
    task = Task("Initial Setup", "Create scaffolding for backend v0.1")
    
    # Agents
    agents = [PlannerAgent(), BuilderAgent(), ValidatorAgent()]
    
    # Orchestrator
    orchestrator = Orchestrator(agents)
    
    # Run task
    orchestrator.run_task(task)

if __name__ == "__main__":
    main()

