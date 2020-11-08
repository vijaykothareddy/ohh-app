echo '''*****************************************************
        Assuming the Git and Virtualenv are installed, if not
        sudo apt install git
	apt install virtualenv 
	please rerun the script post installing above packages
	******************************************************
	'''
echo ''' cloning the app repo from Git '''

Git clone https://github.com/vijaykothareddy/ohh-app

echo ''' creating virtual environment '''

virtualenv -p `which python3` venv

echo ''' activating the virtual environment '''

source venv/bin/activate

echo ''' installing Flask module '''

pip install flask

echo ''' please export you application python file as below
         export FLASK_APP=application.py
	 run application: falsh run '''

