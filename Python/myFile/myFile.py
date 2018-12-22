import os
import logging  # change print() to logging.log(?)

FOLDER_PATH = "C:/Users/Seungwon/Documents/CS stands for Cool Stuff/Python/files"
path = os.path.join(FOLDER_PATH)

# Improve:
# - auto evaluation


class myFileError(Exception):

    def __init__(self, msg):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    def showMsg(self):
        print(self.__class__.__name__ + ": " + self.msg)


class SaveError(myFileError):
    pass


class LoadError(myFileError):
    pass


def Save(text, fileName, mode="w", fileFormat="txt"):  # hmmm two parameter.. it needs two parameter!!!!
    global path

    # append mode
    # do i care about shallow copy thing? I mean it's python..
    text = str(text)

    modes = ("w", "w+", "a", "a+", "r+")
    fileFormats = ("txt", "py", "md", "cfg")

    if mode not in modes:
        raise SaveError(" - Invalid modes")

    if fileFormat not in fileFormats:
        raise SaveError(" - Invalid Format.")

    cont = "\n"
    cont += f"# +# {fileName} #+ #\n"
    cont += text + "\n"
    cont += f"# -# {fileName} #- #\n"

    with open(str(path) + "/" + str(fileName)+ "."+ str(fileFormat), str(mode)) as f:
        f.write(cont)

    # print(f" - {fileName} saved.")


def Load(fileName, fileFormat="txt"):
    global path

    start_i = None
    end_i = None
    cont = ""
    fileFormats = ("txt", "py", "md", "cfg")

    if fileFormat not in fileFormats:
        raise LoadError(" - Invalid Format.")

    with open(f"{path}/{fileName}.{fileFormat}", "r") as f:
        lines = f.readlines()

    # find starting & ending point
    for line in lines:
        if f"# +# {fileName} #+ #" in line:
            start_i = lines.index(line) + 1

        if f"# -# {fileName} #- #" in line:
            end_i = lines.index(line)

    # Check if the points exist
    if start_i is None:
        raise LoadError(f" - Failed finding starting point of {fileName}")

    if end_i is None:
        raise LoadError(f" - Failed finding ending point of {fileName}")

    # Read Contents
    for i in range(start_i, end_i):
        cont += lines[i]

    cont = cont[:len(cont) - 1]

    # print(f" - {fileName} loaded.")
    return cont


def main():
    a = {"a": 1, "b": 2}
    Save(str(a), "a", "i")
    b = eval(Load("a"))
    print(type(b))

if __name__ == '__main__':
    main()
