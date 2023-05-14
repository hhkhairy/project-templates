import os

if __name__ == "__main__":
    os.system("poetry config virtualenvs.in-project true --local")
    os.system("poetry config virtualenvs.create true --local")
    os.system("poetry config virtualenvs.prefer-active-python true --local")
    
    # TODO: We can expand this to add the latest version of testing dependencies instead of 
    # hardcoding them in the pyproject.toml file. 
    # TODO: We can also create another version to use pip with extras
    os.system("poetry install --extras test --extras dev")