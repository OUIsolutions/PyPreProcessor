from typing import List


class PreProcessor:

    def __init__(self) -> None:

        self.identifier = '#comp:'
        self.start_scope = ':'
        self.endscope = '#end'
        self.end_comptimes = ['\n', '#']
        self._text = ''
        # args
        self.t = 20
        self.r = 30

    @staticmethod
    def create_ident_text(ident_level: int):
        ident_text = ''
        for i in range(0, ident_level):
            ident_text += '    '
        return ident_text

    def is_string_from_point(self, content: str, point: int, expected: str):
        try:
            comparation = content[point:point + len(expected)]
            return comparation == expected
        except IndexError:
            return False

    def get_expected_if_is_one_of_expecteds(self, content: str, point: int, expecteds: List[str]):
        for i in expecteds:
            if self.is_string_from_point(content, point, i):
                return i
        return None

    def compile(self, content: str) -> str:
        ident_level = 0
        ident_text = ''
        result = 'self.text+="'
        inside_comptime = False
        i = 0
        while True:
            if i >= len(content):
                return result

            current_char = content[i]

            if self.is_string_from_point(content, i, self.endscope):
                ident_level -= 1
                ident_text = self.create_ident_text(ident_level)
                i+=len(self.endscope)
                result+=f'")\n{ident_text}self.text+="'
                continue

            if not inside_comptime:

                if self.is_string_from_point(content, i, self.identifier):
                    result += f'"\n{ident_text}'
                    inside_comptime = True
                    i += len(self.identifier)
                    continue

                result += current_char.replace("\n", "\\n")
                i += 1
                continue

            end_char = self.get_expected_if_is_one_of_expecteds(content, i, self.end_comptimes)
            if end_char:
                result += f'\n{ident_text}self.text+="'
                inside_comptime = False
                i += len(end_char)
                continue

            if self.is_string_from_point(content, i, self.start_scope):
                ident_level += 1
                ident_text = self.create_ident_text(ident_level)

            result += current_char
            i += 1

    def include(self, file: str):
        with open(file, 'r') as arq:
            content = arq.read()
        converted = self.compile(content)
        print(converted)

    def run(self, file: str) -> str:
        self.include(file)
        return self._text
