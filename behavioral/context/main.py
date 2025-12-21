import logging

from sqlalchemy.orm import Session

from db import db_session, init_db
from model import Article


def render_article(
    user_id: int, article_id: int, db: Session, logger: logging.Logger, api_key: str
) -> str:
    if user_id != 42:
        logger.error(f"Unauthorized access by user: {user_id}")
        return "<p>Unauthorized</p>"

    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        logger.error(f"Article {article_id} not found :()")
        return "<p>Article not found.</p>"

    logger.info(f"Rendering article {article_id} using API key: {api_key[:4]}...")
    return f"<h1>{article.title}</h1><p>{article.body}</p>"


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("context")

    init_db()

    with db_session() as session:
        api_key = "test1234"

        html = render_article(42, 1, session, logger, api_key)
        print(html)

        html = render_article(41, 999, session, logger, api_key)
        print(html)


if __name__ == "__main__":
    main()
