"""
VR Drum Kit Demo
Version: 1.0.0
"""

# Import modules.
import viz
import vizconnect
import vizfx
import vizmat
import viztask
import vizinfo
import vizproximity
import vizshape
import tools
import time
import vizact
from math import * 

maxPossPerSec = 0.1
viz.setOption('viz.stereo', viz.QUAD_BUFFER)
viz.setOption('viz.fullscreen', 1)

#world_axes = vizshape.addAxes()
#X = viz.addText3D('X',pos=[1.1,0,0],color=viz.RED,scale=[0.3,0.3,0.3],parent=world_axes)
#Y = viz.addText3D('Y',pos=[0,1.1,0],color=viz.GREEN,scale=[0.3,0.3,0.3],align=viz.ALIGN_CENTER_BASE,parent=world_axes)
#Z = viz.addText3D('Z',pos=[0,0,1.1],color=viz.BLUE,scale=[0.3,0.3,0.3],align=viz.ALIGN_CENTER_BASE,parent=world_axes)


# add a stencil buffer for the outline highlight
if __name__ == "__main__":
	viz.setOption('viz.display.stencil', 8)
	#vizconnect.go('./vizconnect_config.py')
	vizconnect.go('./xylo_vizconnect_config2017.py')
	for tracker in vizconnect.ConfigurationManager.get().getDict('tracker'):
		print(tracker)
	# get the quality setting of the demo if specified
	DEMO_QUALITY_SETTING = max(0, viz.getOption('DEMO_QUALITY_SETTING', default=4, type=int))
	viz.setMultiSample(DEMO_QUALITY_SETTING*2)
	# disable the head lamps since we're doing lighting ourselves
	for window in viz.getWindowList():
		window.getView().getHeadLight().disable()
else:
	vizconnect.go('./multiscript_vizconnect_config.py')

# Add the local events (events specific to this demo) 
#vizconnect.go('vizconnect_config_local_events.py')

# Load the vizconnect configuration. File: base_vizconnect_config2016.py
vizfx.addDirectionalLight(euler=(0,90,0))

# Add a viewpoint so the user starts at [0,0,0].
vp = vizconnect.addViewpoint(pos=[0, 0, 0], posMode=vizconnect.VIEWPOINT_MATCH_BASE)

# Enable physics so that objects may collide together.
viz.phys.enable()

# Add an environment model with collision mesh.
env = vizfx.addChild('dojo.osgb')
env.disable(viz.SHADOW_CASTING)
env.collideMesh()

# Add directional shadow light pointing down.
light1 = vizfx.addDirectionalLight(shadow=viz.SHADOW_DEPTH_MAP, pos=[6,3,0],euler=(0,45,0))
light2 = vizfx.addDirectionalLight(shadow=viz.SHADOW_DEPTH_MAP, pos=[-6,3,0],euler=(90,45,0))
light3 = vizfx.addDirectionalLight(shadow=viz.SHADOW_DEPTH_MAP, pos=[0,3,6],euler=(180,45,0))
light4 = vizfx.addDirectionalLight(shadow=viz.SHADOW_DEPTH_MAP, pos=[0,3,-6],euler=(270,45,0))

# Set ambient light color.
vizfx.setAmbientColor([.6]*3)

# Add the drum kit
xylo = viz.addChild('./art/models/xylophone.dae',
pos=[-.5,0,1.5], scale=[1,1,1])
xylo.setEuler([340,0,0])



print("--------")
for entry in vizconnect.ConfigurationManager.get().getDict('tracker'):
	print(entry)
print("--------")

		
#Add sounds
class SoundPlayer:
	def __init__(self):
		self.mixer = viz.addSoundMixer()
	def play(self, path):
		self.mixer.play('./art/sounds/%s'%path, viz.PLAY)
	def playXylo1(self):
		self.play('xylo1.wav')
#	def playXylo2(self):
#		self.play('xylo3.wav')
#	def playXylo2(self):
#		self.play('xylo4.wav')
#	def playXylo2(self):
#		self.play('xylo5.wav')
#	def playXylo2(self):
#		self.play('xylo6.wav')
#	def playXylo2(self):
#		self.play('xylo7.wav')
#	def playXylo2(self):
#		self.play('xylo8.wav')
#	def playXylo2(self):
#		self.play('xylo9.wav')
#	def playXylo2(self):
#		self.play('xylo10.wav')
#	def playXylo2(self):
#		self.play('xylo11.wav')
#	def playXylo2(self):
#		self.play('xylo12.wav')
#	def playXylo2(self):
#		self.play('xylo13.wav')
#	def playXylo2(self):
#		self.play('xylo14.wav')
#	def playXylo2(self):
#		self.play('xylo15.wav')
#	def playXylo2(self):
#		self.play('xylo16.wav')
#	def playXylo2(self):
#		self.play('xylo17.wav')
#	def playXylo2(self):
#		self.play('xylo18.wav')
#	def playXylo2(self):
#		self.play('xylo19.wav')
#	def playXylo2(self):
#		self.play('xylo20.wav')
#	def playXylo2(self):
#		self.play('xylo21.wav')
#	def playXylo2(self):
#		self.play('xylo22.wav')
#	def playXylo2(self):
#		self.play('xylo23.wav')
#	def playXylo2(self):
#		self.play('xylo24.wav')
#	def playXylo2(self):
#		self.play('xylo25.wav')
#	def playXylo2(self):
#		self.play('xylo26.wav')
#	def playXylo2(self):
#		self.play('xylo27.wav')
#	def playXylo2(self):
#		self.play('xylo28.wav')
#	def playXylo2(self):
#		self.play('xylo29.wav')
#	def playXylo2(self):
#		self.play('xylo30.wav')
#	def playXylo2(self):
#		self.play('xylo31.wav')
#	def playXylo2(self):
#		self.play('xylo32.wav')
#	def playXylo2(self):
#		self.play('xylo33.wav')
#	def playXylo2(self):
#		self.play('xylo34.wav')
#	def playXylo2(self):
#		self.play('xylo35.wav')
	
		
sp = SoundPlayer()

