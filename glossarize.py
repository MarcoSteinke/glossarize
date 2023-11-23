from operator import contains
import pathlib, os

def glossarize(project_path = pathlib.Path(os.getcwd()), filetype = "md"):
    """
    Returns the most frequent terms used in the given directory.
    """
    current_dir = project_path
    files = list(current_dir.rglob(f"*.{filetype}"))

    frequencies = {}
    for file in files:
        with open(file, "r", encoding="UTF-8") as wrapper:
            # read file content
            content = wrapper.read()
            # split content into tokens
            split_content = content.split(" ")
            # filter unstructured information
            forbidden_characters = ["--", "|", "/", "\n", "=", ".", "[", "]", "(", ")", "*", "\"", "{", "}", ";", "_", "%", "$", "%", "?"]
            filtered_content = list(filter(lambda token: len(token) >= 4, split_content))
            # filter forbidden characters
            filtered_content = list(filter(lambda token: not(any(symbol in token for symbol in forbidden_characters)), filtered_content))
            # only keep nouns
            filtered_content = list(filter(lambda token: token != token.lower(), filtered_content))
            # count frequencies for tokens
            for token in filtered_content:
                if token in frequencies:
                    count = frequencies[token]
                    frequencies[token] = count + 1
                else:
                    frequencies[token] = 1

    return sorted(frequencies, key=lambda item: item[1])

def main():
    print(glossarize(filetype="md"))

if __name__ == "__main__":
    main()
