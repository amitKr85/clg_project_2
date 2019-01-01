import urllib.request
from bs4 import BeautifulSoup


def get_page(topic):
    domain = "https://en.wikipedia.org"
    html = urllib.request.urlopen("https://en.wikipedia.org/w/index.php?search="+topic.replace(' ','+')+"&title=Special%3ASearch&go=Go")
    soup = BeautifulSoup(html, features="lxml")
    first_result = soup.find(attrs={"data-serp-pos": "0"})
    if first_result is None:
        print('page-found')
        return soup
    href = first_result.get('href')
    print('opening first-result')
    html = urllib.request.urlopen(domain+href)
    soup = BeautifulSoup(html, features="lxml")
    return soup


def get_first_para(topic):
    soup = get_page(topic)
    text_section = soup.find(attrs={'class': 'mw-parser-output'})
    text = ''
    for child in text_section.children:
        # print('for tag', child.name, child)
        try:
            if child is not None:
                if child.name == 'p':
                    text += child.text.lower()
                elif child.name == 'div' and 'class' in child.attrs and 'toc' in child['class']:
                    break
        except Exception as e:
            print("exception", e)
    return text


if __name__ == '__main__':

    print(get_first_para('computer vision'))