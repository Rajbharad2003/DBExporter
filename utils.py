import re

def clean_text(value):
    if isinstance(value, str):
        return re.sub(r'[^\x20-\x7E]', '', value)  # Remove non-printable
    return value

def clean_table_name(name):
    return re.sub(r'[^\w\s-]', '_', name)
