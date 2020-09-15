#!/usr/bin/python3

from sys import stdout, stderr, stdin, argv
import datetime
import platform as pf

__version__ = "0.0.10"
__copyright__ = f"Copyright llamaking136 {datetime.datetime.now().year}.\nAll rights reserved."
__about__ = f"Mac-n-Cheese version {__version__}.\n{__copyright__}\nPlatform '{pf.system()}'."
__help__ = f"""Mac-n-Cheese version {__version__}.
{__copyright__}
Platform '{pf.system()}'

Arguments:
-version: Displays the version and a basic about page.
-help: Displays this help page."""

interpret_prompt = "> "

printf = stdout.write
printerr = stderr.write
argv.pop(0)

filename = None

args = ["version", "help"]

# get arguments

for i in argv:
    if (i[0].startswith("-")):
        i = i.replace("-", "").lower()
        if (i in args):
            if ("version" in i):
                print(__about__)
                exit()
            elif ("help" in i):
                print(__help__)
                exit()
        else:
            printerr("[\33[91mERROR\33[0m]: unknown option: " + i + "\n")

try:
    filename = argv[1]
except IndexError:
    filename = "<stdin>"

index = 0

def Throw(type_, details, data, where):
    global filename
    global index
    if (where <= 0):
        raise ValueError("'where' must be over or equal to 1")
    printerr("[\33[91mERROR\33[0m]: file \"" + filename + "\", line " + str(index + 1) + "\n")
    printerr(data + "\n" + (" " * (where - 1)) + "^\n")
    printerr(f"{type_}: {details}\n")

# execution when no file given
"""
if (len(argv) <= 0):
    print(__about__)
    running = True
    while (True):
        try:
            cmd = input(interpret_prompt)
            print(cmd)
        except KeyboardInterrupt:
            try:
                while (True):
                    printerr("\a\n[\33[94mWARNING\33[0m]: really quit? > ")
                    real_quit = input()
                    if (real_quit.lower() == "y" or real_quit.lower() == "yes"):
                        exit()
                    elif (real_quit.lower() == "n" or real_quit.lower() == "no"):
                        break
                    else:
                        printerr("[\33[91mERROR\33[0m]: please type 'y' or 'n'.")
                        continue
            except KeyboardInterrupt:
                exit()
            except EOFError:
                exit()
        except EOFError:
            exit()
"""