# CSE 4308 Project 1

**name: Jacob Valdez**
**id: 1001628688**
**netID: jfv8688**
**email: jacob.valdez2@mavs.uta.edu**

This is my submission for the CSE 4308 Project 1. All code is written in Python 3.8. Solutions for parts 1 and 2 are located directly in the repository root. Please contact me if you have questions.

## Setup

Please install the following packages:
```bash
pip install numpy jnumpy typer
```

If you don't want to mess up your environment, you can install the packages in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install numpy jnumpy typer
```

If your machine has issues installing these packages, run everything in a docker container:

```bash
docker run -i -t civisanalytics/datascience-python:latest /bin/bash
pip install numpy jnumpy typer
git clone https://github.com/JacobFV/cse4308-project1.git
cd cse4308-project1
# stay inside the container for Parts 1 and 2
# type `exit` when you're done testing the code
```

If you don't have access to docker, try testing the code in Google Colab:

1. Go to the [Google Colab](https://colab.research.google.com) website
2. Click the "Sign in" button
3. Run this command in the cell below: `pip install numpy jnumpy typer`
4. Run this command in the cell below: `git clone https://github.com/JacobFV/cse4308-project1.git`
5. Run this command in the cell below: `cd cse4308-project1`
6. Now you should be able to execute the shell commands for Parts 1 and 2 by typing `!<COMMAND>` in code cells.


## Part 1

`find_route/find_route.py` is a Python script. Run it as you would any other python script:

```bash
python find_route.py <input_filename> <origin_city> <destination_city> <heuristic_filename>
```

Example: `cd find_route; python find_route.py input1.txt Bremen Kassel h_kassel.txt`

For help, run: `python find_route.py --help`

## Part 2
