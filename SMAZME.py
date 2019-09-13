#!/usr/bin/env python3
import sys
import time


def sectime(a, b=3):
    """Tato funkce secte 2 argumenty

    Funkci pouzivam, kdyz chci
    secist vice argumentu

    Args:
        a: prvni cislo
        b: druhe cislo (default: {3})
    """
    return a + b


def main():

    print("Question [y/n]? ")
    time.sleep(0.5)
    print("prosel jsem")
    time.sleep(0.5)
    print("prosel jsem")
    time.sleep(0.5)
    print("prosel jsem")
    time.sleep(0.5)
    print("prosel jsem")


if __name__ == '__main__':
    main()
