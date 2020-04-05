node {
      stage('Clone sources') {
	git url:'https://github.com/shulepoff/echolot.git'
      }
      stage('install') {
        sh """
	  python3 -m venv env
	  . ./env/bin/activate
          pip3 install -r requirements.txt
	  """
     }
}