enteredDir = None


rHand = vizconnect.getAvatar().getAttachmentPoint('r_hand').getNode3d()
lHand = vizconnect.getAvatar().getAttachmentPoint('l_hand').getNode3d()
rHandTar = vizproximity.Target(rHand)
lHandTar = vizproximity.Target(lHand)

class DirectionUpdater:
	def __init__ (self):
		self.rHandPre = rHand.getPosition()
		self.rHandPost = rHand.getPosition()
		self.lHandPre = lHand.getPosition()
		self.lHandPost = lHand.getPosition()
		self.fist = True
		
	def upadate(self):
		#if self.fist:
		if abs(self.rHandPost[1] - vizconnect.getAvatar().getAttachmentPoint('r_hand').getNode3d().getPosition()[1]) > 0.01 or abs(self.lHandPost[1] - vizconnect.getAvatar().getAttachmentPoint('l_hand').getNode3d().getPosition()[1]) > 0.01  : #else could be noise
			print("Updated   %s"%(str(abs(self.lHandPost[1] - lHand.getPosition()[1]))))
			self.rHandPre = self.rHandPost;
			self.rHandPost = vizconnect.getAvatar().getAttachmentPoint('r_hand').getNode3d().getPosition()
			
			self.lHandPre = self.lHandPost;
			self.lHandPost = vizconnect.getAvatar().getAttachmentPoint('l_hand').getNode3d().getPosition()
			
	def getDir(self):
		resr = None
		resl = None
		if not (abs(self.rHandPre[1] - self.rHandPost[1]) == 0):
			resr = (self.rHandPre[1] - self.rHandPost[1])/abs(self.rHandPre[1] - self.rHandPost[1])
		if not (abs(self.lHandPre[1] - self.lHandPost[1]) == 0):
			resl = (self.lHandPre[1] - self.lHandPost[1])/abs(self.lHandPre[1] - self.lHandPost[1])
			
		print("returned   %s"%str([resr, resl]))
		
		return [resr, resl]
	
dirUpdate = DirectionUpdater()
#vizact.onupdate(1,dirUpdate.upadate)


def EnterProximity(e):
	global enterDir;
	if True or (e.target == rHandTar and dirUpdate.getDir()[0] == 1.0 ) or (e.target == lHandTar and dirUpdate.getDir()[1] == 1.0):
		enterDir = dirUpdate.getDir()
		
		if e.sensor == xyloBar1:
			sp.playXylo1()
#		elif e.sensor == xyloBar2:
#			sp.playXylo2()
#		elif e.sensor == xyloBar3:
#			sp.playXylo3()
#		elif e.sensor == xyloBar4:
#			sp.playXylo4()
#		elif e.sensor == xyloBar5:
#			sp.playXylo5()
#		elif e.sensor == xyloBar6:
#			sp.playXylo6()
#		elif e.sensor == xyloBar7:
#			sp.playXylo7()
#		elif e.sensor == xyloBar8:
#			sp.playXylo8()
#		elif e.sensor == xyloBar9:
#			sp.playXylo9()
#		elif e.sensor == xyloBar10:
#			sp.playXylo10()
#		elif e.sensor == xyloBar10:
#			sp.playXylo11()
#		elif e.sensor == xyloBar10:
#			sp.playXylo12()
#		elif e.sensor == xyloBar10:
#			sp.playXylo13()
#		elif e.sensor == xyloBar10:
#			sp.playXylo14()
#		elif e.sensor == xyloBar10:
#			sp.playXylo15()
#		elif e.sensor == xyloBar10:
#			sp.playXylo16()
#		elif e.sensor == xyloBar10:
#			sp.playXylo17()
#		elif e.sensor == xyloBar10:
#			sp.playXylo18()
#		elif e.sensor == xyloBar10:
#			sp.playXylo19()
#		elif e.sensor == xyloBar10:
#			sp.playXylo20()
#		elif e.sensor == xyloBar10:
#			sp.playXylo21()
#		elif e.sensor == xyloBar10:
#			sp.playXylo22()
#		elif e.sensor == xyloBar10:
#			sp.playXylo23()
#		elif e.sensor == xyloBar10:
#			sp.playXylo24()
#		elif e.sensor == xyloBar10:
#			sp.playXylo25()
#		elif e.sensor == xyloBar10:
#			sp.playXylo26()
#		elif e.sensor == xyloBar10:
#			sp.playXylo27()
#		elif e.sensor == xyloBar10:
#			sp.playXylo28()
#		elif e.sensor == xyloBar10:
#			sp.playXylo29()
#		elif e.sensor == xyloBar10:
#			sp.playXylo30()
#		elif e.sensor == xyloBar10:
#			sp.playXylo31()
#		elif e.sensor == xyloBar10:
#			sp.playXylo32()
#		elif e.sensor == xyloBar10:
#			sp.playXylo33()
#		elif e.sensor == xyloBar10:
#			sp.playXylo34()
#		elif e.sensor == xyloBar10:
#			sp.playXylo35()
#		

