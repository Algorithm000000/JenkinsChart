
pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                echo 'Building..'
				Cygwin 'python -u runtest.py'
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