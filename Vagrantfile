# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|

  config.vm.box = "centos64"
  config.vm.box_url = "http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130427.box"

  config.vm.forward_port 8000, 8000
  config.vm.share_folder "project", "/home/vagrant/gedgo_env", "./", :nfs => true

  config.vm.network :hostonly, "192.168.33.33"
  
  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet"
    puppet.manifest_file  = "manifest.pp"
  end
end
