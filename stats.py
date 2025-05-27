def CountWords(filePath):
    with open(filePath) as book:
        content = book.read()
    
    return len(content.split())

def CountCharacters(filePath):
    with open(filePath) as book:
        content = book.read()

    content = content.lower()

    charCount = {}

    for char in content:
        if not char in charCount:
            charCount[char] = 0
        
        charCount[char] += 1

    return charCount