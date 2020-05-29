import httplib2
import sys
from urllib.parse import urlencode
import json


# test_phishing_url = "http://www.travelswitchfly.com/"

def check_phishing(url):
    try:
        http = httplib2.Http(".cache")
        data = {"url": url, "format": "json"}
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        (resp, content) = http.request("https://checkurl.phishtank.com/checkurl/", "POST", headers=headers,
                                       body=urlencode(data))
        json_resp = json.loads(content)
        # print(json_resp)
        result = json_resp["results"]
        if "valid" in result.keys():
            print("Provided url is {} url".format("a phishing" if result["valid"] else "not a phishing"))
            print("Find more info at : {}".format(result["phish_detail_page"]))
        else:
            print("Error retrieving the status of the provided url.")
    except Exception as e:
        print("Error retrieving the status of the provided url.", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Url: ")

    check_phishing(url)
