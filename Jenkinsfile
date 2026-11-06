pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out GitHub project'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running Python unit tests'
                sh 'python3 -m unittest -v'
            }
        }

    }

    post {
        success {
            echo 'SUCCESS: All Python tests passed!'
        }

        failure {
            echo 'FAILURE: Python tests did not pass!'
        }

        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}