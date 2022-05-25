class Node:

    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    
    def __init__(self):
        self.head=None

    def insert_at_beginning(self, data):
        node=Node(data,self.head)
        self.head=node

    def print_list(self):
        if self.head is None:
            print("the linkedlist is empty")
        else:
           itr=self.head
           llstr=""
           while itr:
               llstr = llstr+str(itr.data)+"-->"
               itr=itr.next
           print(llstr)

    def linkedlist_length(self):
        count=0

        itr=self.head
        while itr:
            count=count+1
            itr=itr.next
        return count

    def insert_at_end(self,data):
        
        if self.head is None:
            self.head= Node(data,None)
            return
        itr= self.head
        #print(itr)
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def remove_at_index(self,index):
        
        if(index<0 or index>self.linkedlist_length()):
            raise Exception("invalid Index")

        if index==0:
            self.head=self.head.next
            return

        itr=self.head
        for x in range(self.linkedlist_length()):
            if x == index-1:
                itr.next=itr.next.next
                return
            else:
                itr=itr.next


    def insert_values(self,data_list):
        for x in data_list:
            self.insert_at_end(x)
            
    def insert_value_at(self,index,value):

       if(index<0 or index>self.linkedlist_length()):
            raise Exception("invalid Index")
       
       itr=self.head
       count=0
       while itr:   
           if count== index-1:
               node=Node(value,itr.next)
               #self.head
               itr.next=node
               break

           itr=itr.next
           count= count+1

    def insert_After_value(self, data_After, data_to_insert):

        itr=self.head
        count=0
        while itr:
            if itr.data==data_After:
                #self.insert_value_at(count+1,data_to_insert)
                itr.next=Node(data_to_insert,itr.nxt)
                break
            itr=itr.next
            count=count+1

    def remove_by_value(self,data):

        itr=self.head
        count=0
        flag=0
        while itr:
            if(itr.data==data):
                self.remove_at_index(count)
                break
    
            count=count+1
            itr=itr.next
    


if __name__=='__main__':
    ll=LinkedList()
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(4)
    # ll.print_list()
    # print(ll.linkedlist_length())
    # ll.insert_at_end(10)
    # ll.print_list()
    ll.insert_values([1,2,3,6,4,5,999])
    ll.print_list()
    #ll.remove_at_index(0)
    ll.print_list()
    ll.insert_value_at(3,111)
    ll.print_list()
    ll.insert_After_value(6,6666)
    ll.print_list()
    ll.remove_by_value(1)
    ll.print_list()


