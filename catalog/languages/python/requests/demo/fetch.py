import requests


def main() -> None:
    # httpbin 为常用 HTTP 联调服务；离线环境可改为对本机服务发请求
    resp = requests.get("https://httpbin.org/get", params={"q": "demo"}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("status:", resp.status_code)
    print("url:", data.get("url"))


if __name__ == "__main__":
    main()
