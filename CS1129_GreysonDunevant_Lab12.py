class Pet:
    def __init__(self, name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_tpe(self):
        return self.__animal_type


def main():
    inputName = input('Enter a pet name: ')
    inputType = input('Enter a pet type: ')
    inputAge = float(input('Enter a pet age: '))

    animalSpecs = Pet(inputName,inputType,inputAge)

    print('Your pet name: ', animalSpecs.get_name())
    print('Your pet type: ', animalSpecs.get_animal_tpe())
    print('Your pet age: ', animalSpecs.get_age())

main()
    
