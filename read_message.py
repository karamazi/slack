# Read Message
# Listens to slack outgoing hook and responds with a nice 'lil image.

import random
from bottle import post, request, run

SHIT_AUTH=b"token=HET8q577DUeWqdQsf77sda5u&"

imgs = [
"http://orig04.deviantart.net/137f/f/2014/147/3/1/random_character__jet_bear_by_mnrart-d7jwteg.gif",
"http://globalgamejam.org/sites/default/files/styles/game_sidebar__normal/public/game/featured_image/promo_5.png",
"http://payload345.cargocollective.com/1/0/19261/9211166/random_ani_buns_600x600.gif",
"http://www.somerandomfacts.com/wp-content/uploads/2013/11/jpg1",
"http://www.rhaein.com/funnystuff/images/random/random242.jpg",
"https://s-media-cache-ak0.pinimg.com/236x/df/ba/46/dfba46378bc65a62a81733ed714c839b.jpg"
]
@post('/')
def reply_to_slack():
	data = request.body.read()
	if not SHIT_AUTH in data:
		return "Nuhuh"
	
	index = random.randint(0,len(imgs)-1)
	return '{"text": "'+imgs[index]+'"}'

run(host='0.0.0.0', port=45678, debug=True)