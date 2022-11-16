"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    list = []
    for x in range(len(items)):
          items[x] = str(items[x]) 
       
    for i in items:
    
     if i not in list:
          a = items.count(i)
          frequencies[str(i)]= a
          list.append(i)

    return frequencies
