# seed.py

from faker import Faker
from app import models, database

fake = Faker()
db = database.SessionLocal()

def seed_articles(n=10):
    for _ in range(n):
        article = models.Article(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=5),
            author_id=fake.random_int(min=1, max=5)
        )
        db.add(article)
    db.commit()
    db.close()
    print(f"✅ Seeded {n} fake articles")

if __name__ == "__main__":
    seed_articles(20)  # or however many you want
