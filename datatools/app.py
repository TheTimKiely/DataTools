
import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

from datatools.plotting import MatplotlibPlotter
from datatools.providers import HttpProvider


def parse_hockey_reference(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)

    table = soup.select_one('table.skaters')
    table = soup.find('table', {'id': 'skaters'})
    headers = []
    categories = []

    for thead in table.thead.children:
        if isinstance(thead, str):
            continue
        label = 'aria-label'
        if ('class' in thead) and ('over_header' in thead['class']):
            continue
        for tr in thead.children:
            if isinstance(tr, Tag):
                if label in tr.attrs and tr[label]:
                    headers.append(tr[label])
                elif 'data-stat' in tr.attrs and tr['data-stat']:
                    categories.append(tr['data-stat'])


    for tr in table.tbody.children:
        print(tr)

def parse_quanthockey(url):
    html = urlopen(url).read()

    soup = BeautifulSoup(html)

    table = soup.select_one('table.skaters')
    table = soup.find('table', {'id': 'skaters'})
    headers = []

    for th in table.thead.tr:
        label = 'aria-label'
        if th[label]:
            headers.append(th[label])

    print(headers)


url = r'https://www.quanthockey.com/nhl/teams/detroit-red-wings-players-2017-18-nhl-stats.html'
url = r'https://www.hockey-reference.com/teams/DET/2018.html'
#parse_hockey_reference(url)

url = r'https://www.quanthockey.com/nhl/teams/detroit-red-wings-players-2017-18-nhl-stats.html'
#parse_quanthockey(url)

def run_matplotlib(data_source):
    provider = HttpProvider()
    data = provider.download_data(data_source)
    plotter = MatplotlibPlotter()
    plotter.scatterplot(x_data=data['temp']
                , y_data=data['cnt']
                , x_label='Normalized temperature (C)'
                , y_label='Check outs'
                , title='Number of Check Outs vs Temperature')


if __name__ == '__main__':
    data_source = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip'
    run_matplotlib(data_source)