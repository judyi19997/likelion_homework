from django.db import models
from django.conf import settings

# Create your models here.

# Blog_m이란 테이블 작성 
class Blog_m(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blog/', blank = True, null = True)
    writer = models.CharField(max_length = 100, null = True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'likers') 
    #ManyToManyField => N:M관계 -> 모델간 관게 형성 (두 모델 중 어느곳에 해도 상관없음. settings.AUTH_USER_MODEL보단 Blog_m에서 편의상 해줌.)

# __str__()이란 메소드 오버라이딩 - 객체를 반환할때 객체의 제목을 반환함.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

# Fore
class Comment_m(models.Model):
    commentBlog = models.ForeignKey(Blog_m, on_delete = models.CASCADE) #ForeignKey => 1:N 관계 -> 모델간 관계 형성 (한쪽에 종속)
    commentAuthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, blank = True)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()

    def __str__(self):
        return f"'{self.commentBlog}'에 '{self.commentAuthor}'님이 단 댓글"