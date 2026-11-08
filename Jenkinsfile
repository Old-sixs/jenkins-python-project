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
                sh 'python3 -m unittest -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All Python tests passed!'

            withCredentials([
                string(credentialsId: 'webex-bot-token',
                       variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'webex-room-id',
                       variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''
                    set +x
                    python3 webex_notify.py SUCCESS
                '''
            }
        }

        failure {
            echo 'FAILURE: Jenkins build failed!'

            withCredentials([
                string(credentialsId: 'webex-bot-token',
                       variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'webex-room-id',
                       variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''
                    set +x
                    python3 webex_notify.py FAILURE
                '''
            }
        }

        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}