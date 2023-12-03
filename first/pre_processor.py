from typing import List
from .instruction_list import InstructionList

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
     
        instructions = InstructionList()

        inside_comptime = False
        i = 0
        while True:
            if i >= len(content):
                return str(instructions)

            current_char = content[i]

            if self.is_string_from_point(content, i, self.endscope):
                i+=len(self.endscope)
                instructions.decrease_ident()
                continue

            if not inside_comptime:

                if self.is_string_from_point(content, i, self.identifier):
                    instructions.add_code_block()
                    inside_comptime = True
                    i += len(self.identifier)
                    continue

                instructions.add_text_to_last_instruction(current_char)
                i += 1
                continue

            end_char = self.get_expected_if_is_one_of_expecteds(content, i, self.end_comptimes)
            if end_char:
                instructions.add_text_block()
                inside_comptime = False
                i += len(end_char)
                continue

            if self.is_string_from_point(content, i, self.start_scope):
                instructions.increase_ident()
         


            instructions.add_text_to_last_instruction(current_char)
            i += 1

    def include(self, file: str):
        with open(file, 'r') as arq:
            content = arq.read()
        converted = self.compile(content)
        print(converted)

    def run(self, file: str) -> str:
        self.include(file)
        return self._text
