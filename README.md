# covid_expert_system
COVID-19 Diagnosis Expert System build on Python and Prolog.

Firstly, try following the instructions here: https://github.com/yuce/pyswip/blob/master/INSTALL.md 

If the above fails, use these instructions to install:
1. Clone the repo: `git clone https://github.com/nikita-kotsehub/covid_expert_system.git`
2. Navigate here and install the appropriate version of SWI-Prolog: https://www.swi-prolog.org/Download.html 
3. Once inside VS Code (or other IDE), create a virtual environment: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ 
4. Install dependencies: `pip install -r requirements.txt`
5. Run `pip install git+https://github.com/yuce/pyswip@master#egg=pyswip` to install the latest version of PySWIP
6. If you experience issues running the programs, create a .env file in the main directory and add `SWI_HOME_DIR=C:\\Program Files\\swipl`, or another path to where your swipl is stored.
7. If you have windows and face issues, this video might help: https://www.youtube.com/watch?v=oJVXMv2TIoU 
8. Finally, run `cd expert` and then `python expert.py` to run the main expert system.
