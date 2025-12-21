import logging
from dataclasses import dataclass
from typing import Any

from sqlalchemy.orm import Session

from db import db_session, init_db
from model import Article


@dataclass
class AppContext:
    user_id: int
    db: Session
    logger: logging.Logger
    config: dict[str, Any]


def retrieve_article(article_id: int, db: Session, logger: logging.Logger) -> Article | None:
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        logger.error(f"Article {article_id} not found :()")
        return None

    return article

def render_article(article: Article, logger: logging.Logger) -> str:
    logger.info(f"Rendering article {article.id}")
    return f"<h1>{article.title}</h1><p>{article.body}</p>"


def send_to_external_service(html: str, api_key: str) -> None:
    print(f"sending to API with key: {api_key[:4]}... content: {html[:30]}")


def publish_article(article_id: int, context: AppContext) -> str | None:
    if context.user_id != 42:
        context.logger.error(f"Unauthorized access by user {context.user_id}")
        return "<p>Unauthorized</p>"

    article = retrieve_article(article_id, context.db, context.logger)
    if not article:
        return "<p>Article not found.</p>"

    html = render_article(article, context.logger)

    send_to_external_service(html, context.config["api_key"])


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("context")

    init_db()

    with db_session() as session:
        context = AppContext(
            user_id=42,
            db=session,
            logger=logger,
            config={
                "api_key": "test1234",
            },
        )

        publish_article(1, context)


if __name__ == "__main__":
    main()
