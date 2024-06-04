import pandas as pd
import pretty_html_table

def html_from_list(kebabs: list[dict]) -> str:
    results = {}
    for kebab in kebabs:
        for key in kebab.keys():
            if key in results.keys() and not key in ["latitude", "longitude"]: results[key] += [kebab[key]]
            else: results[key] = [kebab[key]]
    df = pd.DataFrame(results)
    return pretty_html_table.build_table(df, 'blue_light')