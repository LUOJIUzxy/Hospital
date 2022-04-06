import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicalWeb.settings")
django.setup()
from myweb.models import Doctor,Patient,Department
import random
def create_departments():
    Department.objects.create(depart_id=10, name="内科",describe = "科室现有医生22人，其中高级职称医生6人，中级职称医生9人。"
        "经验丰富的内科专家常年门诊，对常见病及多发病能进行有效的诊疗外，专科常年聘请华西心血管专家坐诊、会诊，"
        "指导心脑血管疾病的诊治。科室开设高血压、糖尿病等专科疾病门诊，方便辖区内广大师生员工及居民就医。"
    "广大患者真正得到了实惠，真正做到对病人的病情和治疗方案精益求精。")
    Department.objects.create(depart_id=11, name="牙科",describe = "科室现有成员16人，其中副主任医师1人，主治医师5人，"
    "研究生学历5人。科室配置9台口腔综合治疗机、进口的法国赛特力I-Surge牙种植机、瑞士NOUVAG的全自动跟管治疗仪、"
    "冷光牙齿美白仪、激光治疗仪等。")
    Department.objects.create(depart_id=12, name="血液透析科",describe = " 电子科技大学血液透析室，占地面积775平米，环境优美、"
         "配套设施齐全、布局合理，功能分区完善，拥有休息等候区、更衣室、接待室、阴性透析区、阳性透析区、抢救室、"
                                    "水机房、配液间、清洗间、干湿库房、医生办公室等。")
    Department.objects.create(depart_id=13,name="急诊科",describe="我科为医院独立的一级临床科室，坚持以“病人为中心”的服务"
                                    "宗旨，做到“有急必到、有危必救、有求必应”保证第一时间进行抢救，对病员的接诊，"
                                    "抢救分流等运作迅速有序，用最短的时间把最有效的医疗服务提供给伤病员。")
    Department.objects.create(depart_id=14, name="医院影像科", describe="电子科技大学医院影像科成立于2009年，科室设备先进，"
                        "配套设施和人员齐全。科室拥有西门子16排螺旋CT一台，进口DR和CR各一台，透视X光机两台，数字化牙片成像系统两台，"
                         "数字化口腔全景机一台；进口中高端全身彩超机4台，黑白超机两台。科室采用数字化管理，建立了全院图像归档和通讯系统。"
                         "全科现有15名医技人员，其中副主任医生3名，主治医师2名，执业医师法4名，助理医师1名；技师（士）5名。")
    Department.objects.create(depart_id=15, name="五官科", describe="常年聘请经验丰富的主任医师专家坐诊，"
                    "擅长嗓音疾病和鼻炎的治疗。科室配置各种检查设备，喉镜、鼻镜、眼底镜、裂隙灯、检眼镜等。"
                                                "开展各项疑难病的诊疗及各种眼、耳、鼻咽喉常规手术。")
    Department.objects.create(depart_id=16, name="皮肤科", describe="要治疗各种皮肤病，常见皮肤病有牛皮癣 、 疱疹 、"
                "酒渣鼻 、脓疱疮 、化脓菌感染 、疤痕 、癣 、鱼鳞病 、腋臭 、青春痘 、毛囊炎 、"
                "斑秃脱发 、男科炎症 、婴儿尿布疹 、鸡眼 、雀斑 、汗疱疹 、螨虫性皮炎 、白癜风 、湿疹等。")
def main():
    #Doctor.objects.all().delete()
    Department.objects.all().delete()
    create_departments()
    #create_doctor()
if __name__ == "__main__":
    main()
    departments =list(Department.objects.values_list('name'))
    print(departments)
    print("Done!")







