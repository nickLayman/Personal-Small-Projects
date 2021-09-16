"""
This file was made to create the file NameList.p
NameList.p is a file containing a pickled list object of the 50 most common
last names in america in 2019, listed below. The names in the list were
cleaned up to just be strings of the names themselves without numbers
or spaces
"""

import pickle

names = """1. Smith

2. Johnson

3. Williams

4. Brown

5. Jones

6. Garcia

7. Miller

8. Davis

9. Rodriguez

10. Martinez

11. Hernandez

12. Lopez

13. Gonzalez

14. Wilson

15. Anderson

16. Thomas

17. Taylor

18. Moore

19. Jackson

20. Martin

21. Lee

22. Perez

23. Thompson

24. White

25. Harris

26. Sanchez

27. Clark

28. Ramirez

29. Lewis

30. Robinson

31. Walker

32. Young

33. Allen

34. King

35. Wright

36. Scott

37. Torres

38. Nguyen

39. Hill

40. Flores

41. Green

42. Adams

43. Nelson

44. Baker

45. Hall

46. Rivera

47. Campbell

48. Mitchell

49. Carter

50. Roberts
"""

namelist = names.split("\n")

while namelist.__contains__(''):
    namelist.remove('')

for i in range(len(namelist)):
    if i < 9:
        namelist[i] = namelist[i][3:]
    else:
        namelist[i] = namelist[i][4:]


with open('NameList.p', 'wb') as file:
    pickle.dump(namelist, file)
