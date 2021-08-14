

@staticmethod
def is_keyword(keyword):
    is_isbn = 'keyword'
    if len(keyword) == 13 and keyword.isdigit:
        is_isbn = 'isbn'
    rep_q = keyword.replace('-', '')
    if '-' in keyword and len(rep_q) == 10 and keyword.isdigit:
        is_isbn = 'isbn'
    return is_isbn