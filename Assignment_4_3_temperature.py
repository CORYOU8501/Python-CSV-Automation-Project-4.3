from datetime import datetime
from pathlib import Path

CSV_FILE = Path(__file__).with_name('ZooData.csv')


# Converts a Fahrenheit temperature to Celsius.
def convertData(temperature):
    return (temperature - 32) * 5 / 9


# Appends a comma-separated record to the CSV file.
def insertData(file_path, data):
    try:
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            file.write(data + '\n')
        return True
    except OSError as error:
        print(f'Error saving data: {error}')
        return False


# Displays the CSV file location and all of its saved records.
def viewData(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f'The file {Path(file_path).resolve()} contains:')
            contents = file.read()
            print(contents if contents else 'No entries have been saved yet.', end='' if contents else '\n')
    except OSError as error:
        print(f'Error reading data: {error}')


# Collects dates and temperatures, converts them, and saves each entry.
def getInput():
    try:
        number_of_entries = int(input('How many entries would you like to add? '))
        if number_of_entries <= 0:
            print('Please enter a number greater than zero.')
            return

        for entry in range(number_of_entries):
            date = input('Enter a date (MM/DD/YYYY): ').strip()
            temperature = float(input('Enter the highest temp for the inputted date: '))
            converted = convertData(temperature)
            data = f'{date},{temperature:g},{converted}'

            if insertData(CSV_FILE, data):
                print(f'The following data was saved at {datetime.now()}')
                print(data)
    except ValueError:
        print('Error: Please enter a valid number for the count or temperature.')
    except (EOFError, KeyboardInterrupt):
        print('\nData entry was canceled.')


# Displays the menu and runs the function selected by the user.
def main():
    while True:
        print('\n' + '=' * 52)
        print("coryou8501's Spreadsheet Automation Menu")
        print('Choose a number from the following options')
        print('1 Input Data')
        print('2 View Current Data')
        print('3 Generate Report')
        print('4 Exit')

        choice = input('Enter your choice: ').strip()
        if choice in ('1', '2', '3', '4'):
            print(f'You selected {choice} at {datetime.now()}')
        if choice == '1':
            getInput()
        elif choice == '2':
            viewData(CSV_FILE)
        elif choice == '3':
            print('Report generation will be added in a future assignment.')
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Error: Invalid choice selected.')


# Starts the spreadsheet automation program.
if __name__ == '__main__':
    main()
