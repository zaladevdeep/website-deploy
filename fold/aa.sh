new_cron_command='@reboot sudo systemctl start codedeploy-agent\nHello my name is devdeep' 

# Create temporary file
echo -e "$new_cron_command" > /tmp/my_crontab

# Overwrite crontab (use sudo only if necessary)
sudo crontab /tmp/my_crontab

# Clean up
rm /tmp/my_crontab