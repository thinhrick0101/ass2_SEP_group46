# Report for Assignment 2

Programming language used: Python

## Workflow 1: Testing (`testing.yml`)

The tool used to build and run the test is the Python Poetry packaging and dependency management tool. It is installed when the workflow is ran on Github.

[Link to one log (from the "Actions" tab on GitHub) of an execution of this workflow](https://github.com/thinhrick0101/ass2_SEP_group46/actions/runs/9670606918)
This workflow is ran on every commit on the Testing-branch and the main branch.

## Workflow 2: Static analysis (`static_analysis_1.yml`)

<Inform which tool is used to perform code quality check with static analysis.>
flake8 is the tool that was used. 
The flags I added in was to make flake8 return Python syntax errors, Issues with specific Python 3.x features, Issues with specific Python features, Undefined names in __all__.

This is the link to one log of an execution of the workflow: https://github.com/thinhrick0101/ass2_SEP_group46/actions/runs/9670703056/job/26679924349

## Workflow 3: Static analysis (`static_analysis_2.yml`)

pylint is a popular static code analysis tool for Python. It helps developers improve code quality by identifying programming errors, enforcing a coding standard, and offering simple refactoring suggestions.

This is the link of static_ analysis_2: 
https://github.com/thinhrick0101/ass2_SEP_group46/actions/runs/9670428376/job/26679116665

## Workflow 4: Release (`release.yml`)

This is the link of release.yml:
https://github.com/thinhrick0101/ass2_SEP_group46/actions/runs/9670585144/job/26679553754

## Statement of individual contributions

<Write what each group member did. Use the following table for that and add additional text under it if you see fit.>

| Member | Created workflows | Reviewed workflows | Merged pull requests' number |
| --- | --- | --- | --- |
| Nguyen Duc Thinh | static_analysis_2.yml | testing.yml, static_release_2.yml, release.yml | 3 |
| Phan Hoang Minh | testing.yml | static_release_1.yml, static_release_2.yml, release.yml | 4 |
| Hieu Nguyen Viet | static_analysis_1.yml |static_analysis_2.yml | 5 |
| Tuan An Hoang | release.yml | static_analysis_1.yml, static_analysis_2.yml, testing.yml | 6 |
