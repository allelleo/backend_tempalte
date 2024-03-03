from fastapi import FastAPI
from core import settings, database
from user.controller import user

async def lifespan(app: FastAPI):
    await database.init(
        db_url=settings.DATABASE['DB_URL'],
        modules=settings.DATABASE['MODULES'],
        generate_schemas=settings.DATABASE['GENERATE_SCHEMAS']
    )
    app.state.database_connected = True
    yield

    await database.close()


app = FastAPI(lifespan=lifespan)
app.include_router(user, prefix='/user')


