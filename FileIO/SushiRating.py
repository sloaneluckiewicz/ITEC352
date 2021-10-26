#!/usr/bin/env python3
# AUTHOR: Sloane Luckiewicz
# File I/0 Sushi Roll & Rating Assignment

import csv
FILENAME = "sushi1.csv"
FILENAME2 = "sushi_new.csv"

def write_sushi(sushi):
    with open(FILENAME2, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sushi)

def read_sushi():
    sushi= []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sushi.append(row)
    return sushi


def display_sushi(sushi):
    for i in range(len(sushi)):
        sush = sushi[i]
        print(str(i+1) + ". " + str(sush[0]) + ": " + str(sush[1]) + " | " + str(sush[2]) + " | " + str(sush[3]) + " | " + str(sush[4]) + " | " + str(sush[5]))
    print()


def main():
    sushi = read_sushi()
    display_sushi(sushi)
    write_sushi(sushi)
    print("BYE!")



if __name__ == "__main__":
    main()
