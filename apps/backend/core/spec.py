# apps/backend/core/spec.py

class Spec:
    def __init__(self, name, description, files=None, constraints=None):
        self.name = name
        self.description = description
        self.files = files or []
        self.constraints = constraints or []

