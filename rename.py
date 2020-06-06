import os
from glob import glob

def main():

    programs = sorted(glob("*/*progex*"))

    for program in programs:
        try:
            name, ext = os.path.splitext(program)
            directory, name = name.split("/")
            descript, number = name.split("-")
            number = number.replace("progex", "ex_")

            os.rename(program, f"{directory}/{number}-{descript}{ext}")

        except:
            print(">>>", program)

        #break

if __name__ == "__main__":
    main()
