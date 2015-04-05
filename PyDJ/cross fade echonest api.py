

	def customCrossFade(dataA,dataB, seconds):
		customFadeOut(dataA,seconds)
		customFadeIn(dataB,seconds/3)
		
		newdata = AudioData(ndarray=dataA.data, sampleRate=dataA.sampleRate, numChannels=dataA.numChannels, defer=False) 
		i = dataA.endindex - (seconds/3)*sampleRate
		j = 0
		while i <= dataA.endindex:
			newdata.data[i] = dataA[i] + dataB[j]
			i += 1
			j += 1

		while j < dataB.endindex:
			newdata.data[i] += dataB[j]
			i +=1
			j +=1

		return newdata

def customFadeOut(self,seconds):
  	i = endindex - seconds*sampleRate
  	x = 1
  	while i <= endindex:
  		self.data[i] += self.data[i]*(-.100000x)
  		x += 1
  		i += 1

def customFadeIn(self,seconds):
  	i = 0 
  	x = 1
  	while i <= seconds*sampleRate:
  		self.data[i] -= self.data[i]*(1/x)
  		x += .8
  		i += 1

