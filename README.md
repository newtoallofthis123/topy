# ToPy - The Cli ToDo Manager

Topy is a simple cli ToDo manager which is purely written in python.
Topy is different from other ToDo managers becuase it doesn't use command line arguments but rather makes it easier with prompts and can be easily operated by commands. 

## Usage and Commands

The commands are as listed below.

1. new, n: New ToDo
2. show , ls , read : Show all the ToDo's
3. mark: Mark a ToDo complete
4. unmark: Mark a ToDo incomplete
5. clear: Clear the screen and all the ToDo's
6. destory: Delete all the ToDo's
7. del: Delete all the done ToDo's
8. license: Show the license
9. about: About ToPy
10. help: Show is Help
11. commands: Show list of available commands.
12. website: Show ToPy website
13. github: Show the github repository of Topy
14. docs: Show the Topy docs
15. quit: Quit ToPy

![ToPy Example](docs/assets/topy_example.png)

## Installation

There are Three ways to install ToPy

1. .exe OneFile
2. .exe zip
3. raw python file
4. [pypi](https://pypi.org) comming soon

## License

ToPy is registered under the [MIT License](https://newtoallofthis123.github.io/license). Hence you are free to use it as you like.

## Building

Topy doesn't actually need building. Yo ucan directly use it as a raw python script.
Just run it as folows in it's directory

```bash
python topy.py
```

If you want to compile it into a onefile exe, You can do that by using [pyinstaller](https://) or [nuitka](https://). Nuitka is recommended, if you are a beginner, use pyinstaller

1. First Clone into the repository
   
   ```bash
   git clone https://github.com/newtoallofthis123/topy.git
   ```
2. Next Change into the directory
   
   ```bash
   cd topy
   ```
3. Next Compile it with either nuitka ot pyinstaller
   Nuitka
   
   ```bash
   python -m nuitka --onefile --windows-disable-console --windows-icon-from-ico="icon.ico" --windows-company-name="NoobScience" --windows-product-name="ToPy" --windows-file-version=0.1  --windows-product-version=0.1 --windows-file-description="A Simple Cli ToDo manager" --python-arch="x86" topy.py
   ```
   
   Pyinstaller
   
   ```bash
   pyinstaller -w - i "icon.ico" -n "ToPy" topy.py
   ```

## Author

Author : NoobScience
Author Website : [Website](https://newtoallofthis123.github.io/About) Author Github : [Github](https://github.com/newtoallofthis123)

## Details

Project name : ToPy
Project version : v.0.1
Projec Github : [Github](https://github.com/newtoallofthis123/topy)

## More info

For more information read the [docs](https://newtoallofthis123.github.io/topy/docs.html)

### Hope you enjoy using ToPy

> NoobScience