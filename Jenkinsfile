pipeline {
    agent { 
        docker { 
           image 'python:buster'
	   args '--network host'
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
    }
}
