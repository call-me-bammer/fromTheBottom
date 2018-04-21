#Inspired by 'Dragon Realm'
#-*- coding: euc-kr -*-

import random
import time

def intro():
	print
	print '    [Chapter1.] You are a freshman and in the Hanyang Tech\'s the department of computer & software.'
	print '''
	
	lll   lll      ll       ll  --  lllllllllll      llllllllll       llllllllll      lll   lll
	lll   lll       ll     ll   --  lllllllllll      lll             lllll            lll   lll
	lll   lll        lll lll    --      lll          lll            lll               lll   lll
	lllllllll         lllll     --      lll          llllllllll     lll               lllllllll
	lll   lll          lll      --      lll          lll            lll               lll   lll
	lll   lll          lll      --      lll          lll             lllll            lll   lll
	lll   lll          lll      --      lll          llllllllll       llllllllll      lll   lll
'''
	print '    Soon, you\'ll face to the reality this program predicts'
	print '   on choices you made along with a long (maybe short) about 20-year-life.'
	print

def choosePhase():
	room=''
	while room!='0' and room!='1':
		print 'Question_one: What room do you want to go in over 0 and 1?'
		print
		room=raw_input()
	return room

def checkPhase(roomNum):
	print '    You approach the room...'
	time.sleep(3)
	print '    There are many 0 and 1 are on the roadside...'
	print '''
		0000101010111111111010100010101001010101000010
		0101111110101010101110010000010101101111110101
		1010101011111111010000100001000101010001011010
		1000100010011101010101000001011010100110111110
		1111001101111100000001111100000101010010010100
		1010000110100000100001000100010111111101011100
		1111101001000010010010001000101010001010010101
		0010000101011000111111100000010100100100111100
		1000010101010001010101111100001000111001001010
		1110010010010001010100100100100010001010000100
		1001000101001000000000101010101010101010100111
		1000100101010010001010010000100100001000010011
		1000010100101010100101010100001010100101010010
'''
	time.sleep(5)
	print '    Suddenly, "The Master.Imeg" come out from the door and he\'s in front of you now.'
	time.sleep(5)
	print '    He open his mouth to speak...'
	print
	time.sleep(5)

	randomRoom=random.randint(0,1)

	if roomNum==str(randomRoom):
		print '    "...Maybe, you wanna major security, right? You\'ll make some world-awesome program in near future."\n'
		time.sleep(4)
		print '    "So, you have to be my TAs. Su-Go_Ring."'
	else:
		print '    "...OMG. I saw your part of the future for a second...\n'
		time.sleep(2)
		print '    "You\'ll be a slave of coding...It\'s too pity."'

bornToChoose='yes'
while bornToChoose=='yes' or bornToChoose=='y':

	intro()

	roomNum=choosePhase()

	checkPhase(roomNum)
	
	time.sleep(5)
	print '''

	lll         lll	  llllllllll  lllllllllll	  lll	llllllllll    	   lllllllllll	 lllllllllll   lllllllllll      lll
	lll	    lll   lll	      lll		  lll	ll		   lll		 ll	 lll   ll      lll      lll
	lll	   	  lll	      lll		  	ll		   lll		 ll	 lll   ll      lll      lll
	lll	    lll	  lll  	      lll		  lll	ll		   lll		 ll	 lll   ll      lll      lll
	lll	    lll	  llllllllll  lllllllllll	  lll	llllllllll	   lllllllllll	 lllllllllll   lllllllllll      lll
	lll	    lll	  lll         lll		  lll		ll	   lll	 	 	 lll           lll      lll
	lll	    lll	  lll	      lll		  lll		ll	   lll			 lll           lll
	lllllllll   lll	  lll	      lll		  lll		ll	   lll			 lll           lll      lll
	lllllllll   lll	  lll	      lllllllllll	  lll	llllllllll	   lllllllllll	 lllllllllll   lllllllllll      lll

'''
	print
	print '[Choice of -1] Do you want to "Really" be born again? (yes or no)'
	bornToChoose=raw_input()

	if bornToChoose=='really' or bornToChoose=='Really':
		i=0
		while i<100:
			print
			i+=1
		print '    YOU_CAN\'T_BE_BORN_AGAIN.'
