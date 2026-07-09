import json

from app.database import SessionLocal
from app.models.product import Product

db = SessionLocal()

with open("app/data/products.json", "r") as f:
    products = json.load(f)

try:
    for item in products:
        # Skip if product already exists
        exists = db.query(Product).filter(
            Product.slug == item["slug"]
        ).first()

        if exists:
            print(f"Skipping existing product: {item['slug']}")
            continue

        product = Product(
            name=item["name"],
            slug=item["slug"],
            category=item["category"],
            subcategory=item.get("subcategory"),
            brand=item.get("brand"),
            sku=item.get("sku"),
            price=item.get("price"),
            image=item.get("image"),
            short_description=item.get("shortDescription"),
            description=item.get("description"),
            in_stock=item.get("inStock", True),
            featured=item.get("featured", False),
        )

        db.add(product)

    db.commit()
    print("✅ Database seeded successfully.")

except Exception as e:
    db.rollback()
    print(f"❌ Error seeding database:\n{e}")

finally:
    db.close()