manager = vizproximity.Manager()


manager.addTarget(rHandTar)
manager.addTarget(lHandTar)

xyloBar1  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_38"),scale=(1,1,1))#
#xyloBar2  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_39"),scale=(1,1,1))#
#xyloBar3  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_40"),scale=(1,1,1))#
#xyloBar4  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_41"),scale=(1,1,1))#
#xyloBar5  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_42"),scale=(1,1,1))#
#xyloBar6  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_43"),scale=(1,1,1))#
#xyloBar7  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_44"),scale=(1,1,1))#
#xyloBar8  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_45"),scale=(1,1,1))#
#xyloBar9  = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_46"),scale=(1,1,1))#
#xyloBar10 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_47"),scale=(1,1,1))#
#xyloBar11 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_48"),scale=(1,1,1))#
#xyloBar12 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_49"),scale=(1,1,1))#
#xyloBar13 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_50"),scale=(1,1,1))#
#xyloBar14 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_51"),scale=(1,1,1))#
#xyloBar15 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_52"),scale=(1,1,1))#
#xyloBar16 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_53"),scale=(1,1,1))#
#xyloBar17 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_54"),scale=(1,1,1))#
#xyloBar18 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_55"),scale=(1,1,1))#
#xyloBar19 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_56"),scale=(1,1,1))#
#xyloBar20 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_57"),scale=(1,1,1))#
#xyloBar21 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_58"),scale=(1,1,1))#
#xyloBar22 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_59"),scale=(1,1,1))#
#xyloBar23 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_60"),scale=(1,1,1))#
#xyloBar24 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_61"),scale=(1,1,1))#
#xyloBar25 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_62"),scale=(1,1,1))#
#xyloBar26 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_63"),scale=(1,1,1))#
#xyloBar27 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_64"),scale=(1,1,1))#
#xyloBar28 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_65"),scale=(1,1,1))#
#xyloBar29 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_66"),scale=(1,1,1))#
#xyloBar30 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_67"),scale=(1,1,1))#
#xyloBar31 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_68"),scale=(1,1,1))#
#xyloBar32 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_69"),scale=(1,1,1))#
#xyloBar33 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_70"),scale=(1,1,1))#
#xyloBar34 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_71"),scale=(1,1,1))#
#xyloBar35 = vizproximity.addBoundingBoxSensor(xylo.getChild("instance_72"),scale=(1,1,1))#

manager.addSensor(xyloBar1)
#manager.addSensor(xyloBar2)
#manager.addSensor(xyloBar3)
#manager.addSensor(xyloBar4)
#manager.addSensor(xyloBar5)
#manager.addSensor(xyloBar6)
#manager.addSensor(xyloBar7)
#manager.addSensor(xyloBar8)
#manager.addSensor(xyloBar9)
#manager.addSensor(xyloBar10)
#manager.addSensor(xyloBar11)
#manager.addSensor(xyloBar12)
#manager.addSensor(xyloBar13)
#manager.addSensor(xyloBar14)
#manager.addSensor(xyloBar15)
#manager.addSensor(xyloBar16)
#manager.addSensor(xyloBar17)
#manager.addSensor(xyloBar18)
#manager.addSensor(xyloBar19)
#manager.addSensor(xyloBar20)
#manager.addSensor(xyloBar21)
#manager.addSensor(xyloBar22)
#manager.addSensor(xyloBar23)
#manager.addSensor(xyloBar24)
#manager.addSensor(xyloBar25)
#manager.addSensor(xyloBar26)
#manager.addSensor(xyloBar27)
#manager.addSensor(xyloBar28)
#manager.addSensor(xyloBar29)
#manager.addSensor(xyloBar30)
#manager.addSensor(xyloBar31)
#manager.addSensor(xyloBar32)
#manager.addSensor(xyloBar33)
#manager.addSensor(xyloBar34)
#manager.addSensor(xyloBar35)


lastPlayed = time.time();

def playBassDrumWrapper():
	global lastPlayed
	if time.time() - lastPlayed > maxPossPerSec:
		sp.playBassDrum()
		lastPlayed = time.time()

manager.onEnter(None,EnterProximity)
vizact.onkeydown('p', manager.setDebug, viz.TOGGLE)