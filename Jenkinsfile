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
                sh "chmod u+x SE_Jenkins.py"
                sh "./SE_Jenkins.py"
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
