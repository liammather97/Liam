
pipeline{
        agent any
        stages{ 
		    stage('Test-Run'){
                        steps{
                            sh "tests/count_test.py"
                        }
                }
        }
}