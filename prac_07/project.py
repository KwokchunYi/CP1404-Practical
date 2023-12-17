import datetime


class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.start_date_str = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date_str}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def compare_date_with_input_date(self, start_after_date):
        input_date = datetime.datetime.strptime(start_after_date, "%d/%m/%Y").date()
        return self.start_date >= input_date