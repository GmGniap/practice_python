import re

def classify_regex(text):
    ## women
    results = []
    women = re.search("^*[Ww]om[ea]n", text)
    rural = re.search("^[Rr]ural", text)
    if women:
        results.append("woman")
    elif rural:
        results.append("rural")
    else:
        return "unknown"
    return results
        