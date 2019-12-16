from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')        # Hien thi thuoc tinh
    list_filter = ("status",)                                       # Bo loc
    search_fields = ['title', 'content']                            # Tao fields truong tim kiem dua tren cac thuoc tinh title, content
    prepopulated_fields = {'slug': ('title',)}                      # Khi tao bai viet, slug tu dong them vao


admin.site.register(Post, PostAdmin)




