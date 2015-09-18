#
# HeapSort.py - Merge Sort Algorithm Sorting an array of randomly permuted of values.
# Website <http://adrianstatescu.ro>(MIT License).
# Email   <mergesortv@gmail.com>.
# Copyright (c) 2015, Adrian Statescu.
# 
 
class MergeSort:

      def __init__(self, arr):

          self.len = len( arr )

          self.vec = []

          self.vec = arr;

          self._divide_et_impera(0, self.len - 1)

      def _divide_et_impera(self, left, right):
       
        if(left < right):

          m = (left + right) >> 1

          self._divide_et_impera(left, m)

          self._divide_et_impera(m + 1, right)

          temp = [ 0 for i in range(0, self.len) ]
          
          i = left

          j = m + 1

          k = 0

          while ( i <= m and j <= right ):

                        if (self.vec[ i ] < self.vec[ j ]):

                            temp[ k ] = self.vec[ i ]
                            i += 1
                            k += 1

                        else:  
                            temp[ k ] = self.vec[ j ]
                            j += 1
                            k += 1

          while ( i <= m ):
                        temp[ k ] = self.vec[ i ]
                        k += 1
                        i += 1    

          while ( j <= right ):
                        temp[ k ] = self.vec[ j ]
                        k += 1
                        j += 1    
               
          k = 0
          for index in range(left, right + 1):
 
                 self.vec[ index ] = temp[ k ]
                 k = k + 1 
  
      def get(self):
         
          return self.vec
