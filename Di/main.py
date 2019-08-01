from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "domain": "diexample.gmail.com",
        "email" : "YOUR EMAIL ADDRESS",
        "password": " YOUR PASSWORD",
    })
    email_reader = Readers.email_reader()
    print email_reader.read()