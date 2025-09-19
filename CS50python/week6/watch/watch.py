import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if youtube := re.search(r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"',s):
        url = youtube.group(1)
        return f"https://youtu.be/{url}"
    else:
        return "None"
if __name__ == "__main__":
    main()
