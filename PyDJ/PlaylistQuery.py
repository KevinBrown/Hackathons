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

		summary = res.get_audio_summary()
				

	def calculateEnergyQuotient ( src, maxEnergy, maxLive, maxDance, maxAcoutics, maxTempo ) :
		return   ( maxEnergy + maxLive + maxDance ) / ( maxAcoustics * 3 ) 

	def defineSets ()

		bangerOffset = i = int(setDuration/12)
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



	def scanPlaylistDirectory( src, filePath ):
		song = 
	
		for root, dirs, songFiles in walk( filePath ) :
			for song in songFiles:
				#get metadata
				print song
				src.getEchonestSongData()


test = PlaylistQuery()
test.scanPlaylistDirectory( "/home/kbrown/Music/" )




