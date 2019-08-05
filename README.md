# PVault

Python CLI based password manager; Generate, store & retrieve your passwords easily & efficiently. Passwords are stored in sqlite db and encrypted with AES256-CBC encryption and Fernet for the data in the database.

Got the inspiration for this project from my gee [@oluwafenyi](https://github.com/oluwafenyi) from [https://github.com/oluwafenyi/password-vault](https://github.com/oluwafenyi/password-vault) where he built the same exact thing. I'm basically upgrading his work but written from scratch.

**🌟 Star the repo if you like what you see**

## Requirements
* Python 3

## Usage
1. Have all the necessary requirements
    1. Install python3
    2. Install the `requirements.txt`
    ```bash
    $ pip3 install --upgrade -r requirements.txt
    ```
2. Clone the repo
3. Generating random passwords
    ```bash
    $ pvault generate
    "Newly generated password copied to clipboard!"
    ```
4. Generating and saving password for an account
    ```bash
    $ pvault generate gmail.com
    "Newly saved password copied to clipboard!"
    ```
    you can also set a custom password
    ```bash
    $ pvault generate yahoo.com myverysecurepassword
    "Newly saved password copied to clipboard!"
    ```
5. Getting a saved password
    ```bash
    $ pvault account gmail
    "Password has been copied to your clipboard!"
    ```
6. Getting all saved passwords
    ```bash
    $ pvault account
    "gmail = 1_%ue9~M/xDaht9F1oZ9"
    "gmails = myverysecurepassword"
    ```
7. Overwriting previously saved password
    ```bash
    $ pvault generate gmail
    "The password already exists; Do you wish to overwrite it (y/n)? y"
    "Newly saved password copied to clipboard!"
    ```
    you can also set a custom password
    ```bash
    $ pvault generate gmail mynewsecurepassword
    "The password already exists; Do you wish to overwrite it (y/n)? y"
    "Newly saved password copied to clipboard!"
    ```
8. Resetting all passwords
  ```bash
  $ pvault reset
  "Are you sure you want to reset all password in the database (y/n)? y"
  "Completely reset password database"
  ```
9. Deleting saved passwords
  ```bash
  $ pvault delete gmail
  "Are you sure you want to delete the user password in the database (y/n)? y"
  "Completely deleted user password in the database"
  ```
  you can also delete all the passwords at once
  ```bash
  $ pvault delete
  "Are you sure you want to delete all password in the database (y/n)? y"
  "Completely deleted password database"
  ```
10. Other useful commands
    1. Getting Help
    ```bash
    $ pvault -h
    $ pvault --help
    ```
    2. Get Version number
    ```bash
    $ pvault --version
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

## License
[MIT](https://opensource.org/licenses/MIT)
