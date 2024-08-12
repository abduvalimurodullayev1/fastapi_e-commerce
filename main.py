from app.routers import products, categories, carts, users, auth, accounts
from fastapi import FastAPI

description = """
 E-commerce API!

* Github: https://github.com/abduvalimurodullayev1
"""

app = FastAPI(
    description=description,
    title="E-commerce API",
    version="1.0.0",
    contact={
        "name": "Abduvali Murodullayev",
        "url": "https://github.com/abduvalimurodullayev1",
    },

)

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)
