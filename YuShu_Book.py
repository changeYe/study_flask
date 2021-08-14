from Httper import Http


# 具体数据的查询
class Yushu_Book:
    sample_url = "http://localhost:8340/hello"
    complex_url = "http://localhost:8340/test"

    @classmethod
    def search_isbn(cls, word):
        url = cls.sample_url.format(word)
        return Http.get(url)

    @classmethod
    def search_keyword(cls, word, count=15, start=0):
        url = cls.complex_url.format(word, count, start)
        return Http.get(url)
