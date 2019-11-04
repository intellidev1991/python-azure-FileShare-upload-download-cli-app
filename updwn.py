import sys
import random
from azureFileManager import AzureFileManager
from utilities import print_blue, print_green, print_red


def perform_commands():
    """ handle command line interface """
    args = sys.argv
    args = args[1:]  # Skip file name

    if len(args) == 0:
        print('You should pass command, please use --help for more info')
    else:
        # create AzureFileManager
        afm = AzureFileManager()
        # command name
        command = args[0]
        if command == '--help':
            print_blue('Upload/Download command line interface')
            print_green('Commands:')
            print_green('   updwn --upload <upload path> <file path>')
            print_green('   updwn --download <path>')
            print_green('   updwn --list')
            print('')
        elif command == '--upload':
            if len(args)is not 3:
                print_red(
                    "Incorrect parameters, please use correct one ->  updwn --upload <upload path> <file path>")
                exit(1)
            upload_path = args[1]
            file_name = args[2]
            afm.upload_file(upload_path, file_name)
        elif command == '--download':
            if len(args)is not 2:
                print_red(
                    "Incorrect parameters, please use correct one ->  updwn --download <path>")
                exit(1)
            path = args[1]
            afm.download_file(path)
        elif command == '--list':
            if len(args)is not 1:
                print_red(
                    "Incorrect format, please use correct one ->  updwn --list")
                exit(1)
            print_blue("========= List of all files ========= ")
            afm.get_list_of_files()
        else:
            print_red('Unrecognised argument.')


if __name__ == '__main__':
    perform_commands()
