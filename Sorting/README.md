🧠 Quick Comparison Table
Feature	Bubble	Selection	Insertion
Swaps	Many	Few	Very few
Adaptive	❌	❌	✅
Best for	Learning	Costly swaps	Nearly sorted arrays
Intuition	Adjacent swaps	Pick minimum	Insert in correct place
1️⃣ Bubble vs Selection vs Insertion Sort
🔹 Bubble Sort

Idea:
Big elements “bubble” to the end by swapping adjacent elements.

How it behaves:
Compare nums[j] and nums[j+1]
Swap if they are in the wrong order
After each pass, the largest element is fixed at the end
Characteristics:
Many swaps
Very easy to understand
Slow for large arrays
When to use:
Learning sorting basics
Very small arrays
When simplicity matters more than speed