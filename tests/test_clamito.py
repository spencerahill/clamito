import unittest
from clamito.task_parser import TaskParser
from clamito.code_generator import CodeGenerator
from clamito.code_executor import CodeExecutor

class TestClamito(unittest.TestCase):

    def setUp(self):
        self.task_parser = TaskParser()
        self.code_generator = CodeGenerator()
        self.code_executor = CodeExecutor()

    def test_task_parser_instantiation(self):
        self.assertIsInstance(self.task_parser, TaskParser)

    def test_code_generator_instantiation(self):
        self.assertIsInstance(self.code_generator, CodeGenerator)

    def test_code_executor_instantiation(self):
        self.assertIsInstance(self.code_executor, CodeExecutor)

    def test_parse_task(self):
        user_input = "Using the data in /path/to/netcdf/file/data.nc, compute a climatological annual cycle of precipitation."
        parsed_task = self.task_parser.parse_task(user_input)
        self.assertIsInstance(parsed_task, dict)

    def test_generate_code(self):
        parsed_task = {"task": "compute annual cycle", "data_path": "/path/to/netcdf/file/data.nc"}
        generated_code = self.code_generator.generate_code(parsed_task)
        self.assertIsInstance(generated_code, str)

    def test_execute_code(self):
        generated_code = "print('Hello, World!')"
        result = self.code_executor.execute_code(generated_code)
        self.assertIsNone(result)  # Assuming the code prints to stdout and returns None

if __name__ == '__main__':
    unittest.main()