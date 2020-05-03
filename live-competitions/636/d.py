def findMaxGuests(arrl, exit, n): 
  
    # Sort arrival and exit arrays 
    arrl.sort(); 
    exit.sort(); 
  
    # guests_in indicates number of  
    # guests at a time 
    guests_in = 1; 
    max_guests = 1; 
    time = arrl[0]; 
    i = 1; 
    j = 0; 
  
    # Similar to merge in merge sort to  
    # process all events in sorted order 
    while (i < n and j < n): 
          
        # If next event in sorted order is  
        # arrival, increment count of guests 
        if (arrl[i] <= exit[j]): 
      
            guests_in = guests_in + 1; 
  
        # Update max_guests if needed 
            if(guests_in > max_guests): 
          
                max_guests = guests_in; 
                time = arrl[i]; 
                  
            # increment index of arrival array 
            i = i + 1;  
      
        else: 
            guests_in = guests_in - 1; 
            j = j + 1; 
    
    return max_guests

for _ in range(int(input())):
    n,k = map(int,input().split())
    ar = list(map(int,input().split()))
    start = []
    end = []
    for i in range(n//2):
        start.append(min(ar[i],ar[i*-1 -1]) + 1)
        end.append(max(ar[i],ar[i*-1 -1]) + k)
        start.append(ar[i]+ar[i*-1 -1])
        end.append(ar[i]+ar[i*-1 -1])
    print(n-findMaxGuests(start,end,len(start)))