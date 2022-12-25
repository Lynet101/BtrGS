from os import system as call

def main():
    func=installer()
    action=input('(I)nstall or (U)ninstall?\n')
    if action == 'I':
        func.install()
    elif action == 'U':
        func.uninstall()
    elif action == 'Ri':
        func.reinstall() #Debug feature
    else:
        print('Invalid option!')
    
class installer():
    def __init__(self):
        self.primdir='/etc/BtrHGS'
        self.bindir='/usr/bin'
        self.daemondir='/etc/init.d'
        self.backend='BtrHGS_backend.py'
        self.frontend='BtrHGS_frontend.py'
        self.cmd='BtrHGS_command.sh'
        self.daemon='BtrHGS_daemon.sh'
        self.conf='config.py'
    
    def install(self):
        print('installing')
        call(f'mkdir {self.primdir}')
        call(f'cp {self.backend} {self.primdir}')
        call(f'cp {self.frontend} {self.primdir}')
        call(f'cp {self.cmd} {self.bindir}/btrhgs')
        call(f'cp {self.daemon} {self.daemondir}/btrhgsd')
        call(f'cp {self.conf} {self.primdir}')
        call(f'cp -r X/* /etc/')
        call(f'touch {self.primdir}/to_exe')
        print('done')

    def uninstall(self):
        print('removing')
        call(f'rm -r {self.primdir}')
        call(f'rm -r {self.bindir}/btrhgs')
        call(f'rm -r {self.daemondir}/btrhgsd')
        call(f'rm -r /etc/X11.nvi /etc/X11.inte /etc/X11.hyb')
        print('done')

    def reinstall(self):
        self.uninstall()
        self.install()

if __name__ == '__main__':
    main()
        
