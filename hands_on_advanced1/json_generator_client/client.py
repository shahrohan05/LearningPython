import httplib2
import json
import sys,traceback

class Client:
    def __init__(self):
        self.urls_url = "http://localhost:5000/json_gen/urls"
        self.urls = []
        self.foldername = "data"
        self.http = httplib2.Http(".cache")

    def get_urls(self):
        try:

            print("attempting to get from {}".format(self.urls_url))
            (resp, content) = self.http.request(self.urls_url, "GET")
            self.urls = json.loads(content)
            print("Urls fetched successfully.")
            #print(self.urls)
        except Exception as ex:
            print("Error retrieving data!",ex)

    def fetch_data(self):
        print("Attempting to fetch json data for all the urls and loading into files in the 'data' folder.")
        print("This can take a while, please wait.")
        try:
            if len(self.urls) < 1:
                print("Nothing to fetch!")
                return
            counter = 1
            for url in self.urls:
                (resp, content) = self.http.request(url, "GET")
                file_data = content.decode("utf-8").split("\n")
                if len(file_data) == 2:
                    filename = file_data[0]
                    data = file_data[1]
                    file = open(self.foldername+"/"+filename,"w")
                    file.write(data)
                    file.close()
                else:
                    print("Error, could not processed response for : {}".format(url))
                counter += 1
                if counter%100==0:
                    print("# of files loaded : {}".format(counter))

            print("Done loading all {} files!".format(counter))
        except:
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)





if __name__ == "__main__":
    client = Client()
    client.get_urls()
    client.fetch_data()
    # successfully ran and tested/
    # Loaded 1007 files in about 35 minutes over the network without crashing the program on either client/server side.