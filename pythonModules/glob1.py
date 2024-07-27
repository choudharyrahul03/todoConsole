import glob

textFile = glob.glob("files/*.txt")
for filePath in textFile:
    with open(filePath,"r") as file:
        content = file.read()
        print(content)