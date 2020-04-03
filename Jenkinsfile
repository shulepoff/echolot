pipeline {
    agent { 
        docker { 
           image 'python:3.7.2'
        }
    }
    stages {
      stage('install') {
        steps {
	  sh """
	  python3 -m venv env
	  . ./env/bin/activate
          pip3 install -r requirements.txt
	  """
        }
      }
      stage('run') {
	steps{
	 sh """
	 . ./env/bin/activate
	 gunicorn -b :8000 foobar:app
	 """
	}
      }
    }
}
