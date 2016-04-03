#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from lib import lscolors as c
from lib import cli
from lib import URL
from lib import lsprint
from lib import lsweb
from lib import lsnews

import time


def main():
    bTable = bool(cli.args.table)
    bScore = bool(cli.args.score)
    bScorers = bool(cli.args.scorers)
    bNews = bool(cli.args.news)

    if not bTable and not bScore and not bScorers and not bNews:
        bScore = True

    while True:
        try:
            os.system('clear')
            for k in cli.args.League:
                # Code to fetch data from URL[k]
                pingTest = 'www.livescore.com'
                print(' ... Fetching scores from '+pingTest+' ... ')
                if lsweb.is_connected(pingTest) is True:

                    if bTable:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
                        lsprint.table(lsweb.get_table(URL.URL[k][1]), k)

                    if bNews:
                        lsnews.print_news(lsnews.get_news())

                    if bScore:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        lsprint.scores(lsweb.get_score(URL.URL[k][1]), k)

                    if bScorers:
                        print("Displaying Top Scorers for"
                              " {}".format(URL.URL[k][0]))
                        print('Working on it')

                else:
                    print(c.RED+"Check Your Internet Connection ,"
                          " It looks like you're out of internet."+c.END)

                time.sleep(3)

            bTable = False
            bScorers = False
            bNews = False
            if not bool(bScore):
                break
            time.sleep(25)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
