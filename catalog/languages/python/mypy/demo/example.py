def double(n: int) -> int:
    return n * 2


def main() -> None:
    # 故意的类型错误：str 不能传给 int 参数
    print(double("3"))


if __name__ == "__main__":
    main()
