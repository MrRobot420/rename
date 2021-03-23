import os
import time
# To Do: use input() to get path and name from command line. DONE

def ask_for_files():
    path = input('> Enter the path to the folder: ')
    choice = input('\nWhat do you wish to achieve?\n\n (1) remove patterns\n (2) give new name with enumeration)\n\nEnter: ')

    return path, choice


def retrieve_files(path):
    directory = path + '/'
    path = os.path.dirname(directory)
    all_files = os.listdir(path)
    return all_files


def remove_pattern(pattern, files, directory):
    for file in files:
        time.sleep(0.5)
        if file.__contains__('.DS_Store'):
            continue
        if file.__contains__(pattern):
            # replace with your string
            beforePattern = file.split(pattern)[0]
            afterPattern = file.split(pattern)[1]
            afterWithoutSuffix = afterPattern.split('.')[0]

            new_filename = f'{beforePattern}{afterWithoutSuffix}'

            suffix = file.split('.')[1]
            print(f'{new_filename}.{suffix}')

            os.rename(f'{directory}/{file}', f'{directory}/{new_filename}.{suffix}')


def rename_files(name, files, directory):
    for (index, file) in enumerate(files):
        time.sleep(0.5)
        if file.__contains__('.DS_Store'):
            continue
        # replace with your string
        new_filename = f'{name}{index + 1}'
        suffix = file.split('.')[1]
        print(f'{new_filename}.{suffix}')
        os.rename(f'{directory}/{file}', f'{directory}/{new_filename}.{suffix}')


def execute_steps_for_choice(choice, files, path):
    if choice == '1':
        pattern = input('\n> Enter the pattern: ')
        remove_pattern(pattern, files, path)

    elif choice == '2':
        name = input('\n> Enter the new name: ')
        rename_files(name, files, path)


def main():
    print('\n\n# # #   T H E   R E N A M E R   # # #\n')
    print('WARNING!!!! \n(!) Handle renamer with care!! \n(!) If new name (auto enum) == one that already exists, it might get deleted!\n\n')
    path, choice = ask_for_files()
    files = retrieve_files(path)
    print(files)
    print()
    print(sorted(files))
    execute_steps_for_choice(choice, sorted(files), path)

try:
    main()
except KeyboardInterrupt:
    print('\n\nX SHUTDOWN...')