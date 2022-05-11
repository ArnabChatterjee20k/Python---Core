from PyDictionary import PyDictionary


dict = PyDictionary()

# meaning of "python"
meaning = dict.meaning("human")
print(meaning)

print(dict.translate("hi","es"))

#to input and tell meaning
# a=input("Enter:")
# print(dict.meaning(a))

dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
'There can be any number of words in the Instance'

# print(dictionary.printMeanings())   #'''This print the meanings of all the words'''
# print(dictionary.getMeanings()) #'''This will return meanings as dictionaries'''
# print (dictionary.getSynonyms())

print (dictionary.translateTo("hi")) #'''This will translate all words to Hindi'''
print (dictionary.translateTo("bn"))### bengali
