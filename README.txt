ids_sid_registry
================

IDS sid registry for Suricata, SNORT, and any other compatible IDS

Q: How to add a new range for your private rules?
A: Fork the repository on github: 
	https://github.com/philpraxis/ids_sid_registry/fork
Make your changes in sid.py:
	vi sid.py
Commit them and push them to github:
	git commit -a
	git push origin master
Send us a pull request:
	https://github.com/philpraxis/ids_sid_registry

Q: Is this official?
A: No, but so far I've found no registry. 
This one is open and collaborative. IANA style.
Reserve your sid range, work in it with peace :)

Q: What does it apply to?
A: It applies to both SNORT sid and Suricata sid, 
basically, any system which accept rules compatible with these
systems.

Q: Why store this in python file?
A: So that it can be used easily in some tools which needs such data.
That's true that quite a lot of SNORT tools is in PERL, but hey, 
contribute, code some PERL that will treat the sid.py file as a data
file to provide the same.

Q: Can i import this in my python script?
A: Yes, just clone this repo within your code directory
and add in your code or test the following:
import ids_sid_registry
print ids_sid_registry.sid.sid_registry
