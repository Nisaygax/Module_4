from django.contrib import admin
from .models import Advertisement

# Register your models here.

class Advertisement_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'updated_date', 'price', 'auction', 'user', 'admin_image']
    list_filter = ['auction', 'created_at']
    
    actions = ['make_auction_false', 'make_auction_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction = True)

    fieldsets = (
        ('Общее', {'fields' : ('title', 'description', 'user', 'image')}),
        ('Финансы', {'fields' : ('price', 'auction'), 'classes': ['collapse']})
    )


admin.site.register(Advertisement, Advertisement_Admin)