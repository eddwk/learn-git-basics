# learn-git-basics
This repository is to teach the basics of a couple of fundamental concepts to a friend who is thinking about entering into the field of software development.
1. Git workflow Basics
    - The goal is to teach a new developer how to clone down a repository, create a branch, make a commit to the branch, and merge those changes back into master through a pull request on github.
2. The most primitive form of Test Driven Development.
    - The goal here is that the new developer can pull down a repository, run a failing test suite, and follow the errors all the way to a working fizzbuzz.
3. A simple format for solving other problems using python to develop programming chops. This repo or others like it could be used to solve other problems like a building a linked list, reversing a string, or whatever else you might want to do.

Instructions for use:
1. Clone the repository using the following instructions: https://help.github.com/en/articles/cloning-a-repository
2. `cd learn-git-basics`
3. Install the dependencies from the root with `pip install -r requirements.txt`
4. Run the test suite with `pytest`

Before you begin your work, you should create a new branch: `git checkout -b [your branch name]` and do all of the work on a new branch.

Once you have finished the work:

1. Review all of your changes using `git diff`. Make sure that the formatting is clean and that there aren't any mispelled words or typos.
2. Stage your changes to be committed with `git add [file_name]` or `git add .` if you want to commit all of your changes.
3. Commit your changes with `git commit -m 'fix fizzbuzz tests'`
4. Push the changes to github with `git branch --set-upstream origin [your branch name]` and open a pull request to be reviewed.
