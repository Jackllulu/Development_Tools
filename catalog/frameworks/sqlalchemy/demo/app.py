from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


def main() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(User(name="Ada"))
        session.commit()

        user = session.scalar(select(User).where(User.name == "Ada"))
        assert user is not None
        print(f"id={user.id} name={user.name}")


if __name__ == "__main__":
    main()
