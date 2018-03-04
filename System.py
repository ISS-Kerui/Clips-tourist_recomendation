# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Question
import os
###########################################################################
## Class MainPage
###########################################################################



class MainPage ( wx.Frame ):
	def OnEraseBackground(self, evt):
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("pic/background2.jpg")
		bmp.SetMask(wx.Mask(bmp, wx.WHITE))
		dc.DrawBitmap(bmp, 0, 0)
	
	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,350), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetMaxSize((500,350))
		self.SetMinSize((500,350))
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"SgTrip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 36, 70, 90, 90, False, "Big Caslon" ) )
		self.m_staticText1.SetForegroundColour((255,255,255))
		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, "Best Representation of you:", wx.DefaultPosition, (210,40), 0 )
		self.m_staticText2.SetForegroundColour((255,255,255))
		self.m_staticText2.SetFont(wx.Font( 18, 70, 90, 92, False, "Times" ))

		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )
		
		m_choice1Choices = ['Muslim','Hindu','Chinese','Christian','Others']
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gSizer1.Add( self.m_choice1, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, "       Sex:", wx.DefaultPosition, (80,40), 0 )
		self.m_staticText11.SetForegroundColour((255,255,255))
		self.m_staticText11.SetFont(wx.Font( 18, 70, 90, 92, False, "Times" ))
		self.m_staticText11.Wrap( -1 )
		gSizer1.Add( self.m_staticText11, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )
		
		m_choice2Choices = ['Male','Female']
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		gSizer1.Add( self.m_choice2, 0, wx.ALIGN_LEFT|wx.ALL, 10 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, "      Age:", wx.DefaultPosition, (80,40), 0 )
		self.m_staticText8.SetFont(wx.Font( 18, 70, 90, 92, False, "Times" ))
		self.m_staticText8.SetForegroundColour((255,255,255))
		self.m_staticText8.Wrap( -1 )
		gSizer1.Add( self.m_staticText8, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		m_choice3Choices = ['<25','25-40','41-50','50 and above']
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection(0)
		gSizer1.Add( self.m_choice3, 0, wx.ALL, 10 )
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Start", wx.Point( -1,-1 ), wx.Size( 120,120 ), 0 )
		self.m_button1.SetFont( wx.Font( 22, 70, 90, 92, False, "Times" ))
		
		
		sbSizer1.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"© The system is designed by ISS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer1.Add( self.m_staticText13, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )
		
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		os.remove('fact.txt')
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		self.sex = self.m_choice2.GetStringSelection()
		self.age = self.m_choice3.GetStringSelection()
		self.religion = self.m_choice1.GetStringSelection()

		Question.QuestionPage(self).Show()
		self.Hide()
	


if __name__ == '__main__':  
    app = wx.App()  
    MainPage(None).Show()
    app.MainLoop() 
