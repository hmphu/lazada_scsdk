import re


class Resource(object):
    def __init__(self, client=None):
        self.client = client

    def get_url(self, url, **kwargs):
        try:
            return self.client.get(url, **kwargs)
        except Exception as e:
            print(e)
            return None

    def post_url(self, url, data, **kwargs):
        try:
            return self.client.post(url, data, **kwargs)
        except Exception as e:
            print(e)
            return None

    def no_accent_vietnamese(self, text):
        patterns = {
            '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
            '[đ]': 'd',
            '[èéẻẽẹêềếểễệ]': 'e',
            '[ìíỉĩị]': 'i',
            '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
            '[ùúủũụưừứửữự]': 'u',
            '[ỳýỷỹỵ]': 'y'
        }

        output = text
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.upper(), output)
            output = re.sub(r'\W+', ' ', output)
        return output
