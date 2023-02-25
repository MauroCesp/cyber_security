import dns
import dns.resolver
ansA,ansMX,ansNS,ansAAAA=(dns.resolver.query('google.com','A'),dns.resolver.query('google.com','MX'),dns.resolver.query('google.com', 'NS'), dns.resolver.query('google.com', 'AAAA'))
print(ansA.response.to_text())
print(ansMX.response.to_text())
print(ansNS.response.to_text())
print(ansAAAA.response.to_text())