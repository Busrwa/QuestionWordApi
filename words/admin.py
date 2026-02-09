from django.contrib import admin
from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    # Liste ekranında gözükecek alanlar
    list_display = (
        'id',
        'turkish_word',
        'english_word',
        'level',
    )

    # Sağ üst arama kutusu (TR + EN)
    search_fields = (
        'turkish_word',
        'english_word',
        'example_sentence',
    )

    # Sağ taraftaki filtreler
    list_filter = (
        'level',
    )

    # Listeleme performansı için
    list_per_page = 25

    # Varsayılan sıralama
    ordering = ('level', 'turkish_word')

    # Detay ekranında alanları grupla
    fieldsets = (
        ('Kelime Bilgisi', {
            'fields': ('turkish_word', 'english_word')
        }),
        ('Seviye', {
            'fields': ('level',)
        }),
        ('Örnek Cümle', {
            'fields': ('example_sentence',)
        }),
    )
