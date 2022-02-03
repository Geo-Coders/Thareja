# Write a static method that checks whether all words in a list starts with a vowel.

print('--- A Program to check whether all words in a list starts with a vowel ---')
print()

class vowel:
    def __init__(self):
        self._list=[]

    def get_data(self):
        print('Press \'quit\' to quit entering items')
        item=input('Enter a word : ')
        while True:
            self._list.append(item)
            item= input('Enter another word : ')
            if item.lower() == 'quit':
                break
        print()        
        return self._list

    @staticmethod
    def Is_starting_with_vowel(list):
        for item in list:
            if item[0].lower() in ['a','e','i','o','u']:
                return True
            else:
                return False

v= vowel()
list= v.get_data()

for item in list:
    print(f'Does {item.capitalize()} start with a vowel? {vowel.Is_starting_with_vowel(item)} ')


