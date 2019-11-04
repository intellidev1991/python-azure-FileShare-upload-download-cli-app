# Installation

### Step1:

> Make sure python >= 3.6  has been installed

 Install following packages using pip in terminal:
 (this package is `vital` to work this cli-app)

* pip install azure-storage-file

### Step2:

> Edit config.json file and put your Azure StorageAccount name, AccessKey->Key1 and FileShare(SMB) name in it.

```json
{
  "configs": {
    "account_name": "YourAzureStorageAccountName",
    "account_key": "Key1 from AccessKey related to your StorageAccount",
    "file_share": "Name of your FileShare(Container) in StorageAccount"
  }
}

```

Tutorial Link:
[https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share](https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)

Azure Portal:
[https://portal.azure.com/](https://portal.azure.com/)


# Usage:

Open your OS Terminal ( like CMD in windows ) inside `Project directory (CLI directory)`.

Type below command for more info and help:

> python updwn.py --help

Type below command to upload `sample_imgs/lake.jpg` to `image/data` path in azure:

> python updwn.py --upload image/data sample_imgs/lake.jpg

Type below command to download `image/data/lake.jpg` in your computer to the current directory:

> python updwn.py --download image/data/lake.jpg

Type below command to see all files list:

> python updwn.py --list

----------------------------------------------

## Screenshot

![screenshot](Usage-prove.png)


Full Stack Developer