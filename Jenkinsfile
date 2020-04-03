pipeline {
    agent { 
        docker { 
           image 'python:3.7.2'
        }
    }
    stages {
      stage('install') {
        steps {
	  sh 'python3 -m venv env'
	  sh 'source env/bin/activate'
          sh 'pip3 install -r requirements.txt'
        }
      }
      stage('run') {
	steps{
	 sh 'gunicorn -b :8000 foobar:app 
	}
      }
    }
}
