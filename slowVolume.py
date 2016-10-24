import alsaaudio, time

n = 80 # Initial volume, I'm using spare headphones so I have to start really high

m = alsaaudio.Mixer('PCM', 0) # Preconfig for raspberry pi, if using something else you'll have to run alsaaudio.mixers() in python
m.setvolume(n)

while n < 100:
	m.setvolume(n)
	n += 2.5 # Increment the volume higher
	time.sleep(2)
