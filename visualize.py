


def html_from_list(kebabs: list[dict]) -> str:
    results = {}
    for kebab in kebabs:
        for key in kebab.keys():
            if results[key]: results[key] += kebab[key]
            else: results[key] = [kebab[key]]
    