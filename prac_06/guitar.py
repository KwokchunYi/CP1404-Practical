class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2022  # We are using 2022 as the current year here. In a live system, you would pull the current year dynamically.
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50