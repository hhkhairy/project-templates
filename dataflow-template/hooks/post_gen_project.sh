# Create the pyenv venv and activate it in cookiecutter
echo "Starting pregen bash script"
pyenv virtualenv "{{ cookiecutter.python_version }}" "{{ cookiecutter.venv_name }}"
pyenv local "{{ cookiecutter.venv_name }}"


## Poetry
# For safety, configure poetry to respect the pyenv venv
poetry config virtualenvs.in-project false --local
poetry config virtualenvs.prefer-active-python true --local
poetry config virtualenvs.create false --local
# init poetry
poetry init
# add typical dependencies for dev and test
poetry add pytest --group test
poetry add ruff --group test
poetry add jupyter --group dev


