pipeline {
    agent any
    stages {
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shivalikag17/flaskdemo.git'
            }
        }
        stage('Docker image build') {
            steps {
                sh '/usr/bin/docker image build -t shivalika17/flask-demo-image .'
            }
        }
        stage('Docker login') {
            steps {
                sh 'echo dckr_pat_upZWFBxtIVqnMkB8ye5LnrBfY1g | /usr/bin/docker login -u shivalika17 --password-stdin'
          }
        }
        stage('COnfirmation') {
            steps{
                input 'Do you wanna Deploy it?'
            }
        }
        stage('Service remove') {
            steps {
                sh '/usr/bin/docker service rm servicedemo'
            }
        }
        stage('Service create') {
            steps {
                sh '/usr/bin/docker service create --name servicedemo -p 3000:3000 --replicas 2 shivalika17/flask-demo-image'
            }
        }
    }
}
