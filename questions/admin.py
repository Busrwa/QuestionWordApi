from django.contrib import admin, messages
import json
from .models import Question
from django import forms


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        json_upload = cleaned_data.get("json_upload")

        # 🔥 SADECE JSON YÜKLENMİŞSE:
        if json_upload:
            return cleaned_data

        # JSON yoksa normal zorunluluklar
        required_fields = [
            "external_id",
            "category",
            "question_text",
            "options",
            "correct_answer",
        ]

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Bu alan zorunludur.")

        return cleaned_data


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ("id", "category", "correct_answer")
    list_filter = ("category",)
    search_fields = ("question_text",)

    def save_model(self, request, obj, form, change):
        if obj.json_upload:
            try:
                obj.json_upload.file.seek(0)
                data = json.load(obj.json_upload.file)

                created, updated, failed = [], [], []

                for item in data:
                    try:
                        q, is_created = Question.objects.update_or_create(
                            external_id=item["id"],
                            defaults={
                                "category": item["category"],
                                "question_text": item["question_text"],
                                "options": item["options"],
                                "correct_answer": item["correct_answer"],
                                "explanation_tr": item.get("explanation_tr", ""),
                            },
                        )

                        if is_created:
                            created.append(q.external_id)
                        else:
                            updated.append(q.external_id)

                    except Exception as e:
                        failed.append({
                            "id": item.get("id"),
                            "error": str(e)
                        })

                # 🔔 MESAJLAR
                if created:
                    messages.success(
                        request,
                        f"✔ Eklenen ({len(created)}): {created}"
                    )

                if updated:
                    messages.info(
                        request,
                        f"🟡 Güncellenen ({len(updated)}): {updated}"
                    )

                if failed:
                    messages.error(
                        request,
                        f"🔴 Eklenemeyen ({len(failed)}): "
                        + ", ".join([f"{f['id']} ({f['error']})" for f in failed])
                    )

                obj.json_upload.delete(save=False)
                return

            except Exception as e:
                messages.error(request, f"JSON dosyası okunamadı: {e}")
                return

        super().save_model(request, obj, form, change)
