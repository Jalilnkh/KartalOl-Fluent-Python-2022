import re 
import pandas as pd

def check_matches(row_matches, not_that):
        if len(row_matches) == 0:
            return False
        for single_match in row_matches:
            if not re.search(not_that, single_match):
                return True
        else:
            return False

    # Groups here are neccessary for .findall to return entire match. Without them it doesn't return last group in this regex
matched_groups = "aaaaa"
matched_this = pd.Series(matched_groups)


class Calculate:
    def find_in_listings(self, df):
        df = df.copy()
        mask = matched_this.apply(lambda row: check_matches(row, "bbb")) 
        return {"elevator": df[mask]["listing_id"].tolist()}