import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicalWeb.settings")
django.setup()
from myweb.models import Doctor,Department
import random
def create_doc():
    Doctor.objects.create(dor_id=1601, name="李光", gender="男", department=Department.objects.get(depart_id=16),
                          speciality="治疗", describe="主治医生")
    Doctor.objects.create(dor_id=1101, name="赵倩", gender="女", department=Department.objects.get(depart_id=11),
                          speciality="康复", describe="主治医生")
    Doctor.objects.create(dor_id=1001, name="于娜", gender="女", department=Department.objects.get(depart_id=10),
                          speciality="感冒", describe="主治医生")
    Doctor.objects.create(dor_id=1501, name="吴刚", gender="男", department=Department.objects.get(depart_id=15),
                          speciality="近视", describe="主治医生")
    Doctor.objects.create(dor_id=1502, name="周小一", gender="男", department=Department.objects.get(depart_id=15),
                          speciality="发炎", describe="主治医生")
    Doctor.objects.create(dor_id=1503, name="吴大刚", gender="男", department=Department.objects.get(depart_id=15),
                          speciality="手术", describe="主治医生")
    Doctor.objects.create(dor_id=1301, name="小美", gender="女", department=Department.objects.get(depart_id=13),
                          speciality="全能", describe="主治医生")
    Doctor.objects.create(dor_id=1401, name="周娜", gender="女", department=Department.objects.get(depart_id=14),
                          speciality="全能", describe="主治医生")
    Doctor.objects.create(dor_id=1201, name="孙军", gender="男", department=Department.objects.get(depart_id=12),
                          speciality="全能", describe="主治医生")
def main():
    Doctor.objects.all().delete()
    create_doc()
if __name__ == "__main__":
    main()
    doctors =list(Doctor.objects.values_list('name'))
    print(doctors)
    print("Done!")