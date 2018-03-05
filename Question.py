# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import clips
import re
import pandas as pd

###########################################################################
## Class QuestionPage
###########################################################################
def readFactsFile(facts):
	
	
	cluster_name = []
	place_name = []
	new_facts = []
	for fact in facts:
		new_facts.append(fact.PPForm())
	
	for line in new_facts:
		
		if re.findall('selected-places-per-cluster',line):
			line = line.strip()
			places_per_cluster = re.findall(r"\(names\s(.*)\)\s\(",line)
			place_cluster_name = re.findall(r"\(cluster-name\s(.*)\)\s\(names",line)
			place_name.append(places_per_cluster[0].split(' '))
			cluster_name.append(place_cluster_name[0].strip())
			
			
				
	return cluster_name,place_name

def getMoreInfo(file1,place_name):
	df = pd.read_excel(file1)

	all_info =[]
	for cluster in place_name:
		info = []
		for place in cluster:
			info.append(df[df.Small_Attractions == place])
		all_info.append(info)

	return all_info

def createStepGlobal(step):
	if step == 1:
		clips.Assert("(step-one)")
	elif step == 2:
		clips.Assert("(step-two)")
	elif step == 3:
		clips.Assert("(step-three)")
	elif step == 4:
		clips.Assert("(step-four)")
	elif step == 5:
		clips.Assert("(step-five)")
	elif step == 6:
		clips.Assert("(step-six)")
	elif step == 7:
		clips.Assert("(step-seven)")
	elif step == 8:
		clips.Assert("(step-eight)")
	elif step == 9:
		clips.Assert("(step-nine)")
	elif step == 10:
		clips.Assert("(step-ten)")
	elif step == 11:
		clips.Assert("(step-eleven)")

def changePanel(frame,id):

		
		if id == 1:
			frame.panelOne.Destroy()
			frame.panelTwo = Panel_choose(frame)
			frame.panelTwo.m_choice1.SetItems(selections[0])
			frame.panelTwo.m_staticText1.SetLabel(questions[step])

		
		elif id == 2:
			frame.panelOne.Destroy()
			frame.panelThree = Panel_pic(frame)
		elif id == 3:
			frame.panelThree.Destroy()
			frame.panelTwo = Panel_choose(frame)
			frame.panelTwo.m_choice1.SetItems(selections[0])
			frame.panelTwo.m_staticText1.SetLabel(questions[step])
	
		elif id == 4:
			frame.panelTwo.Destroy()
			frame.panelFour = Panel_compare(frame)
		elif id == 5:
			frame.panelFour.Destroy()
			frame.panelOne = Panel_YESorNO(frame)
			frame.panelOne.m_staticText1.SetLabel(questions[step])
		elif id == 6:
			facts = clips.FactList()
			# print t
		

			# t = clips.StdoutStream.Read()

			#clips.SaveFacts('./fact.txt')
 			
			c,s = readFactsFile(facts)

			frame.panelOne.Destroy()
			info = getMoreInfo("Tourist Attraction Description.xlsx",s)
			print len(info)
			frame.panelFive = Panel_result(frame,c,info)

questions = ['Is this your first time travelling \nto Singapore? ',
			'Please select the places you have been to',
 			'How many days will you be \n travelling in Singapore?',
 			'Who are you planning to travel \nwith? ',
 			"What is your daily budget? \n(per person)",
 			'Please choose one place you prefer to go',
 			'Please choose one place you prefer to go',
 			'Please choose one place you prefer to go',
 			'Do you want a relax trip?',
 			'Do you like indoor activities more?'
 			
 			
 			]
selections = [ ['a. Only one day',
				'b. Two days',
				'c. Three days'],
				[ 'a. Solo, I am Solo, Han Solo.                         ',
				'b. I am travelling with my Significant other.         ' ,
				'c. I am travelling with my parents/ elderly.          '  ,
				'd. I am travelling with my other half and my children.',
				'e. I am travelling with my friends.                   '],
				['a. $10-$50',
				'b. $50-$100',
				'c. above $100']
				]

