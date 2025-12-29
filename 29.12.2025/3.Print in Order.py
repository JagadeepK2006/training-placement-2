class Foo(object):
    def __init__(self):
        pass


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        printFirst()
        


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        time.sleep(0.04)
        
        printSecond()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        time.sleep(0.1)
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
