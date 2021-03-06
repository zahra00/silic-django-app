from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICE = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشرشده')
    )

    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField(verbose_name="متن")
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
