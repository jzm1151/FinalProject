class IdListConverter:
    regex = '([0-9]+_{1})*'

    def to_python(self, value):
        try:
            value = value.split('_')
            value.pop()
            return value
        except:
            raise ValueError

    def to_url(self, value):
        try:
            return str(value)
        except:
            raise ValueError
