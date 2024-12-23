Copilot, please create a Python package named "clamito" that demonstrates a prompt-chaining workflow 
for AI-driven climate data analysis. This package must follow Python best practices, including:
  - A PEP 518–compliant "pyproject.toml" and a "setup.py"
  - A standard package structure with an __init__.py
  - A tests/ directory with at least one simple test
  - A README.md with basic usage instructions

The main goal is to demonstrate three agents, each in its own module:
  1) task_parser.py => TaskParser class
  2) code_generator.py => CodeGenerator class
  3) code_executor.py => CodeExecutor class

The overall workflow:
  - We receive a user request (e.g., "Using the data in /path/to/netcdf/file/data.nc, compute a climatological annual cycle of precipitation.")
  - TaskParser parses that request, applying basic safeguards
  - CodeGenerator uses an LLM call (e.g., OpenAI API) to create Python code for performing the requested analysis (likely with xarray)
  - CodeExecutor runs that code in a sandboxed environment, returning or logging the results

Specific files and content:

1) clamito/__init__.py
   - At minimum, define __version__ and possibly author info.

2) clamito/config.py
   - Provide a simple configuration structure for the OpenAI API (e.g., reading OPENAI_API_KEY from environment variables).

3) clamito/task_parser.py
   - class TaskParser
   - parse_task(user_input: str) -> dict
   - apply_safeguards(parsed_task: dict) -> dict
   - docstrings and inline comments explaining what each method does.

4) clamito/code_generator.py
   - class CodeGenerator
   - generate_code(parsed_task: dict) -> str
   - docstring, placeholders for calling openai.ChatCompletion.create or similar
   - minimal error handling

5) clamito/code_executor.py
   - class CodeExecutor
   - execute_code(generated_code: str) -> Any
   - docstring, basic sandboxing approach, captures/returns result or logs output

6) clamito/__main__.py
   - Provide a simple CLI or demonstration entry point.
   - For instance, prompt for user input or accept sys.argv
   - Pass it through TaskParser -> CodeGenerator -> CodeExecutor
   - Print the final result

7) tests/test_clamito.py
   - Minimal test that imports TaskParser, CodeGenerator, CodeExecutor
   - Tests that they can be instantiated and called without error
   - Optionally mock an LLM response to confirm pipeline success

8) README.md at the root of the project
   - Summarize purpose ("clamito" is an AI-driven climate data analysis package)
   - Explain installation steps ("pip install -e .")
   - Mention usage instructions (how to run clamito, etc.)

9) PEP 518 compliance
   - Create a pyproject.toml with a [build-system] section specifying setuptools (build-backend = "setuptools.build_meta")
   - Create a setup.py that references the metadata from pyproject.toml or sets basic project metadata
   - Show an example of a minimal approach consistent with best practices

Provide as complete a code scaffold as possible. 
Include docstrings, inline comments, and example usage. 
The final structure should look like:

 clamito/
   __init__.py
   config.py
   task_parser.py
   code_generator.py
   code_executor.py
   __main__.py
 tests/
   test_clamito.py
 pyproject.toml
 setup.py
 README.md

Thank you, Copilot! Please generate the best possible initial scaffolding for the "clamito" prototype package.
