"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, "
                f"First appeared in {self.year}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}")


    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    # Updated to include the pointer_arithmetic attribute
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    c_language = ProgrammingLanguage("C", "Static", False, 1972, True)
    cpp_language = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, visual_basic, c_language, cpp_language]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
