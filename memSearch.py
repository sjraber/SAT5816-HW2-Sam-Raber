import os

file = input("which file would you like to search through?\n")
print(file)
print("would you like to search profile information, search pid, search process tree used by an application, search network connection used by application, or search command execution?(profile, pid, process, net, or command)")
input1 = input()

match input1:
	case "profile":
		inputProfile = input("input profile to search(example: Win7SP1x86_23418)\n")
		os.system("python2 vol.py -f "+file+" --profile="+inputProfile+" printkey")
	case "pid":
		inputPid = input("input a pid to search(example: 2388)\n")
		os.system("python2 vol.py -f "+file+" --profile=Win7SP1x86_23418 pslist -p "+inputPid)
	case "process":
		inputProc = input("input a process to search(example: chrome.exe)\n")
		os.system("python2 vol.py -f "+file+" --profile=Win7SP1x86_23418 pstree | grep "+inputProc)
	case "net":
		inputNet = input("input an ip address to check for activity(example: 111.111.1.1)\n")
		os.system("python2 vol.py -f "+file+" --profile=Win7SP1x86_23418 netscan | grep "+inputNet)
	case "command":
		inputCmd = input("input a command to search for(example: echo)\n")
		os.system("python2 vol.py -f "+file+" --profile=Win7SP1x86_23418 cmdscan | grep "+inputCmd)
