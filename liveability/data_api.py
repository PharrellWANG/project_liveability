# This Python file uses the following encoding: utf-8import jsonimport loggingfrom collections import OrderedDictfrom rest_framework.renderers import JSONRendererfrom rest_framework.response import Responsefrom rest_framework.views import APIViewfrom .models import PriSchoolRank, MidSchoolRanklog = logging.getLogger(__name__)FLOAT_DATA_FORMAT = '{:,.2f}'class Pri_Edu_Api(APIView):    renderer_classes = (JSONRenderer,)    @staticmethod    def get(request):        list_of_pri = PriSchoolRank.objects.all()        edu_list = []        for x in list_of_pri:            t = {}            log.debug(x.name_of_school)            t['name_of_school'] = x.name_of_school            t['lat'] = x.lat,            t['lng'] = x.lng,            # t['academic'] = x.academic,            # t['sport'] = x.sport,            # t['music'] = x.music,            # t['teaching_resource'] = x.teaching_resource,            # t['dormitory'] = x.dormitory,            # t['ranking_score_this_year'] = x.ranking_score_this_year,            t['ranking_score_average'] = x.ranking_score_average,            t['district_chn'] = x.district_chn,            t['district_eng'] = x.district_eng,            edu_list.append(t)        content = {'PriSchoolRankingAPI': edu_list}        return Response(content)class Mid_Edu_Api(APIView):    renderer_classes = (JSONRenderer,)    @staticmethod    def get(request):        list_of_mid = MidSchoolRank.objects.all()        edu_list = []        for x in list_of_mid:            t = {}            log.debug(x.name_of_school)            t['name_of_school'] = x.name_of_school            t['lat'] = x.lat,            t['lng'] = x.lng,            # t['academic'] = x.academic,            # t['sport'] = x.sport,            # t['music'] = x.music,            # t['teaching_resource'] = x.teaching_resource,            # t['dormitory'] = x.dormitory,            # t['ranking_score_this_year'] = x.ranking_score_this_year,            t['ranking_score_average'] = x.ranking_score_average,            t['district_chn'] = x.district_chn,            t['district_eng'] = x.district_eng,            edu_list.append(t)        content = {'MidSchoolRankingAPI': edu_list}        return Response(content)