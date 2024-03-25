import uvicorn
from fastapi import FastAPI

from connections.mysql import engine_mysql
from models import blog_model, user_model
from routers.blog_router import blog_router
from routers.user_router import user_router

app = FastAPI()
app.include_router(blog_router)
app.include_router(user_router)
blog_model.Base.metadata.create_all(engine_mysql.engine)
user_model.Base.metadata.create_all(engine_mysql.engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, log_level="info", reload=True)


