# CloudBees Flow API-calling container

This container can be used any place you want to make a REST API call to Flow. 

Currently it only has a post call to Flow, but as more use cases are found, additional calls can easily be added and we could use a flag to determine which call to perform.

## How to use

You'll need to define some environment variables before running the container:

Variable | Value | Details
--- | --- | ---
FLOW_VERIFY_SSL | True/False | Defaults to True. If your Flow server has certs setup, stick with True. Otherwise you'll need to set to False to disable SSL verification.
FLOW_URL | String | This is the URL for your Flow server. This shouldn't include the rest endpoint.
FLOW_USER | String | Your Flow username
FLOW_PASSWORD | String | Your Flow password. If you're running in Kubernetes, you'll want to store this in Vault or another password store.
FLOW_PROJECT_NAME | String | The name of your Flow project. This can include spaces.
FLOW_RELEASE_NAME | String | The name of your Flow release. This can include spaces.
