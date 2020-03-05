
def your_language():
    """
    Created global language_input to let user choose 1 of at lease 3 languages
    """
    global language
    language = input('Select one language: English, Chinese, Japanese ')

your_language()


def greet(name):
    """
    Create a function called 'greet' with one 'name' argument, the string will add after 'Hello'
    """
    if language.lower() == 'english':
        print('Hello, ' + name)
    elif language.lower() == 'chinese':
        print('你好, ' + name)
    elif language.lower() == 'japanese':
        print('こんにちは, ' + name)


def name_input():
    """
    Create another name_input function that you type your own input to replace the 'name' argumment of 'greet' function
    """
    if language.lower() == 'english':
        your_name = input('Enter your name: ')
        greet(your_name)
    elif language.lower() == 'chinese':
        your_name = input('输入您的姓名: ')
        greet(your_name)
    elif language.lower() == 'japanese':
        your_name = input('あなたの名前を入力してください: ')
        greet(your_name)


name_input()