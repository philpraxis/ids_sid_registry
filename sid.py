sid_registry = []

sid_registry.append({
"start":1,
"stop": 100,
"description":"Reserved for future use",
"contact":"research@sourcefire.com",
"lookup":"http://www.snort.org/search/sid/",
})

sid_registry.append({
"start":101,
"stop": 1000000,
"description":"SourceFire rules",
"contact":"research@sourcefire.com",
"lookup":"http://www.snort.org/search/sid/",
})

sid_registry.append({
"start":1000000,
"stop": 2000000,
"description":"snort community rule",
"contact":"nobody, that's the problem!",
"lookup":"",
})

sid_registry.append({
"start":2000000,
"stop": 3000000,
"description":"emergingthreats.net",
"contact":"emerging@emergingthreats.net",
"lookup":"http://doc.emergingthreats.net/bin/view/Main/",
})

sid_registry.append({
"start":6000000,
"stop": 7000000,
"description":"Berkeley SNS security custom rules",
"contact":"security@berkeley.edu",
"lookup":"",
})

# 7xx0000 - 7xx9999 prefixes are organization specific
# pick-up the 2 digit code you want and attribute it to your organization
# if you plan to be issueing quite a lot of rules
sid_registry.append({
"start":7010000,
"stop": 7019999,
"description":"TCERT (Telecom CERT) sid prefix",
"contact":"contact@tcert.org",
"lookup":"",
})

sid_registry.append({
"start":7150000,
"stop": 7159999,
"description":"P1 Security sid prefix",
"contact":"contact@p1sec.com",
"lookup":"http://saas.p1sec.com/vuln/sid/",
})


# # Duplicate this below and uncomment it to use it as a template for your range:

# sid_registry.append({
# "start":,
# "stop":,
# "description":"",
# "contact":"XXX@XXX.com",
# "lookup":"http://XXX",
# })

