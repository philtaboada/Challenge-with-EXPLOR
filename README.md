## agents.py
This file contains the definition of custom agents.
To create a Agent, you need to define the following:
1. Role: The role of the agent.
2. Backstory: The backstory of the agent.
3. Goal: The goal of the agent.
4. Tools: The tools that the agent has access to (optional).
5. Allow Delegation: Whether the agent can delegate tasks to other agents(optional).

    [More Details about Agent](https://docs.crewai.com/concepts/agents).

## task.py
This file contains the definition of custom tasks.
To Create a task, you need to define the following :
1. description: A string that describes the task.
2. agent: An agent object that will be assigned to the task.
3. expected_output: The expected output of the task.

    [More Details about Task](https://docs.crewai.com/concepts/tasks).

## crew (main.py)
This is the main file that you will use to run your custom crew.
To create a Crew , you need to define Agent ,Task and following Parameters:
1. Agent: List of agents that you want to include in the crew.
2. Task: List of tasks that you want to include in the crew.
3. verbose: If True, print the output of each task.(default is False).
4. debug: If True, print the debug logs.(default is False).

    [More Details about Crew](https://docs.crewai.com/concepts/crew).

Developing Guidelines with Branch:
=====================================
Step 1: Open a folder of your choice name it project.
Step 2: Clone this repo by following the below steps.
    1. Find Current Directory in Windows
    In Windows, you can find the current working directory using:

    Command Prompt or PowerShell:
        cmd
        ``` bash
        echo %cd%
            or in powershell
        ```bash
        Get-Location
    2. Check If You’re in the Correct Git Repository
    Ensure you’re inside the directory where the repository was cloned:
    powershell
    Copy code
    cd C:\Users\Venks\Desktop\Project\Challenge_1
    git status
    If git status gives the error fatal: not a git repository, then the directory is not a Git repository.
    3. Verify Git Repository
    Check if the .git folder exists in C:\Users\Venks\Desktop\Project\Challenge_1:
    in powershell
    Copy code below
    dir -Force
    Look for a folder named .git.
    4. If the .git Folder is Missing
    This means the repository was not cloned properly, or you’re in the wrong directory. In that case:

Navigate to where the repository was cloned (likely eg: C:\Users\Venks\Desktop\Project).
Re-clone the repository if necessary:
powershell
Copy code below
    cd your project directory
        (eg:cd C:\Users\Venks\Desktop\Project)
        git clone https://github.com/philtaboada/Challenge-with-EXPLOR
    cd Challenge-with-EXPLOR
    5. Open Correct Directory in VS Code
        Use this command to open the correct folder in VS Code:
    powershell or cmd
    Copy code
    code .
The above step will open vs code installed in your pc



Steps to Troubleshoot
1. Check If the Directory Is a Git Repository
Run the following command in your terminal:

cmd
Copy code
git status
If the output is:
fatal: not a git repository (or any of the parent directories): .git
This means the .git folder is missing, and the directory is not a Git repository.
2. Check for .git Folder
Verify if the .git folder exists in the current directory:

cmd prompt
Copy code below
dir /a
If you do not see .git in the output, this directory is not initialized as a Git repository.
3. Re-Cloning the Repository
It’s possible that you navigated to the wrong directory or cloned incorrectly. To fix this:

Navigate to the parent folder:
cmd
Copy code
cd ..
Remove the problematic folder:
cmd
Copy code
rmdir /s /q Challenge_1
Re-clone the repository:
cmd
Copy code
git clone https://github.com/philtaboada/Challenge-with-EXPLOR
Move into the cloned directory:
cmd
Copy code
cd Challenge-with-EXPLOR
Check the Git status:
cmd
Copy code
git status
4. Open in VS Code
After confirming the directory is a Git repository, open it in VS Code:

cmd
Copy code
code .
In VS Code:

Check the bottom-left corner to see if it shows the branch name (e.g., main or feature/checking_features_built).
If it does, you are in the correct directory.
Additional Notes:
If you still face issues:

Ensure that Git is installed and available in your system's PATH.

Check by running:
cmd
Copy code
git --version
If it’s not installed, download and install Git from Git's official website.
Ensure the directory was cloned from GitHub and is not a manually copied folder.

Step 3: Create a new branch for your project using the following command in your terminal.

Directory and Branch:

The terminal shows git status with the output:
```bash
On branch main
Your branch is up to date with 'origin/main'.
```
This confirms you're in the Git repository and on the main branch.
Git Version:

The command git --version outputs 2.47.1.windows.1, confirming Git is installed and working.

What You Can Do Next
1. Create a New Branch
To work on a new feature or task:

```bash
git checkout -b feature/your-branch-name
```
Example:

```bash
git checkout -b feature/checking_features_built
```
This creates and switches to a new branch.

2. Make Changes
Use VS Code to edit files.
Save your changes.
3. Check the Status
To see what changes have been made:

```bash
git status
```
4. Stage and Commit Changes
Stage all the changes:
```bash
git add .
```
Commit with a message:
```bash
git commit -m "Added new feature to check built features"
```
5. Push the Branch to GitHub
Push your branch to the remote repository:

```bash
git push origin feature/checking_features_built
```
6. Create a Pull Request (PR)
Go to the GitHub repository in your browser.
You’ll see an option to create a pull request for your new branch.
Add a title, description, and assign reviewers if applicable.
Submit the pull request.


Developing Guidelines using poetry:
=====================================

First, install Poetry


```bash	
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Second, verify that it is installed

```bash
poetry --versión
```
(If you encounter an error, fix the issue or contact me)

Third, install the dependencies using

```bash
poetry install --no-root
```

Fourth, start the environment

```bash
poetry Shell
```

Fifth, run it

```bash
poetry run python main.py
```
