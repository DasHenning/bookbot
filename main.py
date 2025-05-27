from stats import *

def main():
    wordCount = CountWords("books/frankenstein.txt")
    print(f"{wordCount} words found in the document")

    print(CountCharacters("books/frankenstein.txt"))

main()