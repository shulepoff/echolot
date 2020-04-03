pipeline {
    agent { 
        docker { 
           image 'python:3.7.2'
	   args '--network=host'
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
        steps {
	  sh """
	  . ./env/bin/activate
	  gunicorn -b :8000 foobar:app
	  """
        }
      }
    }
}
