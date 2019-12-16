from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)                                   # Tieu de
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   # Tac gia
    updated_on = models.DateTimeField(auto_now=True)                                        # ngay cap nhat
    content = models.TextField()                                                            # Noi dung
    created_on = models.DateTimeField(auto_now_add=True)                                    # Ngay khoi tao
    status = models.IntegerField(choices=STATUS, default=0)                                 # Trang thai

    class Meta:                             # Sap xep ket qua trong truong created_on theo thu tu giam dan
        ordering = ['-created_on']          # Su dung tien to am, bai viet xuat ban gan day se hien len dau tien

    def __str__(self):
        return self.title



