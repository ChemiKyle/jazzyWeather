# jazzyWeather
Two of my favorite things are jazz and waking up with a worryingly small amount of time to get ready. I occasionally have slow networking on my cell phone, but that's not one of my favorite things.


I've lived in quite a few places with somewhat unpredictable weather, so I made this small program to play a song as my alarm, the song chosen depends on the chance of precipitation and the season, so that Pavlovian conditioning will lead me to grab a rain coat while I'm rushing out the door to barely make the bus.  
Salivation not included.

## I don't care about your life story, what's it do? 
Play a different song according to the weather and (optionally) the season.  
Place desired music files in subdirectories for `clear/`, `rain/`, and `snow/` conditions (also needed in each season directory if using the seasons).  

Requires the vlc module and must be run with python2. `sudo pip install python-vlc`

Utilize the slowVolume.py script for a more gentle wake up a la Android smart alarm (requires alsaaudio module for python).

TODO:  
  Find some way to query the alarm time for my phone and use that instead of a cron job
