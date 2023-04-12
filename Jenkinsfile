pipeline{
    agent any

    stages{
        stage("Clear Workspace"){
            steps{
                deleteDir{}
            }
        }

        stage("CLone Repository"){
            steps{
                sh "git clone "
            }
        }

        stage("Install packages"){
            steps{
                dir("calculator"){
                    sh "npm install"
                }
            }
        }

        stage("Test before build"){
            steps{
                dir("calculator"){
                    sh "run test -- -- watchAll=false"
                }
            }
        }

        stage("Build App"){
            steps{
                dir("calculator"){
                    sh "npm run build"
                }
            }
        }
    }
}
