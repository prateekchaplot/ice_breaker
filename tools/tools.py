from googlesearch import search


def get_profile_url(text: str) -> str:
    """Searches for linkedin profile page"""
    results = search(f"linkedin {text}", num_results=5)
    return get_first(results)


def get_first(results) -> str:
    """Returns first result from a enumerator list"""
    first = ""
    for index, result in enumerate(results):
        first = result
        if index == 0:
            break
    return first
