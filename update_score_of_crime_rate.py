# # This Python file uses the following encoding: utf-8# !/usr/bin/env pythonimport osimport djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_liveability.settings")django.setup()from liveability.models import TwoDishesOneSoupIdximport loggingimport urllib2import jsonfrom collections import OrderedDictfrom liveability.models import Scoreslog = logging.getLogger(__name__)if __name__ == "__main__":    response = urllib2.urlopen('http://hongkongcrimemap.com/hkcm/crj/')    data = json.load(response)    YuenLong = data["yl_crime_rate"]    WongTaiSin = data["wts_crime_rate"]    SaiKung = data["sk_crime_rate"]    ShaTin = data["st_crime_rate"]    KwaiTsing = data["kwai_tsing_crime_rate"]    caw = data["caw_crime_rate"]    KwunTong = data["kt_crime_rate"]    TaiPo = data["tp_crime_rate"]    WanChai = data["wc_crime_rate"]    YauTsimMong = data["ytm_crime_rate"]    TsuenWan = data["tw_crime_rate"]    North = data["north_crime_rate"]    KowloonCity = data["kowloon_city_crime_rate"]    Island = data["island_crime_rate"]    TuenMun = data["tm_crime_rate"]    ssp = data["ssp_crime_rate"]    southern = data["southern_crime_rate"]    eastern = data["eastern_crime_rate"]    x = OrderedDict()    x["Yuen Long"] = YuenLong    x['Wong Tai Sin'] = WongTaiSin    x['Sai Kung'] = SaiKung    x['Sha Tin'] = ShaTin    x['Kwai Tsing'] = KwaiTsing    x['Central & Western'] = caw    x['Kwun Tong'] = KwunTong    x['Tai Po'] = TaiPo    x['Wan Chai'] = WanChai    x['Yau Tsim Mong'] = YauTsimMong    x['Tsuen Wan'] = TsuenWan    x['North'] = North    x['Kowloon City'] = KowloonCity    x['Island'] = Island    x['Tuen Mun'] = TuenMun    x['Sham Shui Po'] = ssp    x['Southern'] = southern    x['Eastern'] = eastern    d = OrderedDict(sorted(x.items(), key=lambda t: t[1]))    e = list(d.items())    print(e[0][1])    print(e[17][1])    i_min = e[0][1]    i_max = e[17][1]    for x in e:        scaled_score = (x[1] - i_min) / float(i_max - i_min) * 100        inversed_score = 100 - scaled_score        scores_set = Scores.objects.all()        for score in scores_set:            if score.district_en == x[0]:                # print(x[0])                score.crime_rate = 60 + inversed_score * 40 /100                score.save()