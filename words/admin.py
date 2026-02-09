from django.contrib import admin, messages
from django import forms
import json

from .models import Word


class WordAdminForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        json_upload = cleaned_data.get("json_upload")

        # JSON varsa alan zorunluluklarını geç
        if json_upload:
            return cleaned_data

        # Normal ekleme için zorunlu alanlar
        required_fields = [
            "turkish_word",
            "english_word",
            "level",
        ]

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Bu alan zorunludur.")

        return cleaned_data


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    form = WordAdminForm

    list_display = (
        "id",
        "turkish_word",
        "english_word",
        "level",
    )

    search_fields = (
        "turkish_word",
        "english_word",
        "example_sentence",
    )

    list_filter = ("level",)
    list_per_page = 25
    ordering = ("level", "turkish_word")

    fieldsets = (
        ("Kelime Bilgisi", {
            "fields": ("turkish_word", "english_word")
        }),
        ("Seviye", {
            "fields": ("level",)
        }),
        ("Örnek Cümle", {
            "fields": ("example_sentence",)
        }),
        ("Toplu JSON Yükleme", {
            "fields": ("json_upload",)
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.json_upload:
            try:
                obj.json_upload.file.seek(0)
                data = json.load(obj.json_upload.file)

                created, updated, failed = [], [], []

                for item in data:
                    try:
                        w, is_created = Word.objects.update_or_create(
                            turkish_word=item["turkish_word"],
                            english_word=item["english_word"],
                            defaults={
                                "level": item["level"],
                                "example_sentence": item.get("example_sentence", ""),
                            },
                        )

                        if is_created:
                            created.append(w.turkish_word)
                        else:
                            updated.append(w.turkish_word)

                    except Exception as e:
                        failed.append({
                            "word": item.get("turkish_word"),
                            "error": str(e),
                        })

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
                        "🔴 Eklenemeyen: "
                        + ", ".join(
                            f"{f['word']} ({f['error']})" for f in failed
                        )
                    )

                obj.json_upload.delete(save=False)
                return

            except Exception as e:
                messages.error(request, f"JSON okunamadı: {e}")
                return

        super().save_model(request, obj, form, change)
