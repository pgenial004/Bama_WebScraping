from net import Net

net = Net()
response = net.http_GET('https://www.cvsd.org/apps/pages/Bids')
print (response.content)