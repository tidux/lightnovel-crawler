#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interactive value input"""
from .app import start_app
from .lnmtl import LNMTLCrawler
from .webnovel import WebnovelCrawler
from .wuxiacom import WuxiaComCrawler
from .wuxiaco import WuxiaCoCrawler
from .wuxiaonline import WuxiaOnlineCrawler
from .boxnovel import BoxNovelCrawler
from .readln import ReadLightNovelCrawler
from .novelplanet import NovelPlanetCrawler
from .lnindo import LnindoCrawler
from .idqidian import IdqidianCrawler
from .utils.crawler import Crawler
from .tests.crawler_app_test import run_tests

crawler_list = {
    'https://lnmtl.com/': LNMTLCrawler,
    'https://www.webnovel.com/': WebnovelCrawler,
    'https://wuxiaworld.online/': WuxiaOnlineCrawler,
    'https://www.wuxiaworld.com/': WuxiaComCrawler,
    'https://m.wuxiaworld.com/': WuxiaComCrawler,
    'https://www.wuxiaworld.co/': WuxiaCoCrawler,
    'https://m.wuxiaworld.co/': WuxiaCoCrawler,
    'https://boxnovel.com/': BoxNovelCrawler,
    'https://novelplanet.com/': NovelPlanetCrawler,
    'https://www.readlightnovel.org/': ReadLightNovelCrawler,
    'https://lnindo.org/': LnindoCrawler,
    'https://www.idqidian.us/': IdqidianCrawler,
}


def main():
    start_app(crawler_list)
# end def


if __name__ == '__main__':
    main()
# end if
