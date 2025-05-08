#
# @brief: collect the data from journal
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
import requests, random, time, re
from datetime import datetime, timedelta

# ========================================================================= #
#
# @brief: paper information
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class paper_information:
    def __init__(self, id: int = 0, journal: str = None, title: str = None, author: str = None,
                 date: str = None, link: str = None, abstract: str = None):
        self.journal = journal
        self.title = title
        self.author = author
        self.pubdate = date
        self.link = link
        self.abstract = abstract
        self.target = False
        self.aisum = ''

    
# ========================================================================= #
#
# @brief: the header of the request
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

# ========================================================================= #
#
# @brief: query data according to the label in html
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def find_data(html: str, label: str) -> list:
    pattern = r'<' + label + r'[^>]*>(.*?)</' + label + r'>'
    return re.findall(pattern, html, re.DOTALL)

def search_data(html: str, label: str) -> str:
    pattern = r'<' + label + r'>(.*?)</' + label + r'>'
    return re.search(pattern, html, re.DOTALL).group(1) if re.search(pattern, html, re.DOTALL) else None 

# ========================================================================= #
#
# @brief: convert the time to beijing time
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def beijing_time(time: str, format: str):
    beijing = datetime.strptime(time, format) + timedelta(hours=8)
    return beijing.strftime("%Y-%m-%d")


