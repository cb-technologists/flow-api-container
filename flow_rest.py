import requests
import os

# Default to verifying SSL. This is needed because env vars show up as strings,
#  need to turn it into a bool.
if os.getenv("FLOW_VERIFY_SSL", True) == "False":
    verify_ssl = False
else:
    verify_ssl = True

payload = {
    "projectName": os.environ["FLOW_PROJECT_NAME"],
    "releaseName": os.environ["FLOW_RELEASE_NAME"],
}

requests.post(
    f"{os.environ['FLOW_URL']}/rest/v1.0/releases",
    auth=(os.environ['FLOW_USER'], os.environ['FLOW_PASSWORD']),
    params=payload,
    verify=verify_ssl
)
