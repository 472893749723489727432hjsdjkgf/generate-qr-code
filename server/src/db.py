from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from server.src.config import settings


engine = create_async_engine(url=settings.URL(),echo=True)
session = async_sessionmaker(bind=engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass



class Url(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str]
    url : Mapped[str]

async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def sendData(file_path : str,url : str):
    url = Url(file_path=file_path, url=url)
    async with session.begin() as sess:
        sess.add(url)
        await sess.commit()

async def getUrl(file_path : str) ->str|None:
    query = select(Url).where(Url.file_path==file_path)
    async with session.begin() as conn:
        res = await conn.execute(query)
        return res.scalar_one_or_none()
