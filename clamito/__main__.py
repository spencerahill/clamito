import sys
from clamito.task_parser import TaskParser
from clamito.code_generator import CodeGenerator
from clamito.code_executor import CodeExecutor

def main():
    # Prompt for user input
    user_input = input("Please enter your climate data analysis request: ")

    # Initialize the components
    parser = TaskParser()
    generator = CodeGenerator()
    executor = CodeExecutor()

    # Parse the task
    parsed_task = parser.parse_task(user_input)
    parsed_task = parser.apply_safeguards(parsed_task)

    # Generate code based on the parsed task
    generated_code = generator.generate_code(parsed_task)

    # Execute the generated code
    result = executor.execute_code(generated_code)

    # Print the final result
    print("Result of the analysis:", result)

if __name__ == "__main__":
    main()