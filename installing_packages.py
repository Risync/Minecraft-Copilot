import subprocess

# if you want to add more packages into the virtual environment, just add the pip install name after sydney-py like this ['sydney-py', 'library_you_want_to_install']
packages = ['sydney-py']

for package in packages:
    subprocess.call(['python', '-m', 'pip', 'install', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
