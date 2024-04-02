import glob, os

path = input("Enter the path of the target folder: ")

if not os.path.exists(path):
    print("Error: The specified path does not exist.")
    exit()

folder = os.listdir(path)

for item in glob.iglob(path + '**/**', recursive=True):
    if item.endswith(".html") or item.endswith(".vlc"):
        try:
            os.remove(os.path.join(path, item))
            print("Successfully removed the file:", item)
        except PermissionError:
            print("Permission denied - unable to remove a secured file")

