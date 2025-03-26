
def preprocessing(url):
    check = "https://www.youtube.com/watch?v="

    if check in url:

        url = url.replace(check, "")

        if "&" in url:
                url = url.split("&")[0]
                return url
        else:
                return url
    else:
        print("Invalid URL")