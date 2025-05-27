from stats import *

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")

    file = "books/frankenstein.txt"
    wordCount = CountWords(file)
    charDict = CountCharacters(file)
    print(f"----------- Word Count ----------\nFound {wordCount} total words")

    charList = [] 
    for entry in charDict:
        charList.append({"char":entry, "count":charDict[entry]})

    charList.sort(key=lambda dict: dict["count"], reverse=True)

    print("----------- Word Count ----------")
    for elem in charList:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["count"]}")
    print("============= END ===============")

main()