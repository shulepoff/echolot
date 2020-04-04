pipeline {
    stages {
      stage('Clone sources') {
	      steps {
	 	git url:'https://github.com/shulepoff/echolot.git'
	      }
      }
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
