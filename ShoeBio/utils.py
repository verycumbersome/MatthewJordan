import csv
import os
import shutil

class Utils:
    # def __init__(self):
    #     self.spiderlist

    def get_urls(self):
        urls = []
        with open("./data/shoes.csv", "rb") as shoe_csv:
            shoe_urls = csv.reader(shoe_csv, delimiter=',')

            for url in shoe_urls:
                urls.append(url[0].split(' ')[0])

            return urls

    def update_spiders(self, site_name, site_url):
        shutil.rmtree("/Shoebio/Shoebio/spiders")
        os.system("scrapy genspider"+site_name+site_url)

if __name__=="__main__":
    print get_urls()
