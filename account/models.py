from django.db import models
from django.contrib.auth.models import AbstractUser #기본 user관련 모델.


# Create your models here.

#유저확장을 위한 상속받은 model
class custom_model(AbstractUser):
    # pass - 기본 AbstractUser에 있는 필드만 사용할때.
    GENDER = (
        ("M","남자"),
        ("W", "여자"),
        ("O", '그 밖의 성')
    )
    birthday = models.DateField(blank = True, null = True)
    gender =  models.CharField(max_length = 10, blank = True, null = True, choices = GENDER)

    # def __str__(self):
    #     return self.

