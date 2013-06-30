snort_sid_registry
==================

SNORT sid registry

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
A: No, but this is so far the only registry I've found.

Q: What does it apply to?
A: It applies to both SNORT sid and Suricata sid, 
basically, any system which accept rules compatible with these
systems.

