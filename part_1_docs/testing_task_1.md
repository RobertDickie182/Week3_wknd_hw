### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# The operator in line 21 should be '==', and there should be a ':' after the 'else' statement in line 23.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# 'dif' on line 27 should be 'def', 'card1' on line 27 should have a ',' after it, and the 'card' variable on line 29, should be 'card1'
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# The 'total' variable on line 36 should have a value, 'return' on line 39 shouldn't be inside the 'for' loop, and 'total' at the end of line 39 should have the str() function before it in order to convert the type to a string to allow for concatenation.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

```
