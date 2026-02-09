from django.db import models


class Question(models.Model):
    external_id = models.IntegerField(unique=True, null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    question_text = models.TextField(blank=True)
    options = models.JSONField(null=True, blank=True)
    correct_answer = models.CharField(max_length=1, blank=True)
    explanation_tr = models.TextField(blank=True, default="")

    json_upload = models.FileField(
        upload_to="question_imports/",
        blank=True,
        null=True,
        help_text="Toplu soru eklemek için JSON dosyası yükleyin"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.external_id)
