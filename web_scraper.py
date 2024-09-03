
from urllib.request import urlopen # import basics of urllib
import re
url = "http://olympus.realpython.org/profiles/dionysus" # we will use this variable to open the string

html_bytes = urlopen(url)
html = html_bytes.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)

title = match_results.group()
title = re.sub("<.*?>", "", title)
for string in ["Name:", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)
    
    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset
    
    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip("\r\n\t")
    print(clean_text)
