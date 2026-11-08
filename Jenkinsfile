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
}