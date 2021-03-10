 <h2>Merge Sort</h2>
<b><i>This is Merge Sort Python Program.</i></b> 

<h3>About :</h3>
<pre>
Merge Sort is a Divide &Conquer Alogrithm.

It divides input array in two halves,calls itself for the two halves.
the merge(arr,l,m,r) is key process that assumes that arr{i....m} and arr{m+1...r}
are sorted and merge the two sorted is sub arrays into one.
 </pre>

<h3>What do you mean by " Divide and Conquer approach"?</h3>

<pre>
A <b>Divide-and-conquer Algorithm</b> works by recursively breaking down a problem into two or more 
sub-problems of the same or related type, until these become simple enough to be solved directly. 

The solutions to the sub-problems are then combined to give a solution to the original problem.

The array is split in half and the process is repeated with each half until each half is of size 1 or 0. 

The array of size 1 is trivially sorted.

Now the two sorted arrays are combined into one big array. And this is continued until all the elements are combined and the array is sorted. 
</pre>
<h3>Time complexity</h3>

The algorithm works in <b>O(n.logn)</b>. This is because the list is being split in log(n) calls and the merging process takes linear time in each call.

<b>Auxiliary Space:</b> O(n)

<b>Algorithmic Paradigm:</b> Divide and Conquer

<b>Sorting In Place:</b> No in a typical implementation
<p> Made by - Ayushi0901</p>

<b>Stable:</b> Yes


<h3>Applications :</h3>
<pre>
1) Merge Sort is useful for sorting linked lists in O(nLogn) time.
2)Inversion Count Problem
3)Used in External Sorting
</pre>


<h3>Pseudocode :</h3>
<pre>
<b>MergeSort(arr[], l,  r)</b>
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
             
             

</pre>
