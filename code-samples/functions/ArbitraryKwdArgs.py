def myLangauges(**languages):
    print("my secondary language is " + languages["dbElement"])


if __name__ == '__main__':
    myLangauges(primaryLang="python", optionalLang="scala", secondaryLang="java", dbElement="oracle")
