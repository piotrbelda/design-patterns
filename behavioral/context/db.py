from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from model import Article, Base

engine = create_engine("sqlite:///:memory:", echo=False, future=True)

SessionLocal = sessionmaker(engine, expire_on_commit=False)

@contextmanager
def db_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    with db_session() as session:
        session.add_all(
            [
                Article(title="Hello", body="World!"),
                Article(title="Python", body="Is awesome :)"),
            ]
        )
        session.commit()
