
import os
import time
import random
from colorama import Fore, Fore, Style
from copy import copy, deepcopy

'''

    Oliver BLOBz. A celular automata in the vein of Conways game of life

    Dedicated to John Conway.

    Copyright (C) 2021 Adam Oliver


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

global num
num = 80
hei = 22
wid = 80


print('#')
print(Fore.RED + '%', end='') #
#print(Fore.LIGHTGREEN + '%') #
print(Fore.YELLOW + '*') #
print(Fore.GREEN + '&') #
print(Fore.BLUE + '$') #
#quit()

global grid
global grid2
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 
grid2 = [[0 for i in range(wid)] for j in range(hei)] # 80 20 

# set all grid[x][y] to 6

county = 0
count = 0
for i in grid:
  for j in i:
    grid[county][count] = '6'
    
    count += 1
  count = 0 
  county += 1
# done

# set a few example variables (to be removed)


'''
buckets = ['6'] * num
buckets[9] = '7'
buckets[1] = '8'
buckets[2] = '9'
buckets[3] = '0'
buckets[4] = '1'
'''




# prints the grid2
def print_grid():

  grid2 = grid
  #grid2 = deepcopy(grid)

  count = 0
  for i in grid2:
    for e in i:

      if(e=='1'):print(Fore.CYAN + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.LIGHTGREEN_EX + '%', end='' ) # 
      if(e=='3'):print(Fore.LIGHTRED_EX + '*', end='' ) # 
      if(e=='4'):print(Fore.YELLOW + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 
      if(e=='6'):print(Fore.BLUE + ' ', end='' ) # 

      if(e=='7'):print(Fore.BLUE + 'i', end='' ) # 

      if(e=='10'):print(Fore.CYAN + '#', end='' ) # 
      if(e=='11'):print(Fore.CYAN + '#', end='' ) # 
      if(e=='12'):print(Fore.CYAN + '#', end='' ) # 
      if(e=='13'):print(Fore.CYAN + '#', end='' ) # 

      if(e=='14'):print(Fore.LIGHTGREEN_EX + '%', end='' ) # 
      if(e=='15'):print(Fore.LIGHTGREEN_EX + '%', end='' ) # 
      if(e=='16'):print(Fore.LIGHTGREEN_EX + '%', end='' ) # 
      if(e=='17'):print(Fore.LIGHTGREEN_EX + '%', end='' ) # 

      if(e=='18'):print(Fore.LIGHTRED_EX + '*', end='' ) # 
      if(e=='19'):print(Fore.LIGHTRED_EX + '*', end='' ) # 
      if(e=='20'):print(Fore.LIGHTRED_EX + '*', end='' ) # 
      if(e=='21'):print(Fore.LIGHTRED_EX + '*', end='' ) # 

      if(e=='22'):print(Fore.YELLOW + '&', end='' ) # 
      if(e=='23'):print(Fore.YELLOW + '&', end='' ) # 
      if(e=='24'):print(Fore.YELLOW + '&', end='' ) # 
      if(e=='25'):print(Fore.YELLOW + '&', end='' ) # 

      if(e=='a'):print(Fore.WHITE + 'a', end='' ) # 
      
      count += 1
      if(count == wid): print(''); count = 0
    
  print(Fore.BLUE + '', end='' ) # 

#
grid[6][9] = '3'
#
print_grid()


###
# this just adds a step
#
def add_cell():

  print('')
  print('')
  global grid
  #grid = deepcopy(grid)
  #quit()
  # change range(1) to change number of new characters
    
  for i in range(1):
    
    # adds a '#'
    # finds a random place in the grid, adds a cell
    #print(random.randint(1,6))
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '1' #str(random.randint(1,4))
    
    # adds a '%'
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '2' #str(random.randint(1,4))

    # adds a '*'
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '3' #str(random.randint(1,4))
    
    # adds a '&' i think
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)
    '''
    if( grid[x][y] != 6 ):
      grid[x][y] = '4' #str(random.randint(1,4))
  
    # adds a '$' i think
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '5' #str(random.randint(1,4))
    '''
  #grid = deepcopy(grid)


# this just stops list index out of range error
def numberz_h(thenum):

  #print('[')
  #print('wid thenum')
  #print(wid)
  #print(thenum)

  if(thenum >= wid):
    return wid - 1
  else:
    return thenum
    
def numberz(thenum):

  #print('[')
  #print('hei thenum')
  #print(hei)
  #print(thenum)

  if(thenum >= hei):
    return hei - 1
  else:
    return thenum


  
def a_step():  

  global grid

  ####a
  #y = deepcopy(x)
  grid2 = deepcopy(grid)

  anyhashes = 0

  # grid loop
  count = 0
  for i in grid:
    county = 0
    for j in i:
      #pass
      '''
      if( j == '4' ): #
 
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][county-1] = str(random.randint(22,25)) #'10' # up
        else:
          if( random.randint(0,1) == 1 ): # this is cool
            grid2[ count ][ county-1 ] = '4' # left
          else:
            grid2[ count ][ numberz_h(county+1) ] = '4' # right

      if( j == '22' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '23' # left
        else:
          grid2[ count-1 ][ county ] = '4' # up

      if( j == '23' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '24' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '4' # down

      if( j == '24' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '25' # down
        else:
          grid2[ count ][ numberz_h(county+1) ] = '4' # right

      '''
      ##

      if( j == '3' ): #
 
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][county-1] = str(random.randint(18,21)) #'10' # left
        else:
          if( random.randint(0,1) == 1 ): # this is cool
            grid2[ count ][ county-1 ] = '3' # left
          else:
            grid2[ count ][ numberz_h(county+1) ] = '3' # right

          

      if( j == '18' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '19' # up
        else:
          grid2[ count-1 ][ county ] = '3' # up

      if( j == '19' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '20' # left
        else:
          grid2[ numberz(count +1) ][ county ] = '3' # down

      if( j == '20' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '21' # 
        else:
          grid2[ count ][ numberz_h(county+1) ] = '3' # right



      if( j == '2' ): #
 
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][county-1] = str(random.randint(14,17)) #'10' # up
        else:
          if( random.randint(0,1) == 1 ): # this is cool
            grid2[ count ][ county-1 ] = '2' # left
          else:
            grid2[ count ][ numberz_h(county+1) ] = '2' # right


      if( j == '14' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '15' # left
        else:
          grid2[ count-1 ][ county ] = '2' # up


      if( j == '15' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '16' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '2' # down

      if( j == '16' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '17' # down
        else:
          grid2[ count ][ numberz_h(county+1) ] = '2' # right

      #print(j)
      #print('.', end='')
      #if( j == '5' ): #
      #  grid2[count][county] = 1

      # removes old '$'
      if(grid2[count][county] == '5' and grid[count][county] == '5' ):
        grid2[count][county] = '6' #'10' # up



      if( j == '1' ): #
 
        #print(':D' + str(i))
        anyhashes = 1

        #print('# detected')
        #print(i)
        #pass

        if( random.randint(0,1) == 1 ): # this is cool

          grid2[count][county-1] = str(random.randint(10,13)) #'10' # up

        else:
          if( random.randint(0,1) == 1 ): # this is cool
            grid2[ count ][ county-1 ] = '1' # left
          else:
            grid2[ count ][ numberz_h(county+1) ] = '1' # right


      if( j == '10' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '11' # left
        else:
          grid2[ count-1 ][ county ] = '1' # up


      if( j == '11' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '12' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '1' # down

      if( j == '12' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '13' # down
        else:
          grid2[ count ][ numberz_h(county+1) ] = '1' # right


















      # Predator and prey
      
      if( j == '1' and grid2[count][county-1] == '2' ): #
        grid2[count][county-1] = '1'

      if( j == '1' and grid2[count-1][county] == '2' ): #
        grid2[count-1][county] = '1'

      if( j == '1' and grid2[numberz(count+1)][county] == '2'  ): #
        grid2[numberz(count+1)][county] = '1'

      if( j == '1' and grid2[count][numberz_h(county+1)] == '2' ): #
        grid2[count][numberz_h(county+1)] = '1'
      

      if( j == '2' and grid2[count][county-1] == '3' ): #
        grid2[count][county-1] = '2'

      if( j == '2' and grid2[count-1][county] == '3' ): #
        grid2[count-1][county] = '2'

      if( j == '2' and grid2[numberz(count+1)][county] == '3'  ): #
        grid2[numberz(count+1)][county] = '2'

      if( j == '2' and grid2[count][numberz_h(county+1)] == '3' ): #
        grid2[count][numberz_h(county+1)] = '2'

      

      if( j == '3' and grid2[count][county-1] == '1' ): #
        grid2[count][county-1] = '3'

      if( j == '3' and grid2[count-1][county] == '1' ): #
        grid2[count-1][county] = '3'

      if( j == '3' and grid2[numberz(count+1)][county] == '1'  ): #
        grid2[numberz(count+1)][county] = '3'

      if( j == '3' and grid2[count][numberz_h(county+1)] == '1' ): #
        grid2[count][numberz_h(county+1)] = '3'
      

      '''
      if( j == '4' and grid2[count][county-1] == '1' ): #
        grid2[count][county-1] = '4'

      if( j == '4' and grid2[count-1][county] == '1' ): #
        grid2[count-1][county] = '4'

      if( j == '4' and grid2[numberz(count+1)][county] == '1'  ): #
        grid2[numberz(count+1)][county] = '4'

      if( j == '4' and grid2[count][numberz_h(county+1)] == '1' ): #
        grid2[count][numberz_h(county+1)] = '4'
      '''









      county += 1
      
    count += 1


  #if(anyhashes == 0 ):
    #print('need a hash')
  
  grid = deepcopy(grid2)


add_cell()

while True:
  #
  #
  #print_grid() # to be removed

  #if( random.randint(0,1) == 1 ): # this is cool
    #add_cell()
  
  a_step() # theres a flaw that moves the hash to left

  #add_cell()

  print_grid()

  #count_blues()

  #print('blues on screen: ' + str(1))
  #print('greens on screen: ')
  print('')

  time.sleep(.1)#0.1


#print(grid)

quit()










