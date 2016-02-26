import glob
import os
import subprocess

script_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_path, 'test_results')
# These scripts are skipped because they either do not terminate,
# don't really have an output, or require user input.
skip_scripts = ['path.py', 'stops.py', 'sum.py', 
                'sum_recursive.py', 'switch.py']


# Get the available scripts.
def get_files(path):
    path = os.path.join(path, '..')
    py_files = glob.glob(os.path.join(path, '*.py'))
    return py_files


# Execute the given file and return the output
def execute_file(f_path):
    proc = subprocess.Popen(['python', f_path], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT)
    return proc.communicate()[0]


# Write the results of an execution into an output file.
def save_output(file_path, output):
    file_name = os.path.basename(file_path)[:-3]
    with open(os.path.join(output_path, file_name + '.txt'), 'w') as output_file:
        output_file.write(output)



all_scripts = get_files(script_path)
for script in all_scripts:
    if os.path.basename(script) in skip_scripts:
        continue
    print('executing ', os.path.basename(script))
    s_output = execute_file(script)
    save_output(script, str(s_output))

# TODO: compare the outputs with desired outputs
