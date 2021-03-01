pipeline {
    agent any 
    stages{

        stage('Test'){
            steps{
                sh '''
                cd ./service1
                pip3 install -r requirements.txt
                pytest --cov=app --cov-report
                cd ..
                # test service2
                cd ./service2
                pytest --cov=app --cov-report
                cd ..
                # test service3
                cd ./service-3
                pytest --cov=app --cov-report
                cd ..
                # test service4
                cd ./service-4
                pytest --cov=app --cov-report
                cd ..
                '''
            }
        }
        stage('Build'){
            steps{
                sh ''' sudo chmod 666 /var/run/docker.sock
                docker-compose down --rmi all
                docker-compose build
                sudo docker login
                sudo docker-compose push
                '''
            }
        }
        // stage("Ansible"){
        //     steps{
        //         sh '''
        //             *
        //             cd ansible
        //             chmod 666 inventory.yaml playbook.yaml
        //             ls -la
        //             ansible-playbook -i inventory.yaml playbook.yaml
        //             '''     
        //     }
        // }
        stage('Deploy'){
            steps{
                sh '''
                    pwd
                    ls -la
                    scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml
                    ssh -i ~/.ssh/id_rsa jenkins@manager
                    cd /
                    cd home/jenkins
                    ls -la
                    docker stack deploy --compose-file docker-compose.yaml restaurant-gen
                    '''
            }
        }                   
    }
}