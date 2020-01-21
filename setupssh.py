import sys
import subprocess

workerNodes = ['m-2', 'm-3', 'm-4']

allNodes = ['m-1', 'm-2', 'm-3', 'm-4']

masterIP = '10.1.2.93'

masterNode = 'm-1'

WorkersString = 'm-2,m-3,m-4'

nameofPemKEy = "cybera.pem" # Change to your own key.

def setupSSH():
    """
    sets up the ssh configs and hosts file and passwordless access.
    :return:
    """


    subprocess.call(["ssh-keygen -f ~/.ssh/id_rsa -t rsa -P '' "],shell=True)
    subprocess.call(["cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys"], shell=True)

    for node in workerNodes:

        print ("Working on Node: {}".format(node))
        #########
        subprocess.call(["cat ~/.ssh/id_rsa.pub | ssh {} 'cat >> ~/.ssh/authorized_keys'".format(node)],shell=True)
                #########
        subprocess.call(["scp ~/.ssh/config {}:~/.ssh/".format(node)],shell=True)

        subprocess.call(["scp ~/.ssh/{} {}:~/.ssh/".format(nameofPemKEy, node)], shell=True)
        subprocess.call(["sudo cp /etc/hosts ~"], shell=True)
        subprocess.call(["sudo chown ubuntu:ubuntu ~/hosts"],shell=True)
        subprocess.call(["scp ~/hosts {}:~".format(node)], shell=True)
        subprocess.call(["ssh {} 'sudo mv ~/hosts /etc/hosts' ".format(node)], shell=True)

print("Setting Up SSH")
setupSSH()
