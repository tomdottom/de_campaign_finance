from bs4 import BeautifulSoup

NON_BREAKING_WHITESPACE = u'\xa0'


class Data(object):

    def __init__(self, html_str, headers=None, skip_rows=0):
        self.soup = BeautifulSoup(html_str, 'html.parser')
        self.rows = iter(self.soup.table.find_all('tr'))
        if headers is None:
            self.headers = [
                unicode(header.string) for header in
                next(self.rows).find_all('td')
            ]
            if (skip_rows - 1) > 0:
                for _ in range(skip_rows - 1):
                    next(self.rows)
        else:
            self.headers = headers
            if (skip_rows) > 0:
                for _ in range(skip_rows):
                    next(self.rows)

    def __iter__(self):
        for row in self.rows:
            data = [
                unicode(col.string).replace(NON_BREAKING_WHITESPACE, ' ')
                for col in row.find_all('td')
            ]
            yield dict(zip(self.headers, data))


def extract_data_from_html(html_str, headers=None, skip_rows=0):
    return Data(html_str, headers=headers, skip_rows=skip_rows)
