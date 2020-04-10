node {
    stage('Clone source'){
        git branch: 'master',
            url:'https://github.com/shulepoff/echolot.git'
    }
    stage('Test'){
        sh "pylint3 foobar.py"
    }
    stage('Build'){
        sh "docker build -t echolot ."
    }
    stage('Run Docker'){
	sh 'if [ "$(docker ps -f name=echolot -q)" ]; then docker stop echolot ; fi'
        sh 'docker run -d --rm --name echolot -p 8000:8000 echolot'
    }
}
