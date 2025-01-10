from django.contrib import admin

# Register your models here.
from .models import News_post

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'short_description', 'text')  # Отображение в списке
    exclude = ('author',)  # Исключаем поле "author" из формы

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если объект новый
            obj.author = request.user  # Устанавливаем текущего пользователя
        super().save_model(request, obj, form, change)

admin.site.register(News_post,NewsAdmin)
