
class ImageBlock():
	def __init__(self, num_images, image_paths):
		self.num_images = num_images
		self.image_paths = image_paths


images_lander_larry_1 = ImageBlock(2, ["images/landerlarry01.png", "images/landerlarry02.jpg"])
images_lander_larry_2 = ImageBlock(2, ["images/landerlarry03.jpg", "images/landerlarry04.jpg", "images/landerlarry05.jpg", ])
images_foxes_chickens_1 = ImageBlock(2, ["images/foxes00.png", "images/foxes01.png", "images/foxes04.png"])


# Home content
home_content_blocks = [
	'''
	This site exists in lieu of a facebook/etc page as I'm not a fan.
	It's mostly a place for me to chuck projects I'm working 
	on or hobbies.
	''',
	'''
	I do lots of programming in my job but also do it as a hobby. I have a 
	particular interest in game development and procedural 
	generation/programmatically generated art. I am an amateur potter and 
	mainly make slab-built geometric pots. I also collect fossils.
	'''
					]


# Programming content
programming_content_blocks = [
	'''
	Here are some of my hobby programming projects. Some have source 
	available on <a href="https://gitlab.com/jmahon">GitLab</a> or 
	<a href="https://github.com/joemahon89/">GitHub</a>, but 
	if not its likely because the code is a bit messy. If you 
	are interested in something where the source isn't public let me 
	know and I can likely neaten it up enough to share! 
	''',

	'''
	<ul>
		<li><a href="#procbirds">"Procedural Birds" Twitter bot</a> ( art 🎨 / procedural generation 🔄 / bots 🤖 )</li>
		<li><a href="#blenderface">Blender face extractor</a> ( ceramics 🏺 / 3D modeling 🎨 )</li>
		<li><a href="#foxeschickens">"Foxes and Chickens" game</a> ( gamedev 🕹 / Android 🤖 )</li>
		<li><a href="#landerlarry">"Lander Larry" game</a> ( gamedev 🕹 / Android 🤖 )</li>
		<li><a href="#spacecowboy">"Space Cowboy" game (made in <48h for LDJAM)</a> ( gamedev 🕹 )</li>
		<li><a href="#miscgames">Other small miscellaneous prototypes and projects</a></li>
	</ul>
	''',

	'''
	<h2 id="procbirds">"Procedural Birds" Twitter bot</h2> 
	I am interested in procedural generation and generative art, where 
	images are created using systems and rules defined in code. I wrote 
	a program which generates simple, stylised images of birds. Each image 
	is created from scratch and is completely unique. Every line, angle, 
	colour is decided using randomness within defined limits. 
	''',
	'''
	The birds are built line by line, starting at the right-most foot, 
	drawing the neck length and angle based on the reasonable 
	approximations of the possible angles that a bird's neck may have. 
	The head is a random percentage of a full circle between two limits.
	The beak can attach at numerous points on the head and have variable 
	thicknesses and colours. The angle of the back varies, and can result 
	birds ranging in appearance from from a long-necked goose-like bird to 
	stumpy quails. The tail angle, thickness, colour, number of feathers 
	is all computed and drawn. The leg length and angle is chosen based on 
	the approximate center of gravity of the bird, so that it doesn't look 
	like it will topple over! The colours are chosen from colour schemes 
	defined in code, and there is a probability that the bird may have 
	different coloured wings or tail or both.
	''',
	'''
	The program also generates names for the birds based on their features.
	For example, a bird where the tail has been drawn with short lines may 
	have the prefix 'short-tailed' or 'stub-tailed'. Birds with larger angles 
	between the lines on their back may have the prefix 'hump-backed'. The 
	colours are also used as descriptors, with ornithological sounding 
	additions, e.g. 'golden-tailed', 'candy winged', 'bronze-feathered'.
	''',
	'''
	I stuck the program onto a Raspberry Pi and wrote a small Twitter bot 
	which generates a new bird every hour, names it based on its features 
	and posts the image on Twitter. 
	''',
	'''
	<a href="https://twitter.com/pybirdbot/">
		Bird bot Twitter account 🐦
	</a>
	''',
	'''
	<a href="#top">Back to top</a>
	''',


	'''
	<h2 id="landerlarry">Lander Larry </h2> 
	This is the first Android game I developed. The player controls 
	a space ship and navigates from the start of the level to a landing pad 
	at the end of the level. There are obstacles along the way including 
	moving lava, gravitational anomalies and falling rocks. The game is free
	and there are no ads or in-app-purchases. 
	<a href="https://play.google.com/store/apps/details?id=org.godotengine.landerlarry">
		Google Play Store
	</a>
	''',
	images_lander_larry_1,
	images_lander_larry_2,
	'''
	<a href="#top">Back to top</a>
	''',

	'''
	<h2 id="foxeschickens">Foxes and Chickens </h2> 
	This is the second Android game that I published. It is a family-friendly 
	puzzle game, where the aim of the game is to move your chickens into their 
	coops using a limited number of moves (and without getting eaten by 
	foxes!). Levels can be completed in 4, 5 or 6 moves depending on 
	difficulty. There are 60 levels and there is only a single solution to 
	each level which adds to the challenge. The game is free and there are no 
	ads or in-app-purchases. 
	<a href="https://play.google.com/store/apps/details?id=com.a4x8e6.foxesandchickens">
		Google Play Store
	</a>
	''',
	images_foxes_chickens_1,
	'''
	<a href="#top">Back to top</a>
	''',


					]

# Ceramics content
ceramics_content_blocks = [
	'''
	I have been doing ceramics/pottery for a few years. I started with an 
	evening class once a week, but now just do my own thing and take my pieces 
	to a local studio for firing. I am still a definite amateur and mostly 
	make things up as I go along.
	''',
	'''
	I really like geometric, angular forms and so this is what I make the 
	most of. These are made using clay which has been wedged (kneaded to 
	remove the air) and rolled out to the desired thickness. Shapes can then 
	be cut out and joined together by scoring the edge of the clay and 
	applying wet clay (a bit like glue). The angles required for this can 
	be a bit tricky so I wrote a Blender script so I could easily create 
	designs and made an adjustable mitre cutter to cut any angle.

	'''











					]


fossils_content_blocks = [
	'''
	I enjoy looking for fossils. The most productive area somewhat close to 
	me is the East/North Yorkshire coast. Some locations on this coastline 
	are productive for Jurassic fossils like 
	<a href="#ammonites">ammonites</a>, <a href="#belemnites">belemnites</a> 
	(squid-like creatures) and <a href="#bivalves">bivalves</a> (shells). 
	You can also find marine reptile remains (although I have yet to find 
	any!) and <a href="#jet">Whitby jet</a>. Here are some of my favourite 
	fossils that I have collected &#129460;
	'''


privacy_policy_content_blocks = [
	'''
	<h2>Privacy Policy</h2>
	The following privacy policy applies to the apps Lander Larry and 
	Foxes and Chickens which are published on the Google Play Store.
	None of the games or apps published by a4x8e6 collect, record, store or 
	process	any personal information. Your data is stored on your device. 
	There are no analytics collected. These apps do not access sensitive 
	permissions or data.
	Android or the Google Play store itself may track and send data (e.g 
	crash reports), but this is beyond our control
	'''






					]

test_url = '<a href=""></a>'

span_inside_header = '''
						<span>
							<a href="https://play.google.com/store/apps/details?id=org.godotengine.landerlarry">
								Free on Google Play Store
							</a> 
						</span>
					'''

