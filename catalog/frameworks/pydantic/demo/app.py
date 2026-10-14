from pydantic import BaseModel, ValidationError, Field


class User(BaseModel):
    id: int
    name: str = Field(min_length=1)
    email: str


def main() -> None:
    ok = User(id=1, name="Ada", email="ada@example.com")
    print("ok:", ok.model_dump())

    try:
        User(id="x", name="", email="not-an-email")
    except ValidationError as exc:
        print("errors:", exc.error_count())
        for err in exc.errors():
            print("-", err["loc"], err["type"])


if __name__ == "__main__":
    main()
