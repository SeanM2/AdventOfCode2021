"""
--- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

"""


def ImportFile():
    file = open("Day3/input.txt")
    fileLines_string = file.readlines()

    output = []
    for line in fileLines_string:
        line = line.replace("\n", "")
        output.append(list(line))

    # print(output)
    return output


def CountFrequencyAtPosition(input):
    valueOneCount = []
    valueZeroCount = []

    while len(valueOneCount) != len(input[0]):
        valueOneCount.append(0)

    while len(valueZeroCount) != len(input[0]):
        valueZeroCount.append(0)

    for line in input:
        for i in range(len(line)):
            valueOneCount[i] += int(line[i])
            valueZeroCount[i] += (1 - int(line[i]))
            print(line[i])
            print("One: " + str(int(line[i])))
            print("Zero: " + str(1 - int(line[i])))

    return valueOneCount, valueZeroCount


def DetermineGammaEpsilon(oneCounter, zeroCounter):
    gamma = []
    epsilon = []
    for i in range(len(oneCounter)):
        gamma.append(ArbitrateResult(oneCounter[i] - zeroCounter[i]))
        epsilon.append(ArbitrateResult(zeroCounter[i] - oneCounter[i]))

    gammaOutput = ''
    epsilonOutput = ''

    gammaOutput = ''.join(gamma)
    epsilonOutput = ''.join(epsilon)

    print(int(gammaOutput, 2) * int(epsilonOutput, 2))


def ArbitrateResult(input):

    if input >= 0:
        return "1"

    return "0"


def Main():
    oneCounter, zeroCounter = CountFrequencyAtPosition(ImportFile())
    # print(oneCounter)
    # print(zeroCounter)

    DetermineGammaEpsilon(oneCounter, zeroCounter)


Main()
