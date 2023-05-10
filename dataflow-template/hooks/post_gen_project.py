import os

if __name__ == "__main__":
    # PYENV commands
    #pyenv virtualenv "{{cookiecutter.python_version}}" "{{cookiecutter.venv_name}}"
    #pyenv local "{{cookiecutter.venv_name}}"
    os.system('pyenv virtualenv "{{cookiecutter.python_version}}" "{{cookiecutter.venv_name}}"')
    os.system('pyenv local "{{cookiecutter.venv_name}}"')

    # POETRY configs
    os.system("poetry config virtualenvs.in-project false --local")
    os.system("poetry config virtualenvs.prefer-active-python true --local")
    os.system("poetry config virtualenvs.create false --local")

    # POETRY commands
    os.system("poetry init")
    # add typical dependencies for dev and test
    os.system("poetry add pytest --group test")
    os.system("poetry add ruff --group test")
    os.system("poetry add jupyter --group dev")



