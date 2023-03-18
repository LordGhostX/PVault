# PVault

Python CLI based password manager; Generate, store & retrieve your passwords easily & efficiently. Passwords are stored in sqlite db and encrypted with AES256-CBC encryption and Fernet for the data in the database.

Got the inspiration for this project from my gee [@oluwafenyi](https://github.com/oluwafenyi) from [https://github.com/oluwafenyi/password-vault](https://github.com/oluwafenyi/password-vault) where he built the same exact thing. I'm basically upgrading his work but written from scratch.

**🌟 Star the repo if you like what you see**

## Requirements
* [Python 3](https://www.python.org/downloads/)

## Installation and Setup
- Clone the repo
    ```console
    foo@bar:~$ git clone https://github.com/LordGhostX/PVault.git
    ```
- Change directory to PVault
    ```console
    foo@bar:~$ cd PVault
    ```
- Install dependencies in `requirements.txt`
    ```console
    foo@bar:~ /PVault$ pip3 install --upgrade -r requirements.txt
    ```
- Change directory to `source` folder to access pvaualt
     ```console
    foo@bar:~ /PVault$ cd source
    ```

## Usage

1. Generating random passwords
    ```console
    foo@bar:~ /PVault/source$ python pvault.py generate
    Newly generated password copied to clipboard!
    ```
    
    ### [*optional*] To use `$pvault` instead of `python pvault.py` - (**Mac/Linux**)
    - Create an **environment variable** `pvault` :
        ```console
        foo@bar:~ /PVault/source$ export pvault='python pvault.py'
        ```
    - You can now use `$pvault` instead of `python pvault.py`

2. Generating and saving password for an account
    ```console
    foo@bar:~ /PVault/source$ python pvault.py generate gmail.com
    Newly saved password copied to clipboard!
    ```

    ```bash
    # You can also set a custom password
    ```

    ```console
    foo@bar:~ /PVault/source$ python pvault.py generate yahoo.com myverysecurepassword
    Newly saved password copied to clipboard!
    ```

3. Getting a saved password
    ```console
    foo@bar:~ /PVault/source$ python pvault.py account gmail
    Password has been copied to your clipboard!
    ```

4. Getting all saved passwords
    ```console
    foo@bar:~ /PVault/source$ python pvault.py account
    gmail = 1_%ue9~M/xDaht9F1oZ9
    gmails = myverysecurepassword
    ```

5. Overwriting previously saved password
    ```console
    foo@bar:~ /PVault/source$ python pvault.py generate gmail
    The password already exists; Do you wish to overwrite it (y/n)? y
    Newly saved password copied to clipboard!
    ```

    ```bash
    # You can also set a custom password
    ```
    
    ```console
    foo@bar:~ /PVault/source$ python pvault.py generate gmail mynewsecurepassword
    The password already exists; Do you wish to overwrite it (y/n)? y
    Newly saved password copied to clipboard!
    ```

6. Resetting all passwords
    ```console
    foo@bar:~ /PVault/source$ python pvault.py reset
    Are you sure you want to reset all password in the database (y/n)? y
    Completely reset password database
    ```

7. Deleting saved passwords
    ```console
    foo@bar:~ /PVault/source$ python pvault.py delete gmail
    Are you sure you want to delete the user password in the database (y/n)? y
    Completely deleted user password in the database
    ```

    ```bash
    # You can also delete all the passwords at once
    ```

    ```console
    foo@bar:~ /PVault/source$ python pvault.py delete
    Are you sure you want to delete all password in the database (y/n)? y
    Completely deleted password database
    ```
    
8. Other useful commands
    1. Getting Help
    ```console
    foo@bar:~ /PVault/source$ python pvault.py -h
    foo@bar:~ /PVault/source$ python pvault.py --help
    ```
    2. Get Version number
    ```console
    foo@bar:~ /PVault/source$ python pvault.py --version
    ```

##### You will be asked for a master password the very first time you run the script. The master password is what protects the other passwords and should be kept secure because it can't be reset.

## Current Progress
* [x] Write CLI parser
* [x] Master password integration & encryption
* [x] Password Generation Functionality
* [x] Clipboard integration
* [x] Database integration for saving passwords
* [x] Retrieving saved passwords
* [x] Password reset - Individual, Mass
* [x] Deleting saved passwords
* [x] Encrypt password before storing

## TODO
* [ ] Nothing for now

## Author
* LordGhostX

## Contributor
* [@akins-dev](https://github.com/akins-dev)

## License
[MIT](https://opensource.org/licenses/MIT)
