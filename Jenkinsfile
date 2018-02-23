
pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                echo 'Building..'
				bat 'python -u CreateChart.py'
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