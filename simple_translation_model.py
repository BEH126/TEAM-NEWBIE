from googletrans import Translator
import all_language
import os

language = all_language.LANGUAGES
translator = Translator()


def titles():
    os.system('clear')
    print("{:-^30}".format("-"))
    print("{:^30}".format("Simple Translation Program"))
    print("{:>30}".format("by Team Newbie"))
    print("{:-^30}".format("-"))


def all_symbol():
    for key, value in language.items():
        print(key, ':', value)


def pair_language():
    print("en:English, \nzh-cn:chinese (simplified), \nid:Indonesian")
    texts = input("\nText to translate: ")
    destination = (input("Destination language: ")).lower()

    try:
        translate = translator.translate(texts, dest=destination)
        print("Translated text: ", translate.text)
    except (Exception, ):
        print("Language destination not exist")


def menu():
    print("Main Program")
    while True:
        print("{:-^30}".format("-"))
        print("Choice")
        print("1. Translate languages")
        print("2. Available languages")
        print("3. Exit program")
        print("{:-^30}".format("-"))
        choose = input("Your choice: ")

        if choose == "1":
            pair_language()
        elif choose == "2":
            all_symbol()
        elif choose == "3":
            print("Thanks for using this translator")
            exit()
        else:
            print("Choice not found")


titles()


menu()
