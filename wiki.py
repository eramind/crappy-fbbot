import wikipedia

def searchWiki(term):
    result = wikipedia.summary(term, sentences=2)
    url = wikipedia.page(term).url
    return result + "\n\nFor full article click here: " + url
    
    