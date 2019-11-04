
import os
import re
from azure.storage.file import FileService
from config import Configuration


class AzureFileManager():
    def __init__(self):
        # fetch config data
        conf = Configuration()
        # create Azure File share service
        self.file_service = FileService(
            account_name=conf.account_name, account_key=conf.account_key)
        # set azure share file name (container)
        self.file_share = conf.file_share

    def upload_file(self, upload_path, file_path):
        if not os.path.isfile(file_path):
            print("Your file is not exists, check your file path and try again.")
            return
        filename = os.path.basename(file_path)
        # remove ' or " from path, if path was empty like "" or '' set upload_path=None, this make upload file to root directory
        upload_path = upload_path.strip().replace("'", '').replace('"', '')
        # remove start and end / or \
        if upload_path.endswith('/') or upload_path.endswith('\\'):
            upload_path = upload_path[:-1]
        if upload_path.startswith('/') or upload_path.startswith('\\'):
            upload_path = upload_path[1:]
        # sanity check
        upload_path = upload_path if len(upload_path) >= 1 else None

        print("Start uploading...")
        try:
            # create sub directories
            self.create_sub_directories(upload_path)
            # upload
            self.file_service.create_file_from_path(
                share_name=self.file_share,  # file_share name in azure
                directory_name=upload_path,  # server directories address. None => root directory
                file_name=filename,          # Name of file to create in azure
                local_file_path=file_path)
            print("'{0}' has been successfully uploaded".format(filename))
        except:
            print("Failed to upload '{0}', please try again".format(filename))

    def download_file(self, file_path):
        """ download file from azure, enter file path in azure """
        # check file path was not empty
        file_path = file_path.strip().replace("'", '').replace('"', '')
        if len(file_path) == 0:
            print("Please enter a file path")
            return
        filename = os.path.basename(file_path)
        dir_path = os.path.dirname(file_path)
        # if parent path was not available, use None => root directory
        dir_path = dir_path if dir_path else None

        print("Downloading...")
        try:
            self.file_service.get_file_to_path(
                share_name=self.file_share,
                directory_name=dir_path,  # The path to the directory in azure
                file_name=filename,  # Name of existing file in azure
                # Path of file to write to local machine
                file_path="{0}".format(filename))
            print(
                "'{0}' has been successfully downloaded and saved in current directory.".format(filename))
        except:
            print("Failed to download '{0}', either file doesn't exist or you are offline.".format(
                filename))

    def get_list_of_files(self, dir_name=None):
        """ show list of all files and all directories in azure"""
        generator = self.file_service.list_directories_and_files(
            share_name=self.file_share,
            directory_name=dir_name)
        parent = "" if dir_name == None else dir_name
        for file_or_dir in generator:
            if not re.match(r"(.[a-z]*[A-Z]*[0-9]*)$", file_or_dir.name):
                # file
                if len(parent) == 0:
                    print(file_or_dir.name)
                else:
                    print("{0}/{1}".format(parent, file_or_dir.name))
            else:
                # dir
                if len(parent) == 0:
                    self.get_list_of_files(file_or_dir.name)
                else:
                    self.get_list_of_files(
                        "{0}/{1}".format(parent, file_or_dir.name))

    def create_sub_directories(self, path):
        """ create sub directories in Azure """
        if path is None:
            return
        dirs = os.path.normpath(path).split(os.path.sep)
        parent = ''
        for dir in dirs:
            parent += dir if len(parent) == 0 else '/'+dir
            self.file_service.create_directory(self.file_share, parent)
