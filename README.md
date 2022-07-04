# Frame Work Setup #
<br>This is a BDD framework build on top of behave https://behave.readthedocs.io/en/latest/index.html </br>
<br>Project uses Gherkin format https://cucumber.io/docs/gherkin </br>

Project structure
```bash
├── AllureReports       - For reporting 
├── requirements.txt    - Contain all dependancies
├── features            - BDD framework files
|  ├── environment.py   - BDD Hooks
|  ├── steps            - BDD steps for the tests
|  └── tests            - BDD features [test cases] included here
├── resources
|  ├── ApiResources.py  - Contains api sub enpoints
|  ├── Payloads.py      - Uses for dyanamic pay load generations
|  └── properties.ini   - Test properties such as endpoints tokens
├── utils
|  ├── Configurations.py - Accessing properties file
|  ├── GistsApiUtil.py   - All api related functions resides here
```

## Pre prerequisites ##
Install  python latest version https://www.python.org/downloads/

Use an editor that supports gherkin feature file.Use pycharm enteprise edition.
```
python --version
```

**Project set up**
<br>Clone the project from the repo</br>
<br>Open the project from the editor pycharm enterprise edition</br>
<br>Go to terminal and install all required dependencies using requirements.txt </br>
<br>Most of the time pycharm will install the dependencies automatically</br>
```
pip install -r requirements.txt
```
<br> Open the properties.ini file and provide your git user id,you can pass the token via command line or include in properties.ini file</br>
<br>if you already python installed select or create new virtual environment freshly install all dependencies </br>
<br>More about virtual env https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ </br>

### important dependencies used ###
<br>For api requests used  https://requests.readthedocs.io/en/latest/ </br>
<br>For behave https://behave.readthedocs.io/en/stable/ </br>
<br>For reporting used allure report https://docs.qameta.io/allure/ </br>

## Execute the tests ##
* To execute the tests on GistsBasicApi.feature provide your username in feature file
1. Execute all the test cases:
* navigate to project root folder
* Generate your token from git
* Parametrize the token command
```
behave features/tests/*.feature --no-capture -D token=<token>
```
* You can provide the token in the properties.ini file

* If you are providing in properties file you can use the following command
```
behave features/tests/*.feature --no-capture
```
2. Execute  the test cases by specific file name :
```
behave features/tests/GistsApiE2E.feature --no-capture -D token=<token>
```
```
behave features/tests/GistsBasicApi.feature --no-capture -D token=<token>
```
3. Execute the test using behave scenario tags
```
 behave features/tests/*.feature --no-capture -D token=<token> --tags=smoke
```
```
 behave features/tests/GistsBasicApi.feature --no-capture -D token=<token> --tags=smoke
```
4. Generating the allure report for your execution:
* install allure_behave for reporting purpose,allready included in requirments.txt
```
pip install allure-behave
```
* Execute the below command it will generate the folder called AllureReport in the root of your project, You can have any folder name.
* This will generate few json files in the folder.
```
behave features/tests/GistsBasicApi.feature --no-capture -D token=ghp_FLh3Fx0jFIY6p5Fo2B241gFJQnPdhDC3PfG7c  -f allure_behave.formatter:AllureFormatter -o AllureReports
```
* For generating the report using the json install the following
```
brew install allure || npm install -g allure-commandline
```
```
allure --version
```
* Let's generate the html report, navigate the allure report folder and execute
*  for more details https://docs.qameta.io/allure/
```
mac : allure serve AllureReports
```