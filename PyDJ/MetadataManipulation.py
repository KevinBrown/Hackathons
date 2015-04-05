import eyed3

class MetadataManipulation:
	dataObj = null	

	def __init__( path ) :
		self.setPath( path )

	def setPath( path ):
		self.filePath = path

	def loadMp3DataObject () :
		if ( self.dataObj == null ):
			self.dataObj = eyed3.load( self.getPath() )
		
		return self.dataObj

	def getArtist():
		return self.dataObj.tag.artist

	def getAlbum():
		return self.dataObj.tag.album

	def getSong():
		return self.dataObj.tag.song

		