# ========================================================================= #
#
# @brief: Geophysical Research Letters
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class GRL:
    def __init__(self):
        url = "https://agupubs.onlinelibrary.wiley.com/feed/19448007/most-recent"
        time.sleep(random.uniform(1, 5))
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'pubDate'), "%a, %d %b %Y %H:%M:%S %z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'dc:description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Geophysical Research Letters', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Journal of Geophysical Research: Space Physics
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class JGR_SPHY:
    def __init__(self):
        url = "https://agupubs.onlinelibrary.wiley.com/feed/21699402/most-recent"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'pubDate'), "%a, %d %b %Y %H:%M:%S %z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'dc:description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Journal of Geophysical Research: Space Physics', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: AGU Space Weather
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class AGU_SW:
    def __init__(self):
        url = "https://agupubs.onlinelibrary.wiley.com/feed/15427390/most-recent"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'pubDate'), "%a, %d %b %Y %H:%M:%S %z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'dc:description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Space Weather', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: AGU Advance
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class AGU_AD:
    def __init__(self):
        url = "https://agupubs.onlinelibrary.wiley.com/feed/2576604x/most-recent"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'pubDate'), "%a, %d %b %Y %H:%M:%S %z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'dc:description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='AGU Advances', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Physical Review Letters 
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class PRL:
    def __init__(self):
        url = "https://feeds.aps.org/rss/recent/prl.xml"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'prism:publicationDate'), "%Y-%m-%dT%H:%M:%S%z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Physical Review Letters', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Physical Review E
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class PRE:
    def __init__(self):
        url = "https://feeds.aps.org/rss/recent/pre.xml"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        pubdate = beijing_time(search_data(item, 'prism:publicationDate'), "%Y-%m-%dT%H:%M:%S%z")
        link = search_data(item, 'link')
        abstract = search_data(item, 'description')
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Physical Review E', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Nature
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Nature:
    def __init__(self):
        url = "https://www.nature.com/nature.rss"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    @staticmethod
    def parse_title(item: str):
        pattern = r'<title><!\[CDATA\[(.*?)\]\]></title>'
        return re.search(pattern, item, re.DOTALL).group(1) if re.search(pattern, item, re.DOTALL) else None 

    @staticmethod
    def parse_abstract(item: str):
        pattern = r'<content:encoded>\s*<!\[CDATA\[(.*?)\]\]></content:encoded>'
        return re.search(pattern, item, re.DOTALL).group(1) if re.search(pattern, item, re.DOTALL) else None 


    def __item(self, item: str):
        title = self.parse_title(item)
        if title is None or title == "Issue Information":
            return None
        pubdate = search_data(item, 'dc:date')
        link = search_data(item, 'link')
        abstract = self.parse_abstract(item)
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        authors = find_data(item, 'dc:creator')
        author = ''
        for au in authors:
            if author == '':
                author = au
            else:
                author = author + ', ' + au
        return paper_information(journal='Nature', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Nature Communications
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Nature_Comm:
    def __init__(self):
        url = "https://www.nature.com/ncomms.rss"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = Nature.parse_title(item)
        if title is None or title == "Issue Information":
            return None
        pubdate = search_data(item, 'dc:date')
        link = search_data(item, 'link')
        abstract = Nature.parse_abstract(item)
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        authors = find_data(item, 'dc:creator')
        author = ''
        for au in authors:
            if author == '':
                author = au
            else:
                author = author + ', ' + au
        return paper_information(journal='Nature Communications', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Nature Physics
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Nature_Phys:
    def __init__(self):
        url = "https://www.nature.com/nphys.rss"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = Nature.parse_title(item)
        if title is None or title == "Issue Information":
            return None
        pubdate = search_data(item, 'dc:date')
        link = search_data(item, 'link')
        abstract = Nature.parse_abstract(item)
        if abstract:
            abstract = abstract.replace('Abstract', '').replace('\n', '')
        authors = find_data(item, 'dc:creator')
        author = ''
        for au in authors:
            if author == '':
                author = au
            else:
                author = author + ', ' + au
        return paper_information(journal='Nature Physics', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Science Advances
# @info: written by Liangjin Song on 2025-03-01 at Nanchang University
#
class Science_Advances:
    def __init__(self):
        url = "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=sciadv"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        art_type = search_data(item, 'dc:type')
        if art_type != 'Research Article':
            return None
        pubdate = beijing_time(search_data(item, 'dc:date'), "%Y-%m-%dT%H:%M:%SZ")
        link = search_data(item, 'link')
        abstract = ''
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Science Advances', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Science
# @info: written by Liangjin Song on 2025-03-01 at Nanchang University
#
class Science:
    def __init__(self):
        url1 = "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science"
        url2 = "https://www.science.org/action/showFeed?type=axatoc&feed=rss&jc=science"
        response = requests.get(url1, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        response = requests.get(url2, headers=headers)
        if response.ok:
            self.html = response.text + self.html
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "Issue Information":
            return None
        art_type = search_data(item, 'dc:type')
        if art_type != 'Research Article':
            return None
        pubdate = beijing_time(search_data(item, 'dc:date'), "%Y-%m-%dT%H:%M:%SZ")
        link = search_data(item, 'link')
        abstract = ''
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Science', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Astrophysical Journal Letters
# @info: written by Liangjin Song on 2025-03-01 at Nanchang University
#
class APJL:
    def __init__(self):
        url = "https://iopscience.iop.org/journal/rss/2041-8205"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "IOPscience":
            return None
        pubdate = beijing_time(search_data(item, 'dc:date'), "%Y-%m-%dT%H:%M:%SZ")
        link = search_data(item, 'link')
        abstract = search_data(item, 'description')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Astrophysical Journal Letters', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Astrophysical Journal
# @info: written by Liangjin Song on 2025-03-01 at Nanchang University
#
class APJ:
    def __init__(self):
        url = "https://iopscience.iop.org/journal/rss/1538-3881"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    def __item(self, item: str):
        title = search_data(item, 'title')
        if title is None or title == "IOPscience":
            return None
        pubdate = beijing_time(search_data(item, 'dc:date'), "%Y-%m-%dT%H:%M:%SZ")
        link = search_data(item, 'link')
        abstract = search_data(item, 'description')
        author = search_data(item, 'dc:creator')
        if author:
            author = author.replace('\n', '')
        return paper_information(journal='Astrophysical Journal', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles

# ========================================================================= #
#
# @brief: Science Bulletin
# @info: written by Liangjin Song on 2025-03-01 at Nanchang University
#
class Science_Bulletin:
    def __init__(self):
        url = "https://rss.sciencedirect.com/publication/science/20959273"
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.html = ''
        else:
            self.html = response.text
        self.articles = []

    @staticmethod
    def description(item: str) -> tuple:
        date_pattern = r'Publication date: (?:Available online )?(\d{1,2} [A-Za-z]+ \d{4})'
        date_match = re.search(date_pattern, item)
        date_str = date_match.group(1) if date_match else None
        if date_str:
            date_str = datetime.strptime(date_str, "%d %B %Y")
            date_str = date_str.strftime("%Y-%m-%d")
        authors_pattern = r'Author\(s\): ([\w\s,]+)'
        authors_match = re.search(authors_pattern, item)
        authors = authors_match.group(1) if authors_match else None
        return date_str, authors

    def __item(self, item: str):
        title = Nature.parse_title(item)
        if title is None or title == "Issue Information":
            return None
        link = search_data(item, 'link')
        abstract = ''
        pubdate, author = self.description(search_data(item, 'description'))
        return paper_information(journal='Science Bulletin', title=title,
                                 author=author, date=pubdate, link=link, abstract=abstract)

    def parse(self):
        matchs = find_data(self.html, 'item')
        for m in matchs:
            art = self.__item(m)
            if art:
                self.articles.append(art)
        return self.articles


# ========================================================================= #
#
# @brief: collect the data from journal
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Collecter:
    def __init__(self):
        for i in range(3):
            try:
                self.articles = []
                # add articles
                self.articles.extend(GRL().parse())
                self.articles.extend(JGR_SPHY().parse())
                self.articles.extend(AGU_SW().parse())
                self.articles.extend(AGU_AD().parse())
                self.articles.extend(PRL().parse())
                self.articles.extend(PRE().parse())
                self.articles.extend(Nature().parse())
                self.articles.extend(Nature_Comm().parse())
                self.articles.extend(Nature_Phys().parse())
                self.articles.extend(Science_Advances().parse())
                self.articles.extend(Science().parse())
                self.articles.extend(APJL().parse())
                self.articles.extend(APJ().parse())
                self.articles.extend(Science_Bulletin().parse())
                break
            except Exception as e:
                print(f"{i}: {e}")
                if i == 2:
                    raise e
                else:
                    time.sleep(300)

    @staticmethod
    def __keywords(keywords: str, abstract: str, title: str) -> bool:
        kw = keywords.split(',')
        abstract = '' if abstract is None else abstract
        title = '' if title is None else title
        state = False
        for k in kw:
            if k.strip().lower() in abstract.lower() or k.strip().lower() in title.lower():
                state = True
        return state

    def filter(self, date: str, keyword: str, ai) -> list:
        index = []
        for i, art in enumerate(self.articles):
            # print(art.title, art.pubdate)
            if art.pubdate == date and self.__keywords(keyword, art.abstract, art.title):
                if not art.target:
                    self.articles[i].target = True
                    if art.abstract == '':
                        self.articles[i].abstract = "需要转到论文原文查看摘要！"
                        self.articles[i].aisum = "没有阅读到摘要，无法生成总结！"
                    else:
                        self.articles[i].aisum = "AI罢工" # ai.chat(art.abstract)
                index.append(i)
        return index
