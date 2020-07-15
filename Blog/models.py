from django.db import models

# Create your models here.

# Blog_m이란 테이블 작성 
class Blog_m(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blog/', blank = True, null = True)
    writer = models.CharField(max_length = 100, null = True)

# __str__()이란 메소드 오버라이딩 - 객체를 반환할때 객체의 제목을 반환함.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
