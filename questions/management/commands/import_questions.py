import json
from django.core.management.base import BaseCommand
from questions.models import Question

class Command(BaseCommand):
    help = "Import questions from JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        created = []
        updated = []
        failed = []

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            try:
                obj, is_created = Question.objects.update_or_create(
                    external_id=item["id"],
                    defaults={
                        "category": item["category"],
                        "question_text": item["question_text"],
                        "options": item["options"],
                        "correct_answer": item["correct_answer"],
                        "explanation_tr": item.get("explanation_tr", ""),
                    }
                )

                if is_created:
                    created.append(item["id"])
                else:
                    updated.append(item["id"])

            except Exception as e:
                failed.append({
                    "id": item.get("id"),
                    "error": str(e)
                })

        self.stdout.write(self.style.SUCCESS("✔ Import tamamlandı"))
        self.stdout.write(f"🟢 Eklenenler: {created}")
        self.stdout.write(f"🟡 Güncellenenler: {updated}")
        self.stdout.write(f"🔴 Hatalılar: {failed}")