class customStatusBar(wx.StatusBar):
    def __init__(self,parent):
        wx.StatusBar.__init__(self,parent,-1)
        self.SetFieldsCount(10)
        self.SetStatusWidths([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
        self.count=0
        self.gauge=wx.Gauge(self,1001,100,pos=(2,2),size=(parent.GetSize()[0],20),style = wx.GA_HORIZONTAL)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.gauge.SetValue(10)

answers = []
step = 0


class Panel_pic ( wx.Panel ):
	
	
	def __init__( self, parent ):
		self.flag = [0,0,0,0,0,0]
		parent.SetSize((720,850))
		parent.Layout()
		self.parent = parent
		global step
		parent.status.gauge.SetValue(10*step)

		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 715,780 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, questions[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 24, 70, 90, 90, False, "Lucida Grande" ) )
		self.select_img = wx.Image('pic/0.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		bSizer2.Add( self.m_staticText6, 0, wx.ALIGN_LEFT|wx.ALL, 40 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/1.jpeg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton1.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/2.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton2.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/3.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton3.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/4.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton4.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/5.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton5.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"pic/6.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		# self.m_bpButton6.SetBitmapSelected( wx.Bitmap( u"pic/0.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizer6.Add( self.m_bpButton6, 0, wx.ALL|wx.EXPAND, 5 )
		

		bSizer2.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALIGN_RIGHT|wx.ALL|wx.RIGHT, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.m_bpButton1OnButtonClick )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.m_bpButton2OnButtonClick )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.m_bpButton3OnButtonClick )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.m_bpButton4OnButtonClick )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.m_bpButton5OnButtonClick )
		self.m_bpButton6.Bind( wx.EVT_BUTTON, self.m_bpButton6OnButtonClick )
	def __del__( self ):
		pass
	def m_bpButton1OnButtonClick( self, event ):
		if self.flag[0] == 0:
			self.m_bpButton1.SetBitmap(self.select_img)
			self.flag[0] =1
		else:
			self.m_bpButton1.SetBitmap(wx.Image('pic/1.jpeg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[0] = 0
	def m_bpButton2OnButtonClick( self, event ):
		if self.flag[1] == 0:
			self.m_bpButton2.SetBitmap(self.select_img)
			self.flag[1] =1
		else:
			self.m_bpButton2.SetBitmap(wx.Image('pic/2.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[1] = 0
	def m_bpButton3OnButtonClick( self, event ):
		if self.flag[2] == 0:
			self.m_bpButton3.SetBitmap(self.select_img)
			self.flag[2] =1
		else:
			self.m_bpButton3.SetBitmap(wx.Image('pic/3.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[2] = 0
	def m_bpButton4OnButtonClick( self, event ):
		if self.flag[3] == 0:
			self.m_bpButton4.SetBitmap(self.select_img)
			self.flag[3] =1
		else:
			self.m_bpButton4.SetBitmap(wx.Image('pic/4.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[3] = 0
	def m_bpButton5OnButtonClick( self, event ):
		if self.flag[4] == 0:
			self.m_bpButton5.SetBitmap(self.select_img)
			self.flag[4] =1
		else:
			self.m_bpButton5.SetBitmap(wx.Image('pic/5.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[4] = 0
	def m_bpButton6OnButtonClick( self, event ):
		if self.flag[5] == 0:
			self.m_bpButton6.SetBitmap(self.select_img)
			self.flag[5] =1
		else:
			self.m_bpButton6.SetBitmap(wx.Image('pic/6.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[5] = 0
	
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		global step
		step = step + 1
		self.parent.status.gauge.SetValue(10*step)
		createStepGlobal(step)
		
		answer = [str(self.flag[0]),str(self.flag[1]),str(self.flag[2]),str(self.flag[3]),str(self.flag[4]),str(self.flag[5])]
		answers.append(answer)
		clips.BuildGlobal('two_answer1',answer[0])
		clips.BuildGlobal('two_answer2',answer[1])
		clips.BuildGlobal('two_answer3',answer[2])
		clips.BuildGlobal('two_answer4',answer[3])
		clips.BuildGlobal('two_answer5',answer[4])
		clips.BuildGlobal('two_answer6',answer[5])
		changePanel(self.parent,3)

class Panel_result ( wx.Panel ):
	def OnEraseBackground(self, evt):
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("pic/background9.jpg")
		bmp.SetMask(wx.Mask(bmp, wx.WHITE))
		dc.DrawBitmap(bmp, 0, 0) 
	
	def __init__( self, parent,c,info):
		parent.status.Destroy()
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,770 ), style = wx.TAB_TRAVERSAL )
		self.parent = parent

		self.c = c
		self.info = info
		self.day_num = 1
		for i in range(len(self.c)):
			self.c[i] = self.c[i].replace('_',' ')
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		parent.SetSize((700,770))
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"DAY 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.SetForegroundColour((255,193,193))
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 36, 70, 90, 92, False, "Times" ) )
		
		bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 20 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"        RECOMMAND PLACES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.SetFont( wx.Font( 26, 70, 90, 92, False, "Times" ) )
		self.m_staticText15.SetForegroundColour((255,193,193))
		self.m_staticText15.Wrap( -1 )
		bSizer6.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, self.c[0], wx.DefaultPosition, (150,20), 0 )
		self.m_staticText11.SetFont( wx.Font( 22, wx.SCRIPT, wx.NORMAL, 92, False, "Times" ) )
		# self.m_staticText11.SetForegroundColour((0,0,122))
		self.m_staticText11.Wrap( -1 )
		bSizer6.Add( self.m_staticText11, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, self.c[1], wx.DefaultPosition, (150,20), 0 )
		self.m_staticText12.SetFont( wx.Font( 22, wx.SCRIPT, wx.NORMAL, 92, False, "Times" ) )
		# self.m_staticText12.SetForegroundColour((139,139,122))
		self.m_staticText12.Wrap( -1 )
		bSizer6.Add( self.m_staticText12, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, self.c[2], wx.DefaultPosition, (150,20), 0 )
		self.m_staticText13.SetFont( wx.Font( 22, wx.SCRIPT, wx.NORMAL, 92, False, "Times" ) )
		# self.m_staticText13.SetForegroundColour((139,139,122))
		self.m_staticText13.Wrap( -1 )
		bSizer6.Add( self.m_staticText13, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		
		gSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, '', wx.DefaultPosition, (200,400), style=wx.TE_MULTILINE )
		self.m_staticText14.SetFont( wx.Font( 16, wx.SCRIPT, wx.NORMAL, 58, False, "Times" ) )
		self.m_staticText14.Wrap( -1 )
		gSizer5.Add( self.m_staticText14, 0, wx.ALL, 40 )
		
		self.m_staticText14.Hide()
		bSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALIGN_RIGHT|wx.ALL, 30 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		# Connect Events
		self.m_staticText11.Bind( wx.EVT_ENTER_WINDOW, self.m_staticText11OnEnterWindow )

		self.m_staticText12.Bind( wx.EVT_ENTER_WINDOW, self.m_staticText12OnEnterWindow )
	
		self.m_staticText13.Bind( wx.EVT_ENTER_WINDOW, self.m_staticText13OnEnterWindow )
		
		
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		
		if len(self.c) == 3:
			self.m_button1.SetLabel('Quit')
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_staticText11OnEnterWindow( self, event ):
		printInfo1 = ''
		# self.m_staticText14.SetForegroundColour((205,85,85))
		if self.day_num == 1:
			info = self.info[0]
			for i in range(len(info)):

				printInfo1 =printInfo1+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'

		elif self.day_num == 2:
			info = self.info[3]
			for i in range(len(info)):
				printInfo1 =printInfo1+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		elif self.day_num == 3:
			info = self.info[6]
			for i in range(len(info)):
				printInfo1 =printInfo1+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		printInfo1 = printInfo1.replace('_',' ')
		self.m_staticText14.SetLabel(printInfo1)
		self.m_staticText14.Show()

	

	
	def m_staticText12OnEnterWindow( self, event ):
		# self.m_staticText14.SetForegroundColour((205,85,85))
		printInfo2 = ''
		if self.day_num == 1:
			info = self.info[1]
			for i in range(len(info)):
				printInfo2 =printInfo2+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		elif self.day_num == 2:
			info = self.info[4]
			for i in range(len(info)):
				printInfo2 =printInfo2+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		elif self.day_num == 3:
			info = self.info[7]
			for i in range(len(info)):
				printInfo2 =printInfo2+'\n'+'NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		printInfo2 = printInfo2.replace('_',' ')
		self.m_staticText14.SetLabel(printInfo2)
		self.m_staticText14.Show()


	
	def m_staticText13OnEnterWindow( self, event ):
		# self.m_staticText14.SetForegroundColour((205,85,85))
		printInfo3 = ''
		if self.day_num == 1:
			info = self.info[2]
			for i in range(len(info)):
				printInfo3 =printInfo3+'\n'+'PLACE NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		elif self.day_num == 2:
			info = self.info[5]
			for i in range(len(info)):
				printInfo3 =printInfo3+'\n'+'PLACE NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		elif self.day_num == 3:
			info = self.info[8]
			for i in range(len(info)):
				printInfo3 =printInfo3+'\n'+'PLACE NAME:'+info[i].Small_Attractions.values[0]+'\n'+'ADDRESS: '+info[i].Address.values[0]+'\n'+'OPENING HOURS: '+info[i].Opening_Hours.values[0]+'\n'+'COST: '+info[i].Cost.values[0]+'\n'
		printInfo3 = printInfo3.replace('_',' ')
		self.m_staticText14.SetLabel(printInfo3)
		self.m_staticText14.Show()
	


	

	def m_button1OnButtonClick( self, event ):
		self.day_num =  self.day_num + 1
		
		if len(self.c)==6 and self.day_num == 2:
				self.m_staticText1.SetLabel('DAY 2')
				self.m_staticText11.SetLabel(self.c[3])
				self.m_staticText12.SetLabel(self.c[4])
				self.m_staticText13.SetLabel(self.c[5])
				self.m_button1.SetLabel('Quit')
		elif len(self.c) == 9 and self.day_num == 2:
			self.m_staticText1.SetLabel('DAY 2')
			self.m_staticText11.SetLabel(self.c[3])
			self.m_staticText12.SetLabel(self.c[4])
			self.m_staticText13.SetLabel(self.c[5])

		elif len(self.c)==6 and self.day_num == 3:
			self.parent.Destroy()
			self.Destroy()
			
		elif len(self.c)>6 and self.day_num == 3:
			self.m_staticText1.SetLabel('DAY 3')
			self.m_staticText11.SetLabel(self.c[6])
			self.m_staticText12.SetLabel(self.c[7])
			self.m_staticText13.SetLabel(self.c[8])
			self.m_button1.SetLabel('Quit')
		else:
			self.parent.Destroy()
			self.Destroy()
					
	
class Panel_compare ( wx.Panel ):
	
	def __init__( self, parent ):
		global step
		parent.status.gauge.SetValue(10*step)
		parent.SetSize((560,430))
		parent.Layout()
		self.parent = parent
		self.flag = [0,0]
		self.select_img = wx.Image('pic/00.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		if parent.parent.religion == 'Hindu':
			self.picIndex = [[0,1],[2,3],[5,6]]
		else:
			self.picIndex = [[0,1],[2,3],[4,6]]
		self.pics =['pic/tag/Metropolian.jpg','pic/tag/Nature.jpeg','pic/tag/Entertainment.jpeg','pic/tag/Historical.jpg','pic/tag/Cultural1.jpeg','pic/tag/Cultural2.jpeg','pic/tag/Shopping.jpeg']
		

		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 560,393 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, questions[5], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 24, 70, 90, 90, False, "Lucida Grande" ) )
		
		bSizer2.Add( self.m_staticText6, 0, wx.ALIGN_LEFT|wx.ALL, 40 )
		
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( self.pics[0], wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer10.Add( self.m_bpButton1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( self.pics[1], wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer10.Add( self.m_bpButton2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.m_bpButton1OnButtonClick )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.m_bpButton2OnButtonClick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_bpButton1OnButtonClick( self, event ):
		if self.flag[0] == 0 and self.flag[1] == 0: 
			self.m_bpButton1.SetBitmap(self.select_img)
			self.flag[0] =1
		elif self.flag[0] == 0 and self.flag[1] == 1: 
			self.m_bpButton1.SetBitmap(self.select_img)
			self.flag[0] =1
			self.flag[1] =0
			self.m_bpButton2.SetBitmap(wx.Image(self.pics[self.picIndex[step-5][1]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
		else:
			self.m_bpButton1.SetBitmap(wx.Image(self.pics[self.picIndex[step-5][0]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[0] = 0
	
	def m_bpButton2OnButtonClick( self, event ):
		if self.flag[1] == 0 and self.flag[0] == 0:
			self.m_bpButton2.SetBitmap(self.select_img)
			self.flag[1] =1
		elif self.flag[0] == 1 and self.flag[1] == 0: 
			self.m_bpButton2.SetBitmap(self.select_img)
			self.flag[0] =0
			self.flag[1] =1
			self.m_bpButton1.SetBitmap(wx.Image(self.pics[self.picIndex[step-5][0]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
		else:
			self.m_bpButton2.SetBitmap(wx.Image(self.pics[self.picIndex[step-5][1]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
			self.flag[1] = 0
	
	def m_button1OnButtonClick( self, event ):
		if self.flag[0] == 1 or self.flag[1] == 1:
			answer = self.flag.index(1)+1
			answers.append(answer)
			global step
			step = step + 1
			createStepGlobal(step)
			self.flag[0] = 0
			self.flag[1] = 0
			self.parent.status.gauge.SetValue(10*step)
			if step == 6:
				self.m_staticText6.SetLabel(questions[step])
				self.m_bpButton1.SetBitmap(wx.Image(self.pics[self.picIndex[1][0]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
				self.m_bpButton2.SetBitmap(wx.Image(self.pics[self.picIndex[1][1]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
				clips.BuildGlobal('six_answer',answer)

			elif step == 7:
				self.m_staticText6.SetLabel(questions[step])
				self.m_bpButton1.SetBitmap(wx.Image(self.pics[self.picIndex[2][0]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
				self.m_bpButton2.SetBitmap(wx.Image(self.pics[self.picIndex[2][1]],wx.BITMAP_TYPE_ANY).ConvertToBitmap())
				clips.BuildGlobal('seven_answer',answer)
			elif step == 8:
				clips.BuildGlobal('eight_answer',answer)
				changePanel(self.parent,5)
		else:
			dlg = wx.MessageDialog(None, "Please click one picture", "", wx.OK | wx.ICON_QUESTION)
			if dlg.ShowModal() == wx.ID_YES:
				self.Close(True)
				dlg.Destroy()

class Panel_YESorNO ( wx.Panel ):
	def OnEraseBackground(self, evt):
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("pic/background.jpg")
		bmp.SetMask(wx.Mask(bmp, wx.WHITE))
		dc.DrawBitmap(bmp, 0, 0)
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 725,410 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		global step
		parent.status.gauge.SetValue(10*step)
		self.parent = parent
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		parent.SetSize((725,410))
		parent.Layout()
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Is this your first time travelling to \n Singapore? ", wx.DefaultPosition, (400,50), 0 )
		self.m_staticText1.SetFont( wx.Font( 20, 70, 90, 90, False, "Lucida Grande" ) )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 3, wx.ALL, 20 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"YES", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"NO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_RIGHT|wx.ALL, 20 )
		
		
		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( gSizer2, 4, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 5, wx.EXPAND, 5 )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		

		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		answers.append('yes')
		global step
		step = step +1
		self.parent.status.gauge.SetValue(10*step)


		if step == len(questions):
			createStepGlobal(step)
			clips.BuildGlobal('ten_answer',1)
			clips.Run()
			changePanel(self.parent,6)
			
		else:
			createStepGlobal(step)
			self.m_staticText1.SetLabel(questions[step])
			# 1 == YES  0 == NO
			if step == 1:
					clips.BuildGlobal('one_answer',1)
			elif step == 9:
				clips.BuildGlobal('nine_answer',1)
				
			if step  == 1 and answers[0] == 'yes':
				step = step +1
				answers.append('NULL')
				changePanel(self.parent,1)
		
		
	def m_button2OnButtonClick( self, event ):
		global step
		step = step +1
		self.parent.status.gauge.SetValue(10*step)
		if step == len(questions):
			createStepGlobal(step)
			clips.BuildGlobal('ten_answer',0)
			clips.Run()
			changePanel(self.parent,6)
		else:
			createStepGlobal(step)
			self.m_staticText1.SetLabel(questions[step])
			answers.append('no')

			if step  == 1 and answers[0] == 'no':
				clips.Assert("(YN_second)")
				changePanel(self.parent,2)
			if step == 1:
				clips.BuildGlobal('one_answer',0)
			elif step == 9:
				clips.BuildGlobal('nine_answer',0)
		

class Panel_choose( wx.Panel ):
	def OnEraseBackground(self, evt):
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("pic/background.jpg")
		bmp.SetMask(wx.Mask(bmp, wx.WHITE))
		dc.DrawBitmap(bmp, 0, 0)
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 725,410 ), style = wx.TAB_TRAVERSAL )
		self.parent = parent
		global step
		parent.status.gauge.SetValue(10*step)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		parent.SetSize((725,410))
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Question1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 20, 70, 90, 90, False, "Lucida Grande" ) )
		gSizer1.Add( self.m_staticText1, 3, wx.ALL, 20 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer5.Add( self.m_choice1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 5, wx.EXPAND, 5 )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		
		global step
		step = step + 1
		self.parent.status.gauge.SetValue(10*step)
		answer = self.m_choice1.GetStringSelection().split('.')[0]
		answers.append(answer)
		createStepGlobal(step)
			

		if step == 3:
			self.parent.panelTwo.m_choice1.SetItems(selections[1])
			self.parent.panelTwo.m_staticText1.SetLabel(questions[step])
			clips.BuildGlobal('three_answer',answer)
		elif step == 4:
			self.parent.panelTwo.m_choice1.SetItems(selections[2])
			self.parent.panelTwo.m_staticText1.SetLabel(questions[step])
			clips.BuildGlobal('four_answer',answer)
		elif step == 5:
			clips.BuildGlobal('five_answer',answer)
			changePanel(self.parent,4)
class QuestionPage ( wx.Frame ):

		
	def __init__( self, parent ):
		clips.Load('try.clp')
		clips.Reset()
		clips.BuildGlobal('religion',parent.religion)
		clips.BuildGlobal('sex',parent.sex)
		clips.BuildGlobal('age',parent.age)
		self.parent = parent
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.status = customStatusBar(self)
		self.SetStatusBar(self.status)
		self.panelOne = Panel_YESorNO(self)
		bsizer = wx.BoxSizer(wx.VERTICAL)
		bsizer.Add(self.panelOne, 1, wx.EXPAND)
		self.SetSizer(bsizer)
		self.Layout()
		
		self.Centre( wx.BOTH )
		

	def __del__( self ):
		self.parent.Show()
		clips.Clear()
		global step
		step = 0
		global answers	
		answers = []

	


		


	
