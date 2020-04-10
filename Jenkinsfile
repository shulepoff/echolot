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
	sh "docker stop echolot"
        sh "docker run -d --rm --name echolot -p 8000:8000 echolot"
    }
}
