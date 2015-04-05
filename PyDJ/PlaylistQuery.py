from pyechonest import config
from pyechonest import artist

import sqlite3
from os import walk

#import metadatalib

config.ECHO_NEST_API_KEY = "EZTRYZBZU8BTT2PK2"


class PlaylistQuery():

	def getEchonestSongData ( src, artist, songName ) :
		res = song.search( artist, songName )
		
		if not res:
			raise Exception( "SongNotFound" )

		

	def calculateEnergyQuotient ( src, maxEnergy, maxLive, maxDance, maxAcoutics, maxTempo ) :
		return (maxTempo / 150 ) * ( ( maxEnergy + maxLive + maxDance ) / ( maxAcoustics * 3 ) )


	def scanPlaylistDirectory( src, filePath ):
		for root, dirs, songFiles in walk( filePath ) :
			for song in songFiles:
				#get metadata
				print song


test = PlaylistQuery()
test.scanPlaylistDirectory( "/home/kbrown/Music/" )




