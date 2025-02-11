#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crawler for [boxnovel.com](https://boxnovel.com/).
"""
import json
import logging
import re
from ..utils.crawler import Crawler

logger = logging.getLogger('KISS-NOVEL')
#search_url = 'https://boxnovel.com/?s=%s&post_type=wp-manga&author=&artist=&release='



class KissNovelCrawler(Crawler):
    #def search_novel(self, query):
    #    query = query.lower().replace(' ', '+')
    #    soup = self.get_soup(search_url % query)

    #    results = []
    #    for tab in soup.select('.c-tabs-item__content'):
    #        a = tab.select_one('.post-title h4 a')
    #        latest = tab.select_one('.latest-chap .chapter a').text
    #        votes = tab.select_one('.rating .total_votes').text
    #        results.append({
    #            'title': a.text.strip(),
    #            'url': self.absolute_url(a['href']),
    #            'info': '%s | Rating: %s' % (latest, votes),
    #        })
        # end for

    #    return results
    # end def

    def read_novel_info(self):
        '''Get novel title, autor, cover etc'''
        logger.debug('Visiting %s', self.novel_url)
        soup = self.get_soup(self.novel_url)

        self.novel_title = ' '.join([
            str(x)
            for x in soup.select_one('.post-title h1').contents
            if not x.name
        ]).strip()
        logger.info('Novel title: %s', self.novel_title)

        self.novel_cover = self.absolute_url(
            soup.select_one('.summary_image img')['src'])
        logger.info('Novel cover: %s', self.novel_cover)

        author = soup.find('div', {'class': 'author-content'}).findAll('a')
        if len(author) == 2:
            self.novel_author = author[0].text + ' (' + author[1].text + ')'
        else:
            self.novel_author = author[0].text
        logger.info('Novel author: %s', self.novel_author)

        latest_chapter = soup.select('div.post-content_item ul li a')[0].text
        chapter_count = [int(i) for i in latest_chapter.split() if i.isdigit()]
        page_count = (chapter_count)[0]//10+1
        chapters_page_url = '%s/%s#chapter-section'

        chapters = []

        for i in range(page_count):
            url = chapters_page_url % (self.novel_url,str(i+1))
            logger.debug('Visiting %s', url)
            soup = self.get_soup(url)
            chapters.extend(soup.select('ul.main li.wp-manga-chapter a'))
        # end for
        chapters.reverse()

        for a in chapters:
            chap_id = len(self.chapters) + 1
            vol_id = chap_id//100 + 1
            if len(self.chapters) % 100 == 0:
                vol_title = 'Volume ' + str(vol_id)
                self.volumes.append({
                    'id': vol_id,
                    'title': vol_title,
                })
            # end if
            self.chapters.append({
                'id': chap_id,
                'volume': vol_id,
                'url':  self.absolute_url(a['href']),
                'title': a.text.strip() or ('Chapter %d' % chap_id),
            })
        # end for

        logger.debug(self.chapters)
        logger.debug('%d chapters found', len(self.chapters))
    # end def

    def download_chapter_body(self, chapter):
        '''Download body of a single chapter and return as clean html format.'''
        logger.info('Downloading %s', chapter['url'])
        soup = self.get_soup(chapter['url'])

        contents = soup.select('div.reading-content p')

        body = [str(p) for p in contents if p.text.strip()]
        return '<p>' + '</p><p>'.join(body) + '</p>'

        #if contents.h3:
        #    contents.h3.decompose()

        #for codeblock in contents.findAll('div', {'class': 'code-block'}):
        #    codeblock.decompose()

        #return contents.prettify()
    # end def
# end class
