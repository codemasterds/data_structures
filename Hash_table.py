class Hash:

    def __init__(self):
        self.max=100
        self.arr=[[] for x in range(100)]
    
    
    def get_hash(self,key):
        hash_value=0
        count=0
        while count<len(key):
            hash_value=hash_value+ord(key[count])
            count=count+1
        return hash_value%self.max
    
    def __setitem__(self,key,val):
        hash_value=self.get_hash(str(key))
        found=False
        for idx, data in enumerate(self.arr[hash_value]):
            if (len(data)==2 and data[0]==key):
                    self.arr[hash_value][idx]= (key,val)
                    found=True
                    break
        if not found:
            self.arr[hash_value].append((key,val))


    def __getitem__(self,key):
        hash_val=self.get_hash(str(key))
        for x in self.arr[hash_val]:
            if x[0]==key:
                return x[1]
        #return self.arr[hash_val]

    def __delitem__(self,key):
            
            found=False
            hash_val=self.get_hash(key)
            for idx,data in enumerate(self.arr[hash_val]):
                if data[0]==key:

                    self.arr[hash_val].remove(data)
                    found=True
            
            if not found:
                print("key is not present")


# dict1=Hash()
# # print(dict1.add("dhoni",7))

# # #dict1.arr[7]
# # print(dict1.arr)
# # print(dict1.get("dhoni"))
# dict1["dhoni"]=7
# dict1["sachin"]=10
# dict1["sachin"]=11
# print(dict1["dhoni"])
# print(dict1["sachin"])
# del dict1["sachin"]
# del dict1["sachin"]
# print(dict1["sachin"])
# #print(dict1.arr)


