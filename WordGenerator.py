import csv
import random as r


class Word:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint


def getWord():
    with open("words.csv", "r") as readFile:
        csvReader = csv.reader(readFile)
        wordList = []
        for line in csvReader:
            wordList.append(Word(line[0], line[1]))

        return wordList[r.randint(0, len(wordList) - 1)]
