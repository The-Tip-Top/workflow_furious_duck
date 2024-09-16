import jenkins.model.*
import hudson.security.*

def instance = Jenkins.getInstance()
def crumbIssuer = instance.getCrumbIssuer()

# Réinitialiser la protection CSRF
if (crumbIssuer != null) {
    def crumbIssuerClass = crumbIssuer.getClass()
    def crumbIssuerConstructor = crumbIssuerClass.getConstructor(boolean)
    def newCrumbIssuer = crumbIssuerConstructor.newInstance(true)
    instance.setCrumbIssuer(newCrumbIssuer)
}

instance.save()


#kubectl --kubeconfig kubeconfig.yml exec -it jenkins-0 -- /bin/bash
#Defaulted container "jenkins" out of: jenkins, fix-permissions (init)
#jenkins@jenkins-0:/$ ls
#bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
#jenkins@jenkins-0:/$ ls -l /var/run/docker.sock
#srw-rw---- 1 root systemd-journal 0 Sep 14 09:17 /var/run/docker.sock
#jenkins@jenkins-0:/$ sudo chown root:docker /var/run/docker.sock
#jenkins@jenkins-0:/$ sudo chown 660 /var/run/docker.sock
#jenkins@jenkins-0:/$
