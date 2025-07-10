# seed.py

from faker import Faker
from app import models, database

fake = Faker()
db = database.SessionLocal()

def seed_users(n=5):
    users = []
    for i in range(n):
        user = models.User(
            username=f"user{i}",
            password="password"  # or use hashed passwords
        )
        db.add(user)
        users.append(user)
    db.commit()
    return users

def seed_articles(n=20):
    users = db.query(models.User).all()
    if not users:
        users = seed_users()

    for _ in range(n):
        article = models.Article(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=5),
            author_id=fake.random_element(elements=[u.id for u in users])
        )
        db.add(article)

    db.commit()
    print(f"✅ Seeded {n} fake articles")

if __name__ == "__main__":
    seed_articles(20)
    db.close()
