import unittest
from Day4Part1 import *


class TestDay4(unittest.TestCase):
    def test_CheckSelectionStringCreation(self):
        data = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,\
            19,3,26,1"
        selectionArray = GenerateSelectionString(data)
        self.assertEqual(
            [
                7,
                4,
                9,
                5,
                11,
                17,
                23,
                2,
                0,
                14,
                21,
                24,
                10,
                16,
                13,
                6,
                15,
                25,
                12,
                22,
                18,
                20,
                8,
                19,
                3,
                26,
                1,
            ],
            selectionArray,
        )

    def test_CheckBingoCardsCreatesCorrectly(self):
        data = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        bingoCard = BingoCard(1, data)
        self.assertEqual(bingoCard.values[0][0], 22)
        self.assertEqual(bingoCard.values[4][0], 1)
        self.assertEqual(bingoCard.values[2][3], 16)

    def test_CheckBingoCardsValueCalledUpdatesCorrectly(self):
        data = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        bingoCard = BingoCard(1, data)
        bingoCard.CheckForNumber(22)
        self.assertEqual(bingoCard.valueCalled[0][0], True)
        self.assertEqual(bingoCard.valueCalled[0][1], False)

    def test_CheckBingoCardsRowCompleteDetection(self):
        data = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        bingoCard = BingoCard(1, data)
        bingoCard.CheckForNumber(22)
        bingoCard.CheckForNumber(13)
        bingoCard.CheckForNumber(17)
        bingoCard.CheckForNumber(11)
        complete = bingoCard.CheckForNumber(0)
        self.assertEqual(complete, True)

    def test_CheckBingoCardsColumnCompleteDetection(self):
        data = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        bingoCard = BingoCard(1, data)
        bingoCard.CheckForNumber(22)
        bingoCard.CheckForNumber(8)
        bingoCard.CheckForNumber(21)
        bingoCard.CheckForNumber(6)
        complete = bingoCard.CheckForNumber(1)
        self.assertEqual(complete, True)

    def test_CheckBingoCardsColumnCompleteDetection(self):
        data1 = [
            3,
            15,
            0,
            2,
            22,
            9,
            18,
            13,
            17,
            5,
            19,
            8,
            7,
            25,
            23,
            20,
            11,
            10,
            24,
            4,
            14,
            21,
            16,
            12,
            6,
        ]
        bingoCard1 = BingoCard(1, data1)
        data2 = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        bingoCard2 = BingoCard(1, data2)
        data3 = [
            14,
            21,
            17,
            24,
            4,
            10,
            16,
            15,
            9,
            19,
            18,
            8,
            23,
            26,
            20,
            22,
            11,
            13,
            6,
            5,
            2,
            0,
            12,
            3,
            7,
        ]
        bingoCard3 = BingoCard(1, data3)
        selectionData = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,\
            19,3,26,1"
        selectionArray = GenerateSelectionString(selectionData)

        output = DetermineOutcome(selectionArray, [bingoCard1, bingoCard2, bingoCard3])
        self.assertEqual(output, 1924)


if __name__ == "__main__":
    unittest.main()
