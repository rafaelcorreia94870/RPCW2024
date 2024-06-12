import subprocess

# List of Python programs to run
python_programs = [
    "script.py",
    "remove_not_countries.py",
    "getDBPEDIAinfo.py",
    "add_countries_temperature.py",
    "fillMissingData.py",
    "get_country_flags.py",
    "add_countries_continent.py",
    "../preprocess/script.py",
    "jsontottl.py"
]

# Iterate over each program and run it
for program in python_programs:
    print(f"Running {program}...")
    try:
        # Run the program
        result = subprocess.run(["python3", program], capture_output=True, text=True)
        
        # Print the output and error messages
        print(f"Output of {program}:\n{result.stdout}")
        if result.stderr:
            print(f"Error in {program}:\n{result.stderr}")

        # Check if the program exited successfully
        if result.returncode == 0:
            print(f"{program} ran successfully.\n")
        else:
            print(f"{program} exited with return code {result.returncode}.\n")
    except Exception as e:
        print(f"Failed to run {program}: {e}\n")