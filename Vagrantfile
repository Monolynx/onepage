# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 3306, host: 3300
#  config.vm.network "private_network", type: "dhcp"
  config.vm.network "private_network", ip: "33.33.33.20"

  

  config.vm.synced_folder ".", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = false
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end

  config.vm.provision :shell, path: "vagrant/bootstrap.sh", privileged: false
  config.vm.provision :shell, path: "vagrant/bootstrap/mysql.sh", privileged: true
  config.vm.provision :shell, path: "vagrant/bootstrap/app.sh", privileged: true

#  config.vm.provision :shell, path: "vagrant/bootstrap/install-git-hooks.sh", privileged: false

  # in this version i have problem with sourcing virtualenvwrapper neede to create virtualenv etc.
  # config.vm.provision :shell, path: "vagrant/bootstrap/prepare-os.sh", privileged: true
  # config.vm.provision :shell, path: "vagrant/bootstrap/virtualenvwrapper.sh", privileged: false
  # config.vm.provision :shell, path: "vagrant/bootstrap/nodejs.sh", privileged: true
  # config.vm.provision :shell, path: "vagrant/bootstrap/gulpphantomjs.sh", privileged: true
  # config.vm.provision :shell, path: "vagrant/bootstrap/mkproject.sh", privileged: false
  # config.vm.provision :shell, path: "vagrant/bootstrap/npmrequirements.sh", privileged: false
  # config.vm.provision :shell, path: "vagrant/bootstrap/pillow-dependencies.sh", privileged: true
  # config.vm.provision :shell, path: "vagrant/bootstrap/piprequirements.sh", privileged: false
  # config.vm.provision :shell, path: "vagrant/bootstrap/supervisor.sh", privileged: true

  config.vm.provision "Success", type: "shell", inline: <<SCRIPT
    echo
    echo
    echo
    echo
    echo "Congratulations! You've just successfully set up Reporta project!"
    echo
    echo "Ignore all red error messages above. If you see this it means all is ok."
    echo
    echo "You can go to http://localhost:8000 to see Reporta website."
    echo
    date > /etc/vagrant_provisioned_at
SCRIPT
end
