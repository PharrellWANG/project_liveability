# This Python file uses the following encoding: utf-8# !/usr/bin/env python""" title: data crawler for house price """import osimport djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_liveability.settings")django.setup()import urllibimport loggingfrom django.utils import timezoneimport geocoderfrom bs4 import BeautifulSoupimport pytzfrom datetime import datetimefrom liveability.models import TwoDishesOneSoupIdx, HousePricePerSquareInch# import timeimport requestslog = logging.getLogger(__name__)# print ("--")if __name__ == "__main__":    start = timezone.localtime(timezone.now())    print("=============================")    print('$>>>>> start at:    %s' % start)    print("$----> Crawler starting... #####")    url_list = [        # 'http://proptx.midland.com.hk/mpp/default.jsp?lang=zh',        'http://proptx.midland.com.hk/mpp/',    ]    for url in url_list:        # print(url)        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content        # print(page)        soup = BeautifulSoup(page, 'html.parser')        # print(soup.prettify())        collection = soup.find_all("tr", class_="row_out_1")        # total_number_of_rows = 0        length_of_collection = len(collection)        # total_number_of_rows += length_of_collection        # print(total_number_of_rows)        print("==============")        print('number_of_district:' + str(len(collection)))        # print(collection)        # print(collection[1])        counter = 0        for x in collection:            # print(x)            counter += 1            prices = x.find_all('td', class_="tdcolor_price")            # print(prices[3])            # for tag in prices[]:            #     price = tag.text.strip()[10:17]            price = str(prices[2].text.strip()[1:7])            price = int(price.replace(",", ''))            entry = ''            print(price)            if counter == 1:  # caw                entry = HousePricePerSquareInch.objects.get(id=1)                entry.ave_price = price            elif counter == 2:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=3)                entry.ave_price = price            elif counter == 3:  # Southern                entry = HousePricePerSquareInch.objects.get(id=4)                entry.ave_price = price            elif counter == 4:  # Wan Chai                entry = HousePricePerSquareInch.objects.get(id=2)                entry.ave_price = price            elif counter == 5:  # Kowloon city                entry = HousePricePerSquareInch.objects.get(id=7)                entry.ave_price = price            elif counter == 6:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=5)                entry.ave_price = price            elif counter == 7:  # ssp                entry = HousePricePerSquareInch.objects.get(id=6)                entry.ave_price = price            elif counter == 8:  # wong tai sin                entry = HousePricePerSquareInch.objects.get(id=8)                entry.ave_price = price            elif counter == 9:  # guantang                entry = HousePricePerSquareInch.objects.get(id=9)                entry.ave_price = price            elif counter == 10:  # Tai Po                entry = HousePricePerSquareInch.objects.get(id=15)                entry.ave_price = price            elif counter == 11:  # yuanlong                entry = HousePricePerSquareInch.objects.get(id=13)                entry.ave_price = price            elif counter == 12:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=12)                entry.ave_price = price            elif counter == 13:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=14)                entry.ave_price = price            elif counter == 14:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=17)                entry.ave_price = price            elif counter == 15:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=16)                entry.ave_price = price            elif counter == 16:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=11)                entry.ave_price = price            elif counter == 17:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=10)                entry.ave_price = price            elif counter == 18:  # Eastern                entry = HousePricePerSquareInch.objects.get(id=18)                entry.ave_price = price            entry.save()    end = timezone.localtime(timezone.now())    c = end - start    duration = "%s days, %.2dh: %.2dm: %.2ds" % (c.days, c.seconds // 3600, (c.seconds // 60) % 60, c.seconds % 60)    print duration