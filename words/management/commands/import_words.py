import json
import os
from django.core.management.base import BaseCommand
from words.models import Word

class Command(BaseCommand):
    help = "Import words from JSON file, skip existing without logging"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        created = 0
        skipped_list = []

        ALLOWED_LEVELS = {"A1", "A2", "B1", "B2", "C1", "C2"}

        for item in data:
            turkish = item.get("turkish_word", "").strip()
            english = item.get("english_word", "").strip()
            raw_level = item.get("level", "").strip().upper()

            # 🔥 Level temizleme
            if "/" in raw_level:
                raw_level = raw_level.split("/")[-1]

            if raw_level not in ALLOWED_LEVELS:
                raw_level = ""

            # Eğer kelime zaten varsa atla ve skipped'e ekleme
            if Word.objects.filter(turkish_word=turkish, english_word=english).exists():
                continue

            # Hatalı level veya eksik kelime varsa skipped_list'e ekle
            if not turkish or not english or not raw_level:
                skipped_list.append(item)
                continue

            # Yeni ve hatasız kelimeyi ekle
            Word.objects.create(
                turkish_word=turkish,
                english_word=english,
                level=raw_level,
                example_sentence=item.get("example_sentence", "").strip()
            )
            created += 1

        # Skipped kelimeleri dosyaya yaz
        if skipped_list:
            skipped_path = os.path.join(os.path.dirname(file_path), "skipped_words.json")
            with open(skipped_path, "w", encoding="utf-8") as f:
                json.dump(skipped_list, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS(
            f"✔ Import tamamlandı | Eklenen: {created} | Atlanan (hatalı): {len(skipped_list)}"
        ))
