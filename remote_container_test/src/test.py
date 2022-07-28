import platform


def test() -> str:
    platform_information = platform.platform()
    return f"platform : {platform_information}"

if __name__ == "__main__":
    print(test())