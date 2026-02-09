from django.db import models

class Word(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]

    turkish_word = models.CharField(max_length=150, blank=True)
    english_word = models.CharField(max_length=150, blank=True)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=True)
    example_sentence = models.TextField(blank=True)

    # 🔥 TOPLU JSON YÜKLEME
    json_upload = models.FileField(
        upload_to="word_imports/",
        blank=True,
        null=True,
        help_text="Toplu kelime eklemek için JSON dosyası yükleyin"
    )

    def __str__(self):
        return f"{self.turkish_word} - {self.english_word}"
