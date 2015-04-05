import eyed3

class MetadataManipulation:
	filePath = ""


	def __init__(self ) :
		return None
#		if ( not path ) :
#			self.setPath( path )

	def setPath(self, path):
		self.filePath = path
	
	def getPath(self):
		return self.filePath

	
	def loadMp3DataObject (self) :
		self.dataObj = eyed3.load( self.getPath() )
		return self.dataObj

	def getArtist(self):
		retval = self.loadMp3DataObject()
		return retval.tag.artist

	def getAlbum(self):
		return self.dataObj.tag.album

	def getSong(self):
		return self.dataObj.tag.title
