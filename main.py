import os
import re


def is_hex(source_string) -> bool:
    try:
        int(source_string, 16)
        return True
    except ValueError:
        return False


def convert_if_hex(source_string) -> str:
    return normalize_hex(source_string) if is_hex(source_string) else source_string


def normalize_hex(hex_string) -> str:
    return f'|{hex(int("0x" + hex_string.replace("|", ""), 0)).upper().replace("0X", "")}'


def main() -> None:
    print('enter input file: ', end='')

    file_path = input().replace('"', '')
    file_path_split = file_path.split('\\')

    if not os.path.exists(path=file_path):
        raise Exception(f'The specified file "{file_path}" does not exists.')

    with open(file_path, encoding='utf-8') as input_file:
        # copy all of lines from the input file, this is not good for bigger files
        # considering improvements
        lines = list(map(str.strip, input_file.readlines()))

        output_filename = f'{file_path_split[-1]}.md'
        output_path = '\\'.join(file_path_split[:-1] + [output_filename])

        md_header_count = len(lines[0].split())
        md_header = '|'.join(lines[0].split())
        md_header_separator = f'{"|".join("----" for x in range(md_header_count))}'

        # remove header in input file from the buffer
        del lines[0]

        access_mode = 'x'

        if os.path.exists(output_path):
            print(f'the output file {output_filename} already exists, opening new one')
            access_mode = 'w'

        with open(output_path, access_mode, encoding='utf-8') as output_file:
            # markdown table header
            output_file.write(f'|{md_header}|\n')
            output_file.write(f'|{md_header_separator}|\n')

            for line in lines:
                words = map(convert_if_hex, f'|{line}|'.split())

                text = '|'.join(words)
                output_file.write(f'{text}\n')

    print(f'output: "{output_path}"')
    print(f'done!')


if __name__ == '__main__':
    main()
