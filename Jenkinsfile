pipeline {
    agent { docker 'python:3.4.1' }
    stages {
        stage('build') {
            steps {
                bat 'python runtest.py'
            }
        }
    }
}