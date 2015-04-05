from pyechonest import config
from pyechonest import artist


config.ECHO_NEST_API_KEY = "EZTRYZBZU8BTT2PK2"


kc_results = artist.search( "One Republic" )

print kc_results




