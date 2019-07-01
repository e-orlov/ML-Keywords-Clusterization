from time import gmtime, strftime


def read_file_to_array(path):
    """
    Input:
    - path - string, path to the file
    """

    file_content = []

    with open(path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            file_content.append(line.strip())

    return file_content


def read_file_to_string(path):
    """
    Input:
    - path - string, path to the file
    """
    file_content = ""
    with open(path, 'r') as file:
        file_content += file.read()

    return file_content


def write_file(path, file_content):
    """
    Input:
    - path - string, path to the file
    - file_content - list, content to write
    """

    with open(path, 'a', encoding="utf-8") as file:
        for element in file_content:
            file.write(str(element + '\n'))

    return True


def write_string_file(path, file_content):
    """
    Input:
    - path - string, path to the file
    - file_content - string, content to write
    """
    with open(path, 'a', encoding="utf-8") as file:
        file.write(file_content)

    return True


def generate_filename(custom_filename='null'):

    # Create a file names with current data and time
    current_datetime = strftime("%Y-%m-%d %H-%M-%S", gmtime())

    # Use Custom Name if Needed
    if(custom_filename != 'null'):
        return str(current_datetime +
                   " - " + custom_filename)
    else:
        return str(current_datetime)


def generate_file(file_name, directory_path):

    if (directory_path[len(directory_path)-1] != '/'):
        directory_path += "/"

    full_path = directory_path + file_name + ".txt"

    print(full_path)
    open(full_path, 'w+', encoding='utf-8')

    return True
