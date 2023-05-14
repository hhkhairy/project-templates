# A Cookie Cutter Template Project for DataFlow pipelines

### Expectations
The scripts in this template expect that you have
* poetry installed
* You have a global python interpreter that has cookiecutter installed

### Preface
* This is the very first iteration for the cookiecutter template. So, it may have some problems. Anyways, we will iteratively fix it to enhance the quality. 
* The main purposes of this template is to
    * minimize the overhead when setting up a new project
    * standardize the project structure

### How it's designed
It's designed to suit our workflows as outlined in Notion.

### Templates
All templates come installed with 
* pytest => testing
* pytest-cov => testing coverage
* ruff => linting

Templates:
* bare-template => Generic template for a project with `src` layout. 
* dataflow-template => A template for dataflow projects
* dataflow-tempalte-extras => A template that uses extras instead of dependency groups (work under progress)