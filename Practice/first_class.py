class CohortThirteen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def set_name(name):
        CohortThirteen.name = name
        # self.age = age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


if __name__ == '__main__':
    result = CohortThirteen("Amirah", 22)
    print(result.get_name(), result.get_age())
    result.set_name("simi")
    print(result.get_name())
    result.set_name("Fill here Fill here ponpon")
    print(result.get_name())
