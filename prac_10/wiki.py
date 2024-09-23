import wikipedia

# Search for articles related to a search term
results = wikipedia.search("Barack")
print(results)

# Get search suggestions for a potentially mistyped query
suggestion = wikipedia.suggest("Barak Obama")
print(suggestion)

# Limit the search results by specifying the `results` parameter
limited_results = wikipedia.search("Ford", results=3)
print(limited_results)

# Obtain summaries of articles
summary = wikipedia.summary("GitHub")
print(summary)

short_summary = wikipedia.summary("Apple III", sentences=1)
print(short_summary)

# Handle Disambiguation and Page errors
try:
    mercury_summary = wikipedia.summary("Mercury")
except wikipedia.exceptions.DisambiguationError as e:
    print("DisambiguationError: The term 'Mercury' may refer to:", e.options)
except wikipedia.exceptions.PageError:
    print("PageError: The page does not exist.")

# Access full page data like title, URL, content, images, and links
ny = wikipedia.page("New York")
print(ny.title)
print(ny.url)
print(ny.content[:60])  # Print the first 60 characters of the content
print(ny.images[0])
print(ny.links[0])

# Change the language for internationalization
wikipedia.set_lang("fr")
print(wikipedia.summary("François Hollande"))

# Check for available language prefixes and print one of them
if 'en' in wikipedia.languages():
    print("English is available.")
print("Spanish language prefix:", wikipedia.languages()['es'])

# Prompt for donations to the Wikimedia project
# This will open a web browser; commented out to avoid running unintentionally
# wikipedia.donate()

# Remember to handle exceptions and errors as appropriate in your script.
