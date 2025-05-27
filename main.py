from stats import *
import sys

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    
    file = sys.argv[1]

    wordCount = CountWords(file)
    charDict = CountCharacters(file)

    print(f"----------- Word Count ----------\nFound {wordCount} total words")

    charList = [] 
    for entry in charDict:
        charList.append({"char":entry, "count":charDict[entry]})

    charList.sort(key=lambda dict: dict["count"], reverse=True)

    print("----------- Character Count ----------")
    for elem in charList:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["count"]}")
    print("============= END ===============")

main()