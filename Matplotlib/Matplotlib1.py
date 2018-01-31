from matplotlib import pyplot as plt

days=[0, 1, 2, 3, 4, 5, 6]
money_spent=[10, 12, 12, 10, 14, 22, 24]
plt.plot(days, money_spent)
plt.show()

days = range(7)
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
plt.plot(days, money_spent)
plt.plot(days, money_spent_2)
plt.show()
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

"""
'--' — dashed line
':' — dotted line
'-' — unbroken line
'o' — circles
'*' — stars
's' — squares
"""

plt.plot(days, money_spent, color='green', linestyle='--')
plt.plot(days, money_spent_2, color='#AAAAAA',  marker='o')
x = [0, 1, 2, 3, 4]
y = [0**2, 1**2, 2**2, 3**2, 4**2]
plt.plot(x, y)
plt.show()
x = [0, 1, 2, 3, 4]
y = [0**2, 1**2, 2**2, 3**2, 4**2]
plt.plot(x, y)
plt.axis([0, 3, 2, 5])
plt.show()
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.legend(['parabola', 'cubic'])
plt.legend(['parabola', 'cubic'], loc=6)

"""
Position values loc accepts:
Number Code	String
0	best
1	upper right
2	upper left
3	lower left
4	lower right
5	right
6	center left
7	center right
8	lower center
9	upper center
10	center
"""

legend_labels = ["Table 1", "Table 2", "Table 3"]
plt.legend(legend_labels, loc=9)

ax = plt.subplot()
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(["10%", "60%", "80%"])
plt.close('all')
plt.figure(figsize=(4, 10)) # 4 inches wide and 10 inches tall
plt.plot(x, parabola)
plt.show()
plt.figure(figsize=(4, 10))
plt.plot(x, parabola)
plt.savefig('tall_and_narrow.png')
