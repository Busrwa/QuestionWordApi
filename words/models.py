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

    turkish_word = models.CharField(max_length=150)
    english_word = models.CharField(max_length=150)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    example_sentence = models.TextField()

    def __str__(self):
        return f"{self.turkish_word} - {self.english_word}"
