from net import Net
#funciona sucuri, cloudflare exceto edlio e recaptcha se coloca dois f5
net = Net()
response = net.http_GET('https://www.co.portage.wi.us/about-us/advanced-components/list-detail-pages/rfp-posts-list')
print (response.content)