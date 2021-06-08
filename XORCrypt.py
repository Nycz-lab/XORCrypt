import sys

def readFile(name):
    with open(sys.argv[1], 'rb') as file:
        content = file.read()
    return content

def writeFile(name, content):

    with open(name, 'wb') as output:
        output.write(bytes(content))

def crypt(content, key):
    
    content_enc = []
    for i in range(0, len(content)):
        content_enc.append(content[i] ^ ord(key[i % len(key)]))

    return content_enc


def main():
    try:
        file_name = sys.argv[1]
        key = sys.argv[2]
    except:
        print("Too few Arguments! Usage: python xorCrypt.py [File_Name] [Key]")
        return

    try:
        content = readFile(file_name)
    except:
        print("Error File not found!")
        return

    try:
        content = crypt(content, key)
    except:
        print("Error while en-/de-/crypting!")
        return

    try:
        if('.enc' in file_name):
            writeFile(file_name.replace('.enc', ''), content)
        else:
            writeFile(file_name + ".enc", content)

        print("Success! c:")

    except:
        print("Error couldnt write File!")
        return


if(__name__ == "__main__"):
    main()