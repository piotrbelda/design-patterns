from rules import Predicate, predicate
from user import User


@predicate
def is_admin(user: User) -> bool:
    return user.is_admin


@predicate
def is_active(user: User) -> bool:
    return user.is_active


@predicate
def account_older_than_30(user: User) -> bool:
    return user.account_age > 30


rule = is_admin | (is_active & account_older_than_30)


def main() -> None:
    user = User(
        id=1,
        is_admin=False,
        is_active=True,
        account_age=35,
        is_banned=False,
        country="NL",
        credit_score=600,
        has_manual_override=True,
    )

    print(rule(user))


if __name__ == "__main__":
    main()
