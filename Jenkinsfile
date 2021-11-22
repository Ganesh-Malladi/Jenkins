pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Ganesh-Malladi/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x SE_jenkins.py"
                sh "./SE_jenkins.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
