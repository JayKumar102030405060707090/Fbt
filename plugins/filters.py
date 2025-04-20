import re

def apply_filters(text, filters):
    if not filters:
        return text

    # Regex Replace
    for pattern, repl in filters.get("regex_replace", {}).items():
        text = re.sub(pattern, repl, text)

    # Hashtag Filter
    hashtags = filters.get("hashtags", [])
    if hashtags:
        if not any(tag in text for tag in hashtags):
            return ""

    # Append/Prepend
    prepend = filters.get("prepend", "")
    append = filters.get("append", "")
    text = f"{prepend}{text}{append}"

    return text