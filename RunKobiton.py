
import subprocess
from AmazonSesSample import EmailService
from KobitonConfig import test_files


for test_file in test_files:
    subprocess.check_call(['python',test_file])


