# FROM jenkins/jenkins:lts

# USER root


# RUN apt-get update && apt-get install -y \
#     docker.io \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# RUN mkdir -p /var/lib/apt/lists/partial && \
#     chown -R 1000:1000 /var/jenkins_home && \
#     chmod -R 755 /var/jenkins_home

# RUN if ! getent group docker > /dev/null; then \
#         groupadd docker; \
#     fi


# RUN usermod -aG docker jenkins


# Use Jenkins base image
FROM jenkins/jenkins:latest

# nous devons utiliser le root pour nous permettre d'avoir les permissions
USER root

# installer les tools necessaires 
RUN apt-get update && \
    apt-get install -y sudo vim curl wget


# on met un password car si non on ne peut pas trouver le password de root
RUN echo 'root:abc123' | chpasswd

# mettre jenkins comme sudoeur 
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# installer docker cli
RUN apt-get update && \
    apt-get install -y apt-transport-https \
                       ca-certificates \
                       gnupg2 \
                       software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli

# on crée un groupe docker 
RUN groupadd docker

# on ajout jenkins au groupe docker pour pouvoir éxécuter les commande 
RUN usermod -aG docker jenkins

# revenir au user jenkins 
USER jenkins