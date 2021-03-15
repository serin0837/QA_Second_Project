pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh '''
                    cd service2
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service3
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service4
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    '''
                }
            }
        stage('Ansible'){
            steps{
                sh ''' 
                cd ansible
                ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
                ansible-playbook -i inventory.yaml playbook.yaml
                '''
            }
        }
        stage('Build'){
            steps{
                sh ''' 
                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u serin0837 -p password1234
                sudo docker-compose push
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@35.197.49.49:/home/jenkins/docker-compose.yaml
                ssh -i ~/.ssh/id_rsa jenkins@35.197.49.49 << EOF
                docker stack deploy --compose-file /home/jenkins/docker-compose.yaml travel-generator << EOF
                '''
            }
        }          
    }
}