# clamito/README.md

# clamito: AI-Driven Climate Data Analysis Package

clamito is a Python package designed to facilitate AI-driven climate data analysis through a prompt-chaining workflow. It leverages advanced language models to interpret user requests, generate Python code for data analysis, and execute that code in a controlled environment.

## Installation

To install clamito, clone the repository and run the following command:

```
pip install -e .
```

This will install the package in editable mode, allowing you to make changes to the code without reinstalling.

## Usage

To use clamito, you can run the package from the command line. The package will prompt you for input or you can provide a command-line argument. The input should describe the climate data analysis task you want to perform.

Example command:

```
python -m clamito "Using the data in /path/to/netcdf/file/data.nc, compute a climatological annual cycle of precipitation."
```

This command will initiate the workflow, parsing the request, generating the necessary code, and executing it to return the results.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.