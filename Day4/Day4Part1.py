class BingoCard:
    def __init__(self, name, inputValues) -> None:
        self.name = name
        self.values = [[0 for i in range(5)] for j in range(5)]
        self.valueCalled = [[False for i in range(5)] for j in range(5)]
        self.valuesCalledInRow = [0 for r in range(5)]
        self.valuesCalledInColumn = [0 for c in range(5)]

        for y in range(5):
            for x in range(5):
                self.values[y][x] = inputValues[x + (5 * y)]

        # print(input_values[2], "0,2:", self.values[0][2])

    def CheckForNumber(self, numberCalled):

        for y in range(5):
            for x in range(5):
                if self.values[y][x] == numberCalled:
                    self.valueCalled[y][x] = True
                    self.valuesCalledInRow[y] += 1
                    self.valuesCalledInColumn[x] += 1
                    if (
                        self.valuesCalledInRow[y] == 5
                        or self.valuesCalledInColumn[x] == 5
                    ):
                        return True
        return False

    def SumOfUncalledNumbers(self):

        sumValues = 0
        for y in range(5):
            for x in range(5):
                if self.valueCalled[y][x] is False:
                    sumValues += self.values[y][x]
        return sumValues


def ImportFile():
    with open("input.txt", "r") as file:
        fileLines_string = file.readlines()
    return fileLines_string


def GenerateSelectionString(input):
    string_split = input.split(",")
    output = []
    for value in string_split:
        output.append(int(value))
    return output


def GenerateBingoCards(input):

    bingo_cards = []
    value_for_bingo_card = []

    for lineCount, line in enumerate(input):
        if line == "\n":
            bingo_cards.append(BingoCard(lineCount, value_for_bingo_card))
            value_for_bingo_card.clear()
        else:
            splitLine = line.strip().split(" ")

            for value in splitLine:
                if value != "":
                    value_for_bingo_card.append(int(value))
    return bingo_cards


def DetermineOutcome(selectionArray, bingoCards):

    for selectionValue in selectionArray:
        for bingoCard in bingoCards:
            if bingoCard.CheckForNumber(selectionValue):
                if len(bingoCards) == 1:
                    print(bingoCards[0].values)
                    print(bingoCards[0].valueCalled)
                    return bingoCard.SumOfUncalledNumbers() * selectionValue
                else:
                    bingoCards.remove(bingoCard)


def main():
    input = ImportFile()
    selectionArray = GenerateSelectionString(input[0])
    bingoCards = GenerateBingoCards(input[2:])

    return DetermineOutcome(selectionArray, bingoCards)


print(main())
