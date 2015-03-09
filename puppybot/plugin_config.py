# CONFIGS FOR PLUGINS HERE
from collections import namedtuple

# PUPPY CONFIG
PuppyCommand = namedtuple('PuppyCommand', ['puppy_type',
'command',
'flickr_group_id',
'reply_prefix'])


AIBO = PuppyCommand('aibo', 'aibo', '51035597776@N01', 'Beep')
BEAGLE = PuppyCommand('beagle', 'beagle', '93217210@N00', 'Aroooooooo!')
BIGDOG = PuppyCommand('bigdog', 'big dog', '358732@N20', 'Woof!')
BULLDOG = PuppyCommand('bulldog', 'frenchie!', '50881036@N00', 'Mais oui!')
BUNNY = PuppyCommand('bunny', 'bunny', '480083@N22', 'Silly wabbit')
CHICKEN = PuppyCommand('chicken', 'chicken', '16442223@N00', 'a-coodle-doodle-doo!')
COCKTAIL = PuppyCommand('cocktail', 'drink', '57434090@N00', 'Happy hour')
CORGI = PuppyCommand('corgi', 'corgi', '42653350@N00', "OMG corgi!")
DONUT = PuppyCommand('donut', 'hungry', '388345@N24', '*omnomnomnomnom*')
DOXY = PuppyCommand('doxy', 'hotdog', '52240151476@N01', "Dachshund time")
GENERIC = PuppyCommand('puppy', 'puppy lottery', '35034344814@N01', "Puppy lottery!")
GOLDEN = PuppyCommand('golden', 'golden', '36618758@N00', 'Ruff!')
HUSKY = PuppyCommand('husky', 'husky', '81839844@N00', 'Wooooo!')
IGUANA = PuppyCommand('iguana', 'iguana', '14757429@N00', "Eww!")
KINGS = PuppyCommand('LA Kings photo', 'go kings', '442911@N21', "Go Kings Go!")  
KITTEN = PuppyCommand('kitten', 'kitten', '52185806@N00', 'Kitteh')
PANDA = PuppyCommand('panda', 'panda', '518319@N22', 'Time for pandas')
POOS = PuppyCommand('poodlemix', 'poodle', '1884736@N25', 'Ouah')
PUG = PuppyCommand('pug', 'pug', '57017533@N00', "Pug for you")
PYR = PuppyCommand('pyrenees', 'pyr', '667639@N24', 'Arf')
SAMOYED = PuppyCommand('samoyed', 'samoyed', '922784@N21', 'So fluffy')
SHIBA = PuppyCommand('shiba', 'shiba', '485910@N25', 'Shiba wow')
SHIHTZU = PuppyCommand('shihtzu', 'shihtzu', '30751387@N00', 'Pup pup')
VINTAGE_MOTORCYCLES = PuppyCommand('motorcyle', 'vroom', '978661@N20', "Awww yisss vroom vroom")
WESTIE = PuppyCommand('westie', 'westie', '93716354@N00', 'Arf!')
WOMBAT = PuppyCommand('wombat', 'wombat', '38109305@N00', 'Wombat')

AVAILABLE_COMMANDS = set([GENERIC,
                AIBO,
                BEAGLE,
                BIGDOG,
                BULLDOG,
                BUNNY,
                CHICKEN,
                COCKTAIL,
                CORGI,
                DONUT,
                DOXY,
                GOLDEN,
                HUSKY,
                IGUANA,
                KINGS,
                KITTEN,
                PANDA,
                POOS,
                PUG,
                PYR,
                SAMOYED,
                SHIBA,
                SHIHTZU,
                VINTAGE_MOTORCYCLES,
                WESTIE,
                WOMBAT])

PHOTOS_PER_PAGE = 20
MAX_API_CALLS = 30

# LINK LOG CONFIG
LOG_LINKS = True
LINK_LOG_FILE = 'links_in_channel.txt'