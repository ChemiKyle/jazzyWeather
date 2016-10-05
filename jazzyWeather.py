import os, random, datetime, urllib2, json, vlc, time

musicDir = "/path/to/files"

date = datetime.datetime.now()

month = str(date.month)
day = str(date.day)

# precede the date with a 0 if it's before the 10th; otherwise the first 9 days of every month are winter!
if int(day) <= 9:
	day = "0" + day

# fetch month and date as strings, concatenate, redefine as integer
dateNum = int(month + day)

# Check date against concatenated dates of seasons, choose the season accordingly
seasonsOn = 0
if seasonsOn == True:
	if dateNum >= 1221 or dateNum < 320:
		season = "winter/"
	elif dateNum >= 922:
		season = "autumn/"
	elif dateNum >= 621:
		season = "summer/"
	elif dateNum >= 320:
		season = "spring/"
else:
	season = ""

# Stuff for interacting with the wunderground API, can obviously be adapted to any service
apiKey = "" # You can't have mine, but you can get your own for free here: https://www.wunderground.com/?apiref=50c69f4667601846
yourLocalStation = "" # Go to the wunderground site and choose your nearest station
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/conditions/q/pws:' + yourLocalStation + '.json')
json_string = f.read()
parsed_json = json.loads(json_string)
pop = parsed_json['forecast']['txt_forecast']['forecastday'][0]['pop'] # Get the chance of precipitation for the current day
f.close()

# Choose the weather directory according to the chance of rain (or snow, but that's a todo)
if pop < 30:
    forecast = "clear/"
elif pop >= 30 and snow != True:
    forecast = "rain/"
elif snow == True:
 	forecast = "snow/"

#Pick a random song from the directory
song = random.choice(os.listdir(musicDir + season + forecast))
song = vlc.MediaPlayer(musicDir + season + forecast + song)
song.play()
# Do some kung-fu to make it actually play the whole song
time.sleep(1)
songLength = song.get_length()
timeRemaining = ((songLength/1000) - 1)*60
time.sleep(timeRemaining)
