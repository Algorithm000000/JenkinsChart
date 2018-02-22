
pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                echo 'Building..'
				sh 'python -u runtest.py'
            }
        }
		
		stage('Test') {
			steps {
				echo 'Testing..'
			}
		}
		
		stage('Deploy') {
			steps {
				echo 'Deploying..'
			}
		}
    }
}