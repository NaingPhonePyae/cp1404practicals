"""
Program store project
Expected time: 1 hour
Actual time:
"""


class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string in desired format"""
        return (f"  {self.name}, start: {self.date}, priority {self.priority}, estimate: ${float(self.cost):,.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Determine if the project is more prioritized"""
        return self.priority < other.priority

    def is_completed(self):
        """Determine if a project is completed"""
        return self.completion == 100
