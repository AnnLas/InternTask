# Calculate

Calculate is a method for dealing with the best set of memes calculation, which can be sold on the USB stick for the highest price on the dark market (ClearCode told me to do that).

## Solution

First, according to this [Article](http://www.micsymposium.org/mics_2005/papers/paper102.pdf) and because of fact that I'm familiar with dynamic programming, I used it here. It has also great performance: O(N*C), in terms of memory and number of operations, where N - a number of input items(memes) and C - capacity(of the usb).   

In the first step, duplicates are removed by creating a set from memes list and then converting it to list.

Next, a value matrix is calculated. Each column of the matrix corresponds to 1 Mib + previous column value and each row coresponds to one meme. Each row can contain only it's item and the previous items. Problem is divided into smaller parts (knapsacks/usb sticks) and then the best set is choosen in for loop. 

Then, the last cell of the value matrix contains the best score to achive. We have to make another loop which starts at the end of the matrix (it makes the algo less efiicient but I have no idea how to solve that). It goes through the whole matrix and adds matching elements.


## Test

I prepare my own tests,  you can check it out. They are in the test_calculator.py file.



