from django.db import models

# Create your models here.
#基础类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=8)

    class Meta:
        abstract = True


#轮播图模型类
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'



#导航模型类
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'