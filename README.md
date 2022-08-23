# Python Selenium Framework (UI Automation)
## Overview
This solution has been designed to test web application https://weathershopper.pythonanywhere.com/ using Selenium with Python. In the interest of time and having hands-on expertise, I have selected Python as the Programming language. In this challenge, my focus was on designing the scalable solution so that more test cases can be added in future with minimal amount of development efforts.
1.	Solution supports running tests against Chrome and Firefox
2.	Solution supports Parallel Test execution
3.	Solution is properly structured as per standard Python Test structure
## Installation
1.	Download and Install PyCharm
2.	Download and Install Python. While installing python you make sure that python is added to System’s env variables (Setup will give you option to choose)
3.	Once done please execute the following commands one by one to install the required packages:
    * **pip install pytest-bdd**
    * **pip install pytest**
    * **pip install pytest-xdist**
    * **pip install Selenium**
4.	Download Chrome and Gecko drivers for compatible versions of browsers installed on the system where tests will be executed. (I have already pushed these two drivers in repo but just in case they are not compatible with your browser versions you’d have to download them separately)
## Frameworks/Tools/Patterns used
1.	Language: Python
2.	Driver: Selenium WebDriver - Web framework that permits you to execute cross-browser tests
3.	Framework: Cucumber, Pytest-BDD - Behavior-Driven (BDD) test framework to enable automating project requirements testing and to facilitate behavioral driven development
4.	Test runner: Pytest with pytest-xdist - It is a testing framework that helps you to write simple and scalable test cases for databases, APIs, or UI. It also allows you to run tests in Parallel
5.	IDE: PyCharm
6.	Design Pattern: Page Object Model - To reducing duplication and minimization of the efforts involved in code maintenance, increase reusability, makes code more modular
## Setup Test Environment
1.	Clone the Repository https://github.com/MuhammadWaleed14/Python_Selenium_Framework
2.	Checkout branch if isn’t already checked out.
3.  Now replace your browser driver executable files in /browsers directory (if required)
## Run Tests in Different Browsers
1.	Go to config.json file on root of project.
2.	Against key **browser** you can:
    *	Set value to **chrome** to run against Chrome
    *	Set value to **firefox** to run against FireFox
         * If you select Firefox, make sure that in config.json against key **firefox_binary** you also specify the path of executable binary for firefox which would be firefox.exe file at the install directory of Firefox on your computer. On windows it would generally be "C:/Program Files/Mozilla Firefox/firefox.exe" and this is already set in the config file but you can change it if your path is different.
**Note: Please note that firefox_binary is not geckodriver so don’t confuse between these two, geckodriver would be picked automatically from /browsers folder**
3.  Once you are done with setting up the code. It’s time to invoke pytest and execute the test
## Execute Tests from PyCharm
1. Set **Python Interpreter** in PyCharm
2.	To run tests in PyCharm:
     * Click on **Add Configuration** option
     * Click on **+** icon to create new configuration
     * Select **Python tests** > **Pytest**
     * Set **Working Directory** path to Tests Folder
     * Set **Target** path to test case file
     * Click on the **Apply** button
3.	Click on **Run** button
## Execute Tests from CMD
1. To run test you need to run this command in the CMD:
   * Example:
       * python -m pytest C:/Python_Selenium_Framework/tests
   * **Note you can also provide relative path to pytest depending on where in directory you’re CMD is scoping**
## Parallel Test Execution
Pytest supports parallel execution of tests. 
1. You need to run:
   * python -m pytest <path of /tests folder> -n 2
      * Where -n parameter is number of parallel executions/threads you want
      * This command will launch tests in two different browser windows



