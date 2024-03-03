from tortoise import Tortoise, connections


async def init(db_url: str, modules: dict, generate_schemas: bool = False):
    await Tortoise.init(db_url=db_url, modules=modules)

    if generate_schemas:
        await Tortoise.generate_schemas()


async def close():
    await connections.close_all()
