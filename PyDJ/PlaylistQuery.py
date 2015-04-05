from pyechonest import config
from pyechonest import song

import sqlite3
from os import walk

from MetadataManipulation import MetadataManipulation

config.ECHO_NEST_API_KEY = "EZTRYZBZU8BTT2PK2"


class PlaylistQuery():

	def getEchonestSongData ( src, artistName, songName ) :
#		res = song.search( artist="Justin Bieber", title="Baby" )
		res = song.search( artist=artistName, title=songName )		
#		res = song.search( artist='Charlie Parker', title='Now\'s the time')
		
		print( res )
		
		for curres in res :
			print curres.get_audio_summary()
	
		if not res:
			raise Exception( "SongNotFound" )

#		summary = res.get_audio_summary()
				

	def calculateEnergyQuotient ( src, maxEnergy, maxLive, maxDance, maxAcoustics, maxTempo ) :
		return   ( maxEnergy + maxLive + maxDance ) / ( maxAcoustics * 3 ) 


	def defineSets ( src ):
		'''bangerOffset = i = int(setDuration/12)
		while i < 0:
			createNewSet
			add songs[i] 

		while numberOfMediumSongsLeft > 0:
			for eachSet :
				for eachMediumSong :
					temp = songs[bangerOffset + 1]
					if maxTempo*maxLive_banger - maxTempo*maxLive_newlistSong < maxTempo*maxLive_banger - maxTempo*maxLive_savedListSong :
						temp = newlistSong
				end
				add tempSong to set
				
		for j = endIndex-bangerOffset set = i
			add song[j] to set[i]
			j+=1
			i+=1
'''

	def scanPlaylistDirectory( src, filePath ):
		extract = MetadataManipulation()

		for root, dirs, songFiles in walk( filePath ) :
			for song in songFiles:
				#get metadata
				print song
				
				extract.setPath( root + song )
				extract.loadMp3DataObject()
				print vars(extract)	

				src.getEchonestSongData( extract.getArtist(), extract.getSong() )


test = PlaylistQuery()
test.scanPlaylistDirectory( "/home/kbrown/Music/" )
#test.calculateEnergyQuotient( 0.5, 0.5, 0.5, 0.5, 0.5 )

#test.getEchonestSongData( "One Republic", "Counting Stars" )
#test.getEchonestSongData( "Justin Bieber", "Baby" )




