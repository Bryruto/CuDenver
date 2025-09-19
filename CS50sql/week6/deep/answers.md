# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

random partitioning works well when you have a lot of data the problem arises when you want to access that data , becuase it is literally everywhere you have to look at all the servers.
That takes time then you must put all of what you find together like a puzzle to me it seems very time consuming.
I would maybe do this if i had a lot of useless data that maybe ill need way later most likely never.
But now looking at the other options this lets you send data very equaly so no server will over load and have more data then the rest.

## Partitioning by Hour

why to adopt this aproach
this makes the data very organized meaning if i want to query i can do it very fast all i need to know is what time.
this also makes it easy to identify where the most action is happening , and if you know where most action is going on you can identify when different actions go down.
I would use this if i wanted to see what people do on the clock and off the clock, or if the data i get is all day the same amount.

why not to adopt
I most likely would not use this if i have data only from a specific time becuase this would make one server have all the data and overload when the other servers are doing nothing.
also makes the server with all the data a lot slower but thats the data you probably want.

## Partitioning by Hash Value

why to adopt this aproach
This aproach work well when you want your data to be evenly disbured across the servers.
This aproach is also good to find a specific action by using the time and passing it through the hash funtion.


why not
Not that good at keeping related data together so if you need more then one result you need to access all the servers.

