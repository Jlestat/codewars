def remove_url_anchor(url: str) -> str:
    try:
        return url[:url.index('#')]
    except:
        return url


print(remove_url_anchor("www.codewars.com#about"))