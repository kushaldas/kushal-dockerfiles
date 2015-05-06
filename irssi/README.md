## First add a SELinux rule

chcon -Rt svirt_sandbox_file_t /home/kdas/irclogs

## How to run the container?
sudo docker run -it -e TERM -u $(id -u):$(id -g)     -v /home/kdas/.irssi:/home/kdas/.irssi:ro     -v /home/kdas/irclogs:/home/kdas/irclogs     -v /etc/localtime:/etc/localtime     kushal/irssi
