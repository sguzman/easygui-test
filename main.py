import easygui

def main() -> None:
    print('hello')

    print(easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No')))
    print(easygui.msgbox('This is a basic message box.', 'Title Goes Here'))
    print(easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry')))


if __name__ == '__main__':
    main()

