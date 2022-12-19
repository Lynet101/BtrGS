#!/bin/sh
#Sebastian Lindau-Skands© 2022
#@lynet_101


#Easy GPU management for hybrid graphic setups | daemon
path=./src
echo '(I)nstall or (U)ninstall?'
read act

if [ $act = 'I' ]
then
	echo 'Installing ui'
	cp $path/fun-ui /usr/bin/fun
	mkdir /etc/fun
	echo 'Installing switcher'
	cp $path/fun-daemon-script /etc/fun/fun-daemon-script
	echo 'Installing daemon'
	cp $path/fun-openrc-daemon /etc/init.d/fund
	echo 'Setting permissions'
	chmod +x /usr/bin/fun
	chmod +x /etc/fun/fun-daemon-script
	chmod +x /etc/init.d/fund
	echo 'Done'
	act=""
fi

if [ $act = 'U' ]
then
	echo 'Uninstalling...'
	rm /usr/bin/fun
	rm -r /etc/fun
	rm /etc/init.d/fund
	echo 'Done'
	act=""
fi

if [ $act ]
then
	echo "Invallid option | Type 'I' to install or 'U' to uninstall"
fi
