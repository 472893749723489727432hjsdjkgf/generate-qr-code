from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from server.src.config import settings
from sqlalchemy import select

engine = create_async_engine(url=settings.URL())
session = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass



class Url(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str]
    url : Mapped[str]

class TestUrl(Base):
    __tablename__ = "test_urls"
    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str]
    url: Mapped[str]


async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def sendData(file_path : str,url : str):
    url = Url(file_path=file_path, url=url)
    async with session.begin() as sess:
        sess.add(url)
        await sess.commit()


async def TestSendData(file_path : str,url : str):

    url = TestUrl(file_path=file_path, url=url)
    await init_tables()
    async with session.begin() as sess:
        sess.add(url)
        await sess.commit()


async def TestCheckDb(file_path : str) ->str|None:
    async with session.begin() as conn:
        query = select(TestUrl).where(TestUrl.file_path==file_path)
        req = await conn.execute(query)
        result = req.scalars().first()
        return result.url if result else None