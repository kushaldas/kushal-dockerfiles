
sudo docker run -it -e TERM -u $(id -u):$(id -g)     -v $HOME/.irssi:/home/kdas/.irssi:ro     -v $HOME/irclogs:/home/kdas/irclogs     -v /etc/localtime:/etc/localtime:ro     kushal/irssi
