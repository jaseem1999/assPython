class vehicle:
    vic ={'marudi':'alto','banz':'c class'}
    print(vic)
    def displayKey(self):
        print(self.vic.keys())
    def insert(self):
        self.vic[input("Enter the company name")] = input("Enter the brand")
        print(self.vic)
    def delete(self):
        del self.vic[input("Enter the deletting company name")]
        print(self.vic)
    def search(self):
        s = input("Enter search ::  ")
        if s in self.vic:
            print("found")
        else:
            print("Not")
obj = vehicle()
obj.displayKey()
obj.insert()
obj.delete()
obj.search()
