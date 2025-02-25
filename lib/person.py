class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name="Unknown", job="Unknown"):
        self.name = name  # Use property to set name
        self.job = job    # Use property to set job

    # Name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Assign None if invalid

    # Job property with validation
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = None  # Assign None if invalid
