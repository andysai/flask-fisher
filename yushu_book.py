from http import HTTP
class YuShuBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url ='http://t.yushu.im/v2/book/serach?q={}&start={}&count={}'

    @classmethod
    def search_by_isbin(self, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keywork(self, keyword):
        url = YuShuBook.keyword_url.format(keyword)
        result = HTTP.get(url)
        return result
