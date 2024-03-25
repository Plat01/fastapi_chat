from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from .config import DB


class Base(DeclarativeBase):
    pass


engine = create_async_engine(DB.db_url)
# sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't
# call await_only() here. Was IO attempted in an unexpected place?
# (Background on this error at: https://sqlalche.me/e/20/xd2s)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
# the same error
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


if __name__ == '__main__':
    print(DB)
