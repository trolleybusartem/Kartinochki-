from random_word import RandomWords
from icrawler.builtin import GoogleImageCrawler
google_crawler = GoogleImageCrawler(storage={'root_dir': 'E:\Kartinki'})
amount = int(input('Какое количество изображений вы хотите получить? '))
random_words = RandomWords()
words = (random_words.get_random_word())
google_crawler.crawl(keyword=words, max_num=amount)
input()