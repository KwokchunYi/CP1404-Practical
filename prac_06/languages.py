from programming_language import ProgrammingLanguage

def main():
    """Create programming language objects and display information about them."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print a single ProgrammingLanguage object to check __str__ method
    print(python)

    # Create a list of programming language objects
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
