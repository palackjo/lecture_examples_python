import glob
import os
import subprocess
import sys




script_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_path, 'test_results')
# These scripts are skipped because they either do not terminate,
# don't really have an output, or require user input.
skip_scripts = ['legendre.py', 'path.py', 'primes_eratosthenes.py', 
                'stops.py', 'sum.py', 
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
    with open(os.path.join(output_path, 
        file_name + '.txt'), 'w') as output_file:
        output_file.write(output)


def read_file(script_name):
    with open(os.path.join(output_path, 
        script_name[:-3] + '.txt'), 'r') as r_file:
        return r_file.read()

def create_results(scripts):
    for script in scripts:
        if os.path.basename(script) in skip_scripts:
            continue
        print('executing ', os.path.basename(script))
        s_output = execute_file(script)
        save_output(script, str(s_output))


def compare_results(scripts):
    faulty_scripts = []
    for script in scripts:
        script_name = os.path.basename(script)
        if script_name in skip_scripts:
            continue
        print('executing ', script_name)
        s_output = str(execute_file(script))
        # desired result
        des_result = read_file(script_name)
        if s_output != des_result:
            print(s_output)
            print(script_name, ' is not working properly')
            faulty_scripts.append(script_name)

    if faulty_scripts:
        print('The faulty scripts can be seen in results.txt')

    with open(os.path.join(script_path, 'results.txt'), 'w') as result_file:
        if faulty_scripts:
            result_file.write('The following scripts didn\'t work properly:\n')
            for f_script in faulty_scripts:
                result_file.write(f_script + '\n')
        else:
            result_file.write('Last test execution was succesful.')



all_scripts = get_files(script_path)


sys.argv.pop(0)
if sys.argv:
    if len(sys.argv) == 1:
        if sys.argv[0] == 'create':
            print('\nCreating desired results.. \n')
            create_results(all_scripts)
        elif sys.argv[0] == 'compare':
            print('\nComparing results to existing ones.. \n')
            compare_results(all_scripts)
        else:
            print('Wrong parameter given.')
    else:
        print('Too many parameters given.')
else:
    print('If you want to create files with the desired results, ' +
        'execute this script with the parameter "create".\n' +
        'If you want to compare the current results of the scripts ' +
        'with the desired results execute this script ' +
        'with the parameter "compare".')
