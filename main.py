import sys
import keyboard
import bcolors
import individualStockAnalyzer
import allStockAnalyzer

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def welcome_message():
    """
    Display a welcome message to the user
    """
    # Use a breakpoint in the code line below to debug your script.
    print('Welcome to StockAnalyzer')  # Press Ctrl+F8 to toggle the breakpoint.
    print('This tool will display stock information and help with stock selections')


def start_analysis():
    """
    Get users input and allow them to stop analysis and kill the app / script
    """

    print('Steps:')
    print(f"{bcolors.Colors.OkGreen}1 - Individual stock analysis")
    print(f"{bcolors.Colors.OkGreen}2 - Full S&P 500 stock analysis")
    print('')
    print(f"{bcolors.Colors.ENDC}Enter your selection (q to quit): ")

    if keyboard.read_key() == '1':
        print('Starting individual stock analysis')
        analyzer = individualStockAnalyzer.IndividualStockAnalyzer()
        analyzer.analyze("MSFT")
    elif keyboard.read_key() == '2':
        print('Starting full S&P 500 stock analysis')
        analyzer = allStockAnalyzer.AllStockAnalyzer()
        analyzer.analyze()
    elif keyboard.read_key() == 'q':
        sys.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Display welcome message to user
    welcome_message()

    # Start Analysis
    start_analysis()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
