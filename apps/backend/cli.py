# apps/backend/cli.py

import sys

from core.task import Task
from core.orchestrator import Orchestrator
from agents.planner import PlannerAgent
from agents.builder import BuilderAgent
from agents.validator import ValidatorAgent


def print_help():
    print("""
CodeGuild CLI v0.1.1

Usage:
  python cli.py run "<task description>"

Example:
  python cli.py run "Build authentication system"
""")


def run_task(task_description: str):
    # Create task
    task = Task(
        name="CLI Task",
        description=task_description
    )

    # Create agents
    agents = [
        PlannerAgent(),
        BuilderAgent(),
        ValidatorAgent()
    ]

    # Run orchestrator
    orchestrator = Orchestrator(agents)
    orchestrator.run_task(task)


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "run":
        if len(sys.argv) < 3:
            print("❌ Error: Task description is required.")
            print_help()
            return

        task_description = " ".join(sys.argv[2:])
        run_task(task_description)

    else:
        print(f"❌ Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()
