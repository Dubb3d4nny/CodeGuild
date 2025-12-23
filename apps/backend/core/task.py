# apps/backend/core/task.py

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_spec(self):
        from .spec import Spec
        return Spec(self.name, self.description)

