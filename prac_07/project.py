class Project:
    """Represent a project with a name, completion %, priority, and start date."""

    def __init__(self, name, completion_percentage, priority, start_date):
        """Initialize a Project instance."""
        self.name = name
        self.completion_percentage = completion_percentage
        self.priority = priority
        self.start_date = start_date

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name} (Priority {self.priority}): {self.completion_percentage}% completed, Start date: {self.start_date}"

    def __lt__(self, other):
        """Compare projects by priority, then by start date."""
        if self.priority == other.priority:
            return self.start_date < other.start_date
        return self.priority < other.priority
