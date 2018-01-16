#This is a solution based on Stefan Prodan blog, the author of the entire repo (under MIT license)
#source: https://stefanprodan.com/2016/a-monitoring-solution-for-docker-hosts-containers-and-containerized-services/

git clone https://github.com/stefanprodan/dockprom
cd dockprom

ADMIN_USER=admin ADMIN_PASSWORD=admin docker-compose up -d