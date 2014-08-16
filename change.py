#!/usr/bin/env python

# http://en.wikipedia.org/wiki/Shebang_(Unix)

"""
    This program calculates change through the make_change function

"""

import sys

def make_change(amount_chg):
    # input amount of change to make_change
    # return the minimun number of coin to make change
    # coins will be quarter, dimes, nickles, and pennies

    # check for 0 cents left, so as to stop computation
    # handle negative value amounts

    QUARTERS = 25
    DIMES = 10
    NICKLES = 5
    PENNIES = 1

    changelist = [QUARTERS,DIMES,NICKLES,PENNIES]
    coinlist = []

    for coin in changelist:
        res = process_change(amount_chg, coin)
        amount_chg = res[1]
        coinlist.append(res)

    return coinlist

def process_change(balance, denom):
    number_denom = balance/denom
    balance = balance % denom
    return (number_denom, balance)

if __name__=='__main__':
    prog_args = sys.argv

    list1 = make_change(int(prog_args[1]))
    returninfo = []
    for element in list1:
        returninfo.append(element[0])
    print "{} Quarters, {} Dimes, {} Nickels, {} Pennies".format(*returninfo)
