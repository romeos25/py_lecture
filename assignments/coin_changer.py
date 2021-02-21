#!/usr/bin/env python3

from argparse import ArgumentParser
import sys

def loop(amt, total_coin):
    coin_list = [10, 5, 2, 1]
    remains = amt

    for num in coin_list:
        if remains % num == 0:
            total_coin += remains//num
            break
        else:
            total_coin += remains//num
            remains = remains%num
            continue
    print('input: ', amt)
    print(total_coin)

def main():
    parser = ArgumentParser(description='Coin Change')
    parser.add_argument('--amount', help='change amount', dest='AMT')
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit()
    
    amt = int(args.AMT)

    if amt < 0:
        print('Amount cannot be negative')
        sys.exit()

    if amt == 0:
        print('Here\'s your change => ', amt)
        sys.exit()

    total_coin = 0
    loop(amt, total_coin)

if __name__ == '__main__':
    main()